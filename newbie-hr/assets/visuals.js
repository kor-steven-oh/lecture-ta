// Local teaching demos only: no requests, arbitrary command execution, or stored user data.
function initVisuals(){
 document.querySelectorAll('.step-demo').forEach(d=>{
  const buttons=[...d.querySelectorAll('[data-step-select]')];
  const select=i=>{d.dataset.step=i;buttons.forEach((b,j)=>b.setAttribute('aria-pressed',j===i));d.querySelectorAll('[data-step-panel]').forEach((p,j)=>p.hidden=j!==i)};
  buttons.forEach((b,i)=>b.onclick=()=>select(i));d.querySelector('.demo-next').onclick=()=>select((Number(d.dataset.step)+1)%buttons.length);
 });
 document.querySelectorAll('.token-demo').forEach(d=>{
  const tokens=[...d.querySelectorAll('.token')];const next=d.querySelector('.token-next');
  const update=i=>{d.dataset.token=i;tokens.forEach((t,j)=>t.classList.toggle('revealed',j<=i));next.disabled=i===tokens.length-1};
  next.onclick=()=>update(Number(d.dataset.token)+1);d.querySelector('.token-reset').onclick=()=>update(0);
 });
 document.querySelectorAll('.context-demo').forEach(d=>{
  d.querySelector('input').oninput=e=>{const v=Number(e.target.value);d.querySelector('output').textContent=45+v;d.querySelector('.log-segment').style.setProperty('--portion',v);d.querySelector('.context-meter').setAttribute('aria-label',`고정 지침 20, 핵심 자료 25, 대화와 로그 ${v}, 총 ${45+v} / 100`);d.querySelector('.context-message').textContent=v>=45?'문맥이 거의 찼습니다. 관련 없는 로그를 줄이고 결정 사항을 보존하세요.':'현재 목표와 관련 있는 자료를 우선 보존하세요.'};
 });
 document.querySelectorAll('.terminal-demo').forEach(d=>{
  d.querySelectorAll('[data-terminal-command]').forEach(b=>b.onclick=()=>{
   const cmd=b.dataset.terminalCommand;let dir=d.dataset.dir,result='';
   if(cmd==='처음으로'){dir='workshop';result='현재 폴더 → /practice/workshop'}
   if(cmd==='pwd')result='/practice/'+dir;
   if(cmd==='ls')result=dir==='workshop'?'materials/   output/   README.md':dir==='workshop/materials'?'policy.md   faq.md   schedule.csv':'workshop/';
   if(cmd==='cd materials'){if(dir==='workshop'){dir='workshop/materials';result='현재 폴더 → /practice/'+dir}else result='현재 위치에 materials 폴더가 없습니다.'}
   if(cmd==='cd ..'){dir=dir==='workshop/materials'?'workshop':'';result='현재 폴더 → /practice/'+dir}
   d.dataset.dir=dir;const screen=d.querySelector('.terminal-screen');screen.replaceChildren();const c=document.createElement('p');c.className='terminal-command';c.textContent='$ '+(cmd==='처음으로'?'pwd':cmd);const r=document.createElement('p');r.className='terminal-output';r.textContent=result;screen.append(c,r);
  });
 });
 document.querySelectorAll('.diff-demo').forEach(d=>d.querySelectorAll('[data-diff]').forEach(b=>b.onclick=()=>{const after=b.dataset.diff==='after';d.classList.toggle('changed',after);d.querySelectorAll('[data-diff]').forEach(x=>x.setAttribute('aria-pressed',x===b));d.querySelectorAll('.diff-line').forEach(l=>l.textContent=l.dataset[after?'after':'before'])}));
 document.querySelectorAll('.check-demo').forEach(d=>d.querySelectorAll('input').forEach(c=>c.onchange=()=>d.querySelector('output').textContent=d.querySelectorAll('input:checked').length));
 const dialog=document.createElement('dialog');dialog.className='image-dialog';dialog.setAttribute('aria-labelledby','referenceTitle');dialog.innerHTML='<header><span id="referenceTitle" class="reference-title">공식 참고 도해</span><button class="image-dialog-close">닫기 · Esc</button></header><img alt=""><p>© Anthropic · 공식 문서에서 발췌 · 원본 비율 유지</p>';document.body.append(dialog);
 dialog.querySelector('button').onclick=()=>dialog.close();dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}});
 document.querySelectorAll('.zoom-image').forEach(b=>b.onclick=()=>{const image=b.querySelector('img');const target=dialog.querySelector('img');target.src=image.src;target.alt=image.alt;dialog.querySelector('#referenceTitle').textContent=b.closest('.slide').querySelector('h1').textContent;dialog.showModal()});
 document.querySelectorAll('.section:not(.cover)').forEach(s=>{const ch=Number(s.querySelector('.eyebrow').textContent.slice(0,2));if(!Number.isFinite(ch))return;const scale=document.createElement('div');scale.className='chapter-scale';scale.setAttribute('aria-hidden','true');for(let i=1;i<=8;i++){const node=document.createElement('span');if(i<=ch)node.className='completed';scale.append(node)}s.querySelector('.body').append(scale)});
}
initVisuals();
