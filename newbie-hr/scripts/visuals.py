"""Educational diagrams and interactions, rendered as native HTML/SVG.
All illustrative quantities are explicitly labeled; no measured AI benchmarks.
"""
from html import escape as e
from pathlib import Path
import base64

ASSETS = [
 dict(after='채팅과 에이전트의 차이', title='공식 도해 · 도구가 연결된 LLM',file='augmented-llm.png',source='agents',origin='https://www-cdn.anthropic.com/images/4zrzovbb/website/d3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png',alt='입력과 출력 사이의 LLM에 검색, 도구, 메모리가 양방향으로 연결된 Anthropic 공식 도해',lead='검색은 자료를 가져오고, 도구는 행동하고, 메모리는 정보를 남깁니다.',items=['Retrieval = 검색 · Tools = 도구 · Memory = 기억','온보딩 예: 규정 찾기 → 파일 작성 → 다음 작업 기록']),
 dict(after='작업 루프를 읽는 법',title='공식 도해 · 에이전트의 작업 루프',file='agentic-loop.svg',source='how-claude-code-works',origin='https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/agentic-loop.svg',alt='프롬프트 다음에 문맥 수집, 행동, 결과 검증이 반복되며 사용자가 언제든 방향을 조정하는 공식 작업 루프',lead='한 번의 답변 안에서도 읽기·실행·검증이 여러 번 반복될 수 있습니다.',items=['Gather context → Take action → Verify results','사용자는 도중에 중단하거나 자료와 방향을 보완할 수 있음']),
 dict(after='Agent teams · 실험적 기능',title='공식 도해 · 위임과 팀 협업',file='agent-teams.png',source='agent-teams',origin='https://mintcdn.com/claude-code/nsvRFSDNfpSU5nT7/images/subagents-vs-agent-teams-light.png',alt='왼쪽은 주 에이전트에 결과를 보고하는 서브에이전트, 오른쪽은 공유 작업 목록과 동료 간 통신을 사용하는 Agent teams',lead='왼쪽은 결과를 받아 통합하는 구조, 오른쪽은 동료끼리 조정하는 구조입니다.',items=['Subagents: 좁은 과업 위임과 결과 회수에 적합','Agent teams: 동료 간 논의가 필요한 작업 · 실험적 기능']),
 dict(after='고급 에이전트 설계 패턴',title='공식 도해 · 단계 사이의 검증',file='prompt-chaining.png',source='agents',origin='https://www-cdn.anthropic.com/images/4zrzovbb/website/7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png',alt='LLM 호출 1의 출력이 Gate를 통과하면 호출 2와 3으로 이어지고 실패하면 종료하는 프롬프트 연쇄 도해',lead='중간 결과가 기준을 통과해야 다음 작업으로 넘어갑니다.',items=['Gate = 검사 지점 · Pass = 통과 · Fail = 실패','온보딩 예: 정보 추출 → 근거 검사 → 초안 → 표현 정리']),
]

def enrich(slides, sources, root):
 sources['mcp-architecture']='https://modelcontextprotocol.io/docs/learn/architecture'
 for asset in ASSETS:
  at=next(i for i,s in enumerate(slides) if s['title']==asset['after'])
  slides.insert(at+1,dict(chapter=slides[at]['chapter'],title=asset['title'],lead=asset['lead'],items=asset['items'],code='',label='',note='Anthropic 공식 원문 도해를 발췌해 원래 비율로 표시했다. 영문 레이블을 한국어 설명과 함께 읽는다. 이미지를 누르면 확대된다. 도해는 개념 설명이며 실제 실행 기록이나 성능 측정 결과가 아니다. 출처 확인: 2026-11-03.',sources=[asset['source']],kind='reference',answer='',asset=asset))
 for slide in slides:
  if slide['title']=='MCP는 도구 연결 규약': slide['sources'].append('mcp-architecture')
  if slide['title'] in SPECS: slide['visual']=SPECS[slide['title']][0]
 return slides

def flow(labels, caption='', vertical=False):
 return '<div class="flow '+('vertical' if vertical else '')+'">'+''.join('<div class="flow-step"><span class="step-number">'+str(i+1).zfill(2)+'</span><strong>'+e(label)+'</strong></div>'+('<span class="connector" aria-hidden="true">'+('↓' if vertical else '→')+'</span>' if i<len(labels)-1 else '') for i,label in enumerate(labels))+'</div>'+('<p class="diagram-caption">'+e(caption)+'</p>' if caption else '')
def compare(columns):
 return '<div class="compare">'+''.join('<div><h3>'+e(title)+'</h3><p>'+e(body)+'</p><span>'+e(foot)+'</span></div>' for title,body,foot in columns)+'</div>'
def table(headers,rows):
 return '<div class="table-wrap"><table class="visual-table"><thead><tr>'+''.join('<th scope="col">'+e(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if i==0 else '<td>')+e(x)+('</th>' if i==0 else '</td>') for i,x in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'
def stepper(labels,descriptions):
 return '<div class="step-demo" data-step="0"><div class="step-tabs">'+''.join(f'<button type="button" data-step-select="{i}" aria-pressed="{str(i==0).lower()}"><span>{i+1:02d}</span>{e(label)}</button>' for i,label in enumerate(labels))+'</div><div class="step-description" aria-live="polite">'+''.join(f'<p data-step-panel="{i}" '+('' if i==0 else 'hidden')+'>'+e(desc)+'</p>' for i,desc in enumerate(descriptions))+'</div><button type="button" class="demo-next">다음 단계 →</button><span class="demo-hint">단계를 눌러 설명을 확인하세요</span></div>'
def tree():
 return '<div class="file-tree"><div>workshop/ <small>현재 작업 폴더</small></div><div class="branch">├─ materials/ <em>읽는 자료</em><div>│　├─ policy.md</div><div>│　├─ faq.md</div><div>│　└─ schedule.csv</div></div><div class="branch accent">└─ output/ <em>만드는 결과</em><div>　　└─ checklist.md</div></div></div>'
def bars(labels,values,unit,caption):
 maxval=max(values)
 return '<div class="bars">'+''.join('<div class="bar-row"><span>'+e(l)+'</span><div class="bar-track"><div class="bar-fill" style="--bar:'+str(v/maxval*100)+'%"></div></div><b>'+str(v)+e(unit)+'</b></div>' for l,v in zip(labels,values))+'</div><p class="diagram-caption">'+e(caption)+'</p>'

def custom(kind):
 if kind=='taxonomy':
  return '<div class="taxonomy"><div class="nest">AI <small>지능적 과업을 수행하는 기술</small><div class="nest">머신러닝 <small>데이터에서 패턴 학습</small><div class="nest">생성형 AI <small>텍스트·이미지·소리 생성</small><div class="nest">LLM <small>언어를 다루는 모델</small></div></div></div></div></div><p class="diagram-caption">이 수업에서 사용하는 범위의 단순화된 개념도</p>'
 if kind=='tokens':
  return '<div class="token-demo" data-token="0"><span class="visual-label">생성 중인 문장</span><div class="tokens" aria-live="polite">'+''.join('<span class="token '+('revealed' if i==0 else '')+'">'+e(t)+'</span>' for i,t in enumerate(['첫날',' 준비물','은',' 신분증','입니다','.']))+'</div><div class="token-model">현재 문맥 <span>→</span> 다음 조각 생성 <span>→</span> 문맥에 추가</div><div class="demo-controls"><button class="token-next">다음 조각 생성</button><button class="token-reset">처음으로</button></div><p class="diagram-caption">개념 시연 · 실제 Claude 토크나이저의 분할 결과가 아닙니다.</p></div>'
 if kind=='context':
  return '<div class="context-demo"><div class="meter-head"><span>가상의 작업 공간</span><b><output>60</output> / 100</b></div><div class="context-meter" role="img" aria-label="고정 지침 20, 핵심 자료 25, 조절 가능한 대화와 로그 15"><span style="--portion:20;--tone:var(--green)">지침</span><span style="--portion:25;--tone:#899b78">자료</span><span class="log-segment" style="--portion:15;--tone:var(--accent)">로그</span></div><label>대화·로그 양 <input class="context-range" type="range" min="0" max="55" value="15"></label><p class="context-message" aria-live="polite">현재 목표와 관련 있는 자료를 우선 보존하세요.</p><p class="diagram-caption">설명용 100칸 모형 · 실제 토큰 수·모델 한도가 아닙니다.</p></div>'
 if kind=='terminal':
  return '<div class="terminal-demo" data-dir="workshop"><div class="terminal-title">폴더 이동 연습 <span>브라우저 안의 모의 환경</span></div><div class="terminal-screen" role="log" aria-live="polite"><p class="terminal-command">$ pwd</p><p class="terminal-output">/practice/workshop</p></div><div class="terminal-commands">'+''.join('<button data-terminal-command="'+e(cmd)+'">'+e(cmd)+'</button>' for cmd in ['pwd','ls','cd materials','cd ..','처음으로'])+'</div><p class="diagram-caption">버튼은 실제 파일이나 터미널을 변경하지 않습니다.</p></div>'
 if kind=='diff':
  return '<div class="diff-demo"><div class="diff-switch"><button data-diff="before" aria-pressed="true">변경 전</button><button data-diff="after" aria-pressed="false">변경 후</button></div><div class="diff-pane" aria-live="polite"><span class="visual-label">checklist.md</span><p class="diff-line" data-before="첫날 집합: 09:30" data-after="첫날 집합: 09:30 / 10:00 · 담당자 확인 필요">첫날 집합: 09:30</p><p class="diff-line" data-before="장소: 7층 교육실" data-after="장소: 7층 교육실 / 2층 세미나실 · 확인 필요">장소: 7층 교육실</p><p class="diff-stable">준비물: 신분증, 개인 이어폰</p></div><p class="diagram-caption">실습 자료 기반 · 바뀌어야 할 정보만 고치고 나머지는 유지합니다.</p></div>'
 if kind=='mcp':
  return '<div class="mcp-map"><div class="host"><span class="visual-label">HOST · 앱</span><h3>Claude Code</h3><div class="clients"><span>MCP client A</span><span>MCP client B</span></div></div><div class="mcp-links"><span>↕ 로컬 stdio</span><span>↕ 원격 HTTP</span></div><div class="servers"><div><b>로컬 서버</b><span>허용된 파일</span></div><div><b>원격 서버</b><span>이슈·업무 자료</span></div></div><p class="diagram-caption">서버마다 별도 연결 · 인증과 도구 권한을 확인</p></div>'
 if kind=='git':
  return '<div class="git-map"><div class="git-line"><span>A<br><small>기준 상태</small></span><i>→</i><span>B<br><small>체크리스트</small></span><i>→</i><span>C<br><small>검증 완료</small></span></div><div class="git-branch">↳ 작업 브랜치 <b>D · HTML 초안</b></div><p class="diagram-caption">커밋은 선택한 상태의 기록 · push는 별도의 원격 전송</p></div>'
 if kind=='parallel':
  return '<div class="parallel-map"><div class="parallel-lead">주 에이전트 · 범위와 기준 전달</div><div class="parallel-arrows">↙　↓　↘</div><div class="workers"><span>정확성 검토<br><small>원문 대조</small></span><span>사용성 검토<br><small>화면 확인</small></span><span>누락 검토<br><small>요구사항 대조</small></span></div><div class="parallel-arrows">↘　↓　↙</div><div class="parallel-lead">결과 통합 · 오탐 제거 · 최종 확인</div></div>'
 if kind=='checklist':
  return '<div class="check-demo"><div class="check-score"><output>0</output><span>/ 4 확인</span></div>'+''.join('<label><input type="checkbox">'+e(x)+'</label>' for x in ['필수 산출물 4개 존재','시간·장소 충돌과 누락 표시','좁은 화면·체크박스 동작 확인','원본 보존·근거 추적 확인'])+'<p class="diagram-caption">수업용 확인표 · 체크가 실제 검증을 대신하지 않습니다.</p></div>'
 if kind=='layers':
  return '<div class="boundary"><div><b>지침</b><span>어떻게 행동할지 요청</span><div><b>권한 규칙</b><span>무엇을 허용할지 결정</span><div><b>샌드박스</b><span>명령의 접근 경계 제한</span></div></div></div></div><p class="diagram-caption">보완 관계를 나타낸 개념도 · 모든 도구에 같은 격리가 적용되지는 않음</p>'
 if kind=='curriculum':
  return bars(['AI·LLM','터미널·설치','첫 작업','검증·보안','컨텍스트','확장 기능','Agent','종합 실습'],[30,45,45,40,35,45,50,70],'분','본 수업 360분 · 강의 운영안 기준, 휴식 제외')
 if kind=='schedule':
  return bars(['탐색·계획','결과 생성','검토·동작','수정·인계'],[7,15,10,8],'분','합계 40분 · 종합 실습 권장 시간 배분')
 return ''

SPECS={
 '전체 목차와 권장 시간':('curriculum',),
 'AI와 LLM의 관계':('taxonomy',),
 'LLM은 토큰을 이어서 생성한다':('tokens',),
 '학습과 추론은 다른 단계':('compare',[('학습','데이터로 모델의 내부를 조정','모델을 만드는 단계'),('추론','지금의 문맥으로 결과를 생성','모델을 사용하는 단계')]),
 '컨텍스트는 지금 펼쳐 둔 작업 자료':('context',),
 '환각과 불확실성':('flow',['주장 발견','원문 확인','불확실성 표시'],'그럴듯함과 사실 여부는 따로 확인'),
 '검색·RAG·파일 읽기':('flow',['질문','관련 자료 검색','근거와 답변'],'검색 결과의 날짜·누락·충돌도 검토'),
 '채팅과 에이전트의 차이':('compare',[('채팅','“작성 방법을 알려줘”','답변을 읽고 사람이 실행'),('에이전트','“파일을 만들고 확인해줘”','도구로 실행하고 결과 관찰')]),
 '워크플로와 에이전트':('compare',[('워크플로','정해진 길을 따라 처리','예측 가능한 순서'),('에이전트','관찰한 결과로 다음 행동 결정','동적으로 작업 조정')]),
 'Claude와 Claude Code':('compare',[('Claude 채팅','대화·자료 분석','대화 중심 인터페이스'),('Claude Code','파일·명령·개발 도구','프로젝트 중심 인터페이스')]),
 '터미널·셸·CLI':('flow',['터미널 창','셸: 명령 해석','claude 실행'],'같은 창에서도 입력을 받는 프로그램은 달라집니다'),
 '경로와 현재 폴더':('tree',),
 '기본 명령 · macOS / Linux':('terminal',),
 '세 종류의 입력을 구별하기':('table',['입력 위치','입력 예'],[['OS 터미널','claude --version'],['Claude Code 내부','요약해줘 /help'],['파일 내용','CLAUDE.md, JSON']]),
 '설치 전 확인':('flow',['환경 확인','계정 준비','설치·실행'],'OS → 네트워크 → 로그인 가능한 계정'),
 '구독·API·사용량':('compare',[('구독','로그인한 플랜의 사용량','포함량과 한도 확인'),('API','Console의 사용량 기반 과금','실제 청구는 결제 화면 확인')]),
 '설치·로그인 문제 해결':('table',['증상','먼저 확인'],[['명령을 못 찾음','새 창 / PATH'],['403·로그인 반복','계정 / 조직 / 네트워크'],['설치 상태가 이상함','claude doctor']]),
 '실습 준비 확인':('tree',),
 '첫 대화는 탐색부터':('flow',['파일 찾기','실제 내용 읽기','충돌·누락 보고'],'먼저 이해한 뒤 결과물을 만듭니다'),
 '좋은 요청의 다섯 요소':('stepper',['목표','자료','제약','산출물','검증'],['누가 무엇을 할 수 있게 만들까요? 신입사원이 준비물을 알게 합니다.','materials/policy.md와 schedule.csv를 근거로 사용합니다.','없는 사실을 만들지 않고 원본 파일을 보존합니다.','output/checklist.md에 결과를 저장합니다.','항목마다 근거를 붙이고 원문과 대조합니다.']),
 '계획 검토의 네 가지 질문':('flow',['범위','영향','검증','가정'],'계획을 실행 전에 검토하는 관점'),
 '실습 1 · 확인 포인트':('table',['대상','자료 A','자료 B'],[['시각','09:30','10:00'],['장소','7층 교육실','2층 세미나실'],['식대','미확정','담당자 확인']]),
 '작업 루프를 읽는 법':('stepper',['자료 수집','행동','검증','수정·완료'],['규정과 FAQ를 읽고 시간·장소 충돌을 찾습니다.','output/checklist.md를 만들고 근거를 표시합니다.','원문과 대조하고 빠진 정보가 있는지 확인합니다.','문제가 있으면 수정합니다. 기준을 충족하면 결과와 남은 질문을 보고합니다.']),
 '권한 모드 선택':('table',['모드','교육에서의 의미'],[['default','변경을 직접 검토'],['acceptEdits','편집 자동 허용 확대'],['plan','먼저 분석·계획'],['auto','자동 위험 검토'],['bypassPermissions','격리된 고급 환경']]),
 '권한 요청에서 볼 내용':('flow',['대상','영향','허용 범위'],'일회 허용과 반복 허용을 구별'),
 'diff는 변경 전후의 차이':('diff',),
 '검증의 종류':('table',['검증','증거 예'],[['내용','원문·숫자 대조'],['실행','명령과 실행 결과'],['행동','클릭·예외 입력'],['회귀','기존 기능 재확인']]),
 'Git은 프로젝트의 변경 기록':('git',),
 '체크포인트와 /rewind':('compare',[('복구 범위에 포함될 수 있음','추적한 파일 편집·대화','선택한 복구 옵션 확인'),('별도 복구 필요','외부 전송·DB·배포','Git·백업·서비스별 복구')]),
 '데이터 보호와 프롬프트 인젝션':('flow',['외부 문서','내용과 지시 구별','범위 내 도구 사용'],'참고 자료가 실행 권한을 갖는 것은 아닙니다'),
 '지침·권한·샌드박스의 역할':('layers',),
 '긴 대화를 관리하는 기준':('context',),
 'CLAUDE.md는 프로젝트 안내서':('flow',['프로젝트 목적','팀의 제약','검증 방법'],'반복되는 핵심 지침만 짧게 유지'),
 '지침과 자동 메모리':('compare',[('CLAUDE.md','사람이 정하고 검토','공유하는 작업 지침'),('자동 메모리','Claude가 관찰해 기록','확인하고 정리할 학습 사항')]),
 '설정 파일의 범위':('table',['위치','범위'],[['~/.claude/settings.json','내 프로젝트 전반'],['.claude/settings.json','공유 프로젝트'],['.claude/settings.local.json','이 프로젝트의 개인 설정'],['조직 관리 설정','조직 정책 우선 적용']]),
 '모델 선택과 사용량':('flow',['작업 난도','모델·effort','결과·비용 관찰'],'대표 과제로 비교하고 사용량을 확인'),
 '확장 기능을 고르는 기준':('table',['필요한 것','선택할 기능'],[['항상 읽는 지침','CLAUDE.md'],['재사용하는 절차','Skill'],['외부 도구 연결','MCP'],['이벤트 자동 실행','Hook'],['기능 묶음 배포','Plugin']]),
 'Skill의 구조와 호출':('flow',['SKILL.md','/이름 호출','절차 실행'],'설명 → 입력 → 단계 → 결과 형식을 명확하게'),
 'MCP는 도구 연결 규약':('mcp',),
 'MCP 운영에서 생기는 문제':('flow',['설정 등록','인증 성공','도구 호출 성공'],'각 단계를 따로 확인해야 합니다'),
 'Hook은 이벤트에 반응하는 자동화':('stepper',['실행 전','도구 실행','실행 후','응답 종료'],['PreToolUse: 입력과 허용 조건을 검사하는 시점입니다.','Claude Code가 허용된 도구를 실행합니다.','PostToolUse: 성공한 도구 실행의 후처리 시점입니다.','Stop: 응답 종료 시점의 검사를 연결할 수 있습니다. 이벤트별 실패 처리를 확인하세요.']),
 'Plugins와 공유':('flow',['기능 묶음','출처·권한 검토','버전 관리'],'Skill · Hook · MCP · 서브에이전트'),
 '서브에이전트가 필요한 때':('parallel',),
 '작업자와 검토자를 분리하기':('flow',['작성자','검토자','통합자','최종 확인'],'서로 다른 역할과 같은 수용 기준'),
 '병렬 처리할 수 있는 일':('parallel',),
 'worktree로 작업 폴더 분리':('compare',[('작업 폴더 A','문서 브랜치','문서 변경을 검토'),('작업 폴더 B','화면 브랜치','HTML 변경을 검토')]),
 '자동화의 출력 계약':('flow',['결과 JSON','상태·증거 검사','후속 단계'],'실패·권한 거부·한도 초과는 중단 경로로'),
 'Agent SDK로 넘어갈 때':('flow',['CLI로 검증','SDK로 통합','운영 체계 추가'],'인증 · 격리 · 로그 · 예산 · 재시도'),
 '고급 에이전트 설계 패턴':('table',['패턴','작업 구조'],[['연쇄','단계의 출력을 다음 입력으로'],['라우팅','자료 종류별 분기'],['병렬','독립 작업 후 통합'],['평가·수정','기준 검사 후 제한적 반복']]),
 '멈출 조건과 성공 기준':('compare',[('완료','수용 기준 충족','결과와 검증 증거 보고'),('중단','정보·권한·예산 부족','미완료 이유와 다음 행동 보고')]),
 '종합 과제 · 단계별 시간':('schedule',),
 '수용 기준 · 통과 여부를 직접 확인':('checklist',),
 '동료 검토 · 10분':('flow',['위치','관찰','영향','제안'],'의견보다 확인 가능한 사실로 전달'),
 '막혔을 때의 진단 순서':('flow',['위치·파일','오류 문구','원인 분류','최소 재현'],'환경 문제와 요청 문제를 분리'),
 '실패 패턴과 수정 방법':('table',['실패 패턴','수정 방향'],[['너무 큰 요청','단계·완료 기준으로 분할'],['과도한 자료','관련 범위부터'],['근거 없는 확정','출처·불확실성 표시'],['검증 생략','실행·대조·화면 확인']]),
 '2주 도입 계획 · 제안':('flow',['1~2일 비교','3~5일 재사용','2주차 검토'],'오류·비용·수정 시간을 기록한 뒤 확대'),
 '업무 실행 전 체크리스트':('flow',['범위','권한','근거','검증','복구'],'작업을 시작하기 전과 완료하기 전에 확인'),
}

def render_visual(s, root):
 if s.get('asset'):
  a=s['asset'];path=root/'assets/references'/a['file'];mime='image/svg+xml' if path.suffix=='.svg' else 'image/png'
  data=f'data:{mime};base64,'+base64.b64encode(path.read_bytes()).decode()
  return '<figure class="reference-figure"><button class="zoom-image" aria-label="공식 도해 확대"><img src="'+data+'" alt="'+e(a['alt'])+'"></button><figcaption>원문 도해 · © Anthropic · 2026.11.03 확인 <span>클릭하여 확대 ↗</span></figcaption></figure>'
 spec=SPECS.get(s['title'])
 if not spec:return ''
 kind,*args=spec
 if kind=='flow': result=flow(*args)
 elif kind=='compare':result=compare(*args)
 elif kind=='table':result=table(*args)
 elif kind=='stepper':result=stepper(*args)
 elif kind=='tree':result=tree()
 else:result=custom(kind)
 return '<div class="visual visual-'+kind+'">'+result+'</div>'
