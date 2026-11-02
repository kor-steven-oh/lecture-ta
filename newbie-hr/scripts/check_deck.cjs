const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');

async function main() {
  const root = path.resolve(__dirname, '..');
  const out = path.join(root, '.qa');
  fs.mkdirSync(out, { recursive: true });
  const macChrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const executablePath = process.env.CHROME_PATH || (fs.existsSync(macChrome) ? macChrome : undefined);
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const context = await browser.newContext({ permissions: ['clipboard-read', 'clipboard-write'], reducedMotion: 'reduce' });
    const page = await context.newPage();
    const errors = [], externalRequests = [];
    page.on('pageerror', err => errors.push(err.message));
    page.on('request', req => { if (/^https?:/.test(req.url())) externalRequests.push(req.url()); });
    const url = pathToFileURL(path.join(root, 'index.html')).href;
    await page.goto(url);
    const slides = JSON.parse(fs.readFileSync(path.join(root, 'slides.json'), 'utf8'));
    assert.equal(await page.locator('.slide').count(), slides.length);
    const go = async title => {
      const index = slides.findIndex(s => s.title === title);
      assert.ok(index >= 0, title);
      await page.evaluate(i => show(i), index);
    };
    const report = { slides: slides.length, visuals: await page.locator('.visual-slide').count(), referenceImages: await page.locator('.reference-figure').count(), viewports: {} };
    for (const [width, height] of [[1440, 900], [1280, 720], [390, 844]]) {
      await page.setViewportSize({ width, height });
      const overflows = [];
      for (let i = 0; i < slides.length; i++) {
        await page.evaluate(i => show(i), i);
        const box = await page.locator('.slide:not([hidden])').evaluate(el => ({
          bottom: el.getBoundingClientRect().bottom,
          toolbarTop: document.querySelector('.toolbar').getBoundingClientRect().top,
          pageWidth: document.documentElement.scrollWidth,
          viewportWidth: innerWidth
        }));
        if (box.pageWidth > box.viewportWidth + 1 || (width > 800 && box.bottom > box.toolbarTop + 1)) overflows.push({ slide: i + 1, ...box });
      }
      report.viewports[`${width}x${height}`] = overflows;
      assert.deepEqual(overflows, [], `Overflow at ${width}x${height}`);
    }
    await page.setViewportSize({ width: 1280, height: 720 });
    await go('LLM은 토큰을 이어서 생성한다');
    for (let i = 0; i < 5; i++) await page.locator('.token-next').click();
    assert.equal(await page.locator('.token.revealed').count(), 6);
    assert.ok(await page.locator('.token-next').isDisabled());
    await page.locator('.token-reset').click();
    assert.equal(await page.locator('.token.revealed').count(), 1);

    await go('컨텍스트는 지금 펼쳐 둔 작업 자료');
    const range = page.locator('.slide:not([hidden]) input[type=range]');
    await range.fill('55');
    assert.equal(await page.locator('.slide:not([hidden]) output').innerText(), '100');
    await range.fill('0');
    assert.equal(await page.locator('.slide:not([hidden]) output').innerText(), '45');
    const slideAtRange = await page.locator('#counter').innerText();
    await range.focus();
    await page.keyboard.press('ArrowRight');
    assert.equal(await page.locator('#counter').innerText(), slideAtRange, 'Range input must not navigate slides');

    await go('기본 명령 · macOS / Linux');
    await page.getByRole('button', { name: 'cd materials', exact: true }).click();
    await page.getByRole('button', { name: 'pwd', exact: true }).click();
    assert.match(await page.locator('.terminal-output').innerText(), /workshop\/materials/);
    await page.getByRole('button', { name: 'ls', exact: true }).click();
    assert.match(await page.locator('.terminal-output').innerText(), /policy.md/);
    await page.getByRole('button', { name: '처음으로', exact: true }).click();
    assert.equal(await page.locator('.terminal-demo').getAttribute('data-dir'), 'workshop');

    await go('diff는 변경 전후의 차이');
    await page.getByRole('button', { name: '변경 후', exact: true }).click();
    assert.match(await page.locator('.diff-line').first().innerText(), /확인 필요/);
    await page.getByRole('button', { name: '변경 전', exact: true }).click();
    assert.equal(await page.locator('.diff-line').first().innerText(), '첫날 집합: 09:30');

    await go('좋은 요청의 다섯 요소');
    await page.locator('.slide:not([hidden]) .demo-next').click();
    assert.equal(await page.locator('.slide:not([hidden]) .step-demo').getAttribute('data-step'), '1');
    assert.equal(await page.locator('.slide:not([hidden]) [data-step-panel]:not([hidden])').count(), 1);
    await go('수용 기준 · 통과 여부를 직접 확인');
    for (const checkbox of await page.locator('.check-demo input').all()) await checkbox.check();
    assert.equal(await page.locator('.check-demo output').innerText(), '4');

    assert.ok(await page.locator('.reference-figure img').evaluateAll(imgs => imgs.every(i => i.complete && i.naturalWidth > 0)));
    await go('공식 도해 · 위임과 팀 협업');
    await page.locator('.slide:not([hidden]) .zoom-image').click();
    assert.ok(await page.locator('dialog').evaluate(el => el.open));
    const before = await page.locator('#counter').innerText();
    await page.keyboard.press('ArrowRight');
    assert.equal(await page.locator('#counter').innerText(), before);
    await page.keyboard.press('Escape');
    assert.ok(!(await page.locator('dialog').evaluate(el => el.open)));
    await page.keyboard.press('t');
    await page.locator('#search').fill('MCP');
    assert.ok(await page.locator('#tocList button').count() > 0);
    await page.keyboard.press('Escape');
    await page.keyboard.press('n');
    assert.ok(await page.locator('.slide:not([hidden]) .notes').isVisible());
    await page.keyboard.press('n');
    await page.keyboard.press('Home');
    await page.keyboard.press('ArrowRight');
    assert.equal(await page.locator('#counter').innerText(), `2 / ${slides.length}`);
    await go('퀴즈 1 · 파일이 바뀌지 않는 이유');
    await page.locator('.slide:not([hidden]) summary').click();
    assert.ok(await page.locator('.slide:not([hidden]) details').evaluate(el => el.open));
    await go('문서 검토 Skill 예시');
    await page.locator('.slide:not([hidden]) .copy').click();
    await page.locator('#toast').waitFor({ state: 'visible' });
    assert.ok(await page.evaluate(async () => await navigator.clipboard.readText() === document.querySelector('.slide:not([hidden]) code').textContent));

    const examples = ['전체 목차와 권장 시간','AI와 LLM의 관계','좋은 요청의 다섯 요소','MCP는 도구 연결 규약','공식 도해 · 위임과 팀 협업','Git은 프로젝트의 변경 기록','지침·권한·샌드박스의 역할','업무 실행 전 체크리스트','기본 명령 · macOS / Linux','병렬 처리할 수 있는 일'];
    for (const [i, title] of examples.entries()) {
      await go(title);
      await page.screenshot({ path: path.join(out, `visual-${i + 1}.png`) });
    }
    await page.setViewportSize({ width: 390, height: 844 });
    await go('MCP는 도구 연결 규약');
    await page.screenshot({ path: path.join(out, 'mobile.png'), fullPage: true });
    await page.setViewportSize({ width: 1280, height: 720 });
    await page.pdf({ path: path.join(out, 'deck.pdf'), preferCSSPageSize: true, printBackground: true });
    await page.emulateMedia({ reducedMotion: 'no-preference' });
    await go('AI와 LLM의 관계');
    assert.equal(await page.locator('.slide:not([hidden]) h1').evaluate(el => getComputedStyle(el).animationName), 'slide-enter');
    await page.emulateMedia({ reducedMotion: 'reduce' });
    assert.equal(await page.locator('.slide:not([hidden]) h1').evaluate(el => getComputedStyle(el).animationName), 'none');
    assert.deepEqual(errors, []);
    assert.deepEqual(externalRequests, []);
    report.errors = errors;
    report.externalRequests = externalRequests;
    report.interactions = 'passed';
    fs.writeFileSync(path.join(out, 'report.json'), JSON.stringify(report, null, 2));
    console.log(JSON.stringify(report, null, 2));
  } finally { await browser.close(); }
}
main().catch(err => { console.error(err); process.exitCode = 1; });
