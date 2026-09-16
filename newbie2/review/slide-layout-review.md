# THE SPEED 슬라이드 검토

2026-09-16. 19장 모두 사건명·사실 설명 중심으로 수정. 제목과 본문에서 발표자의 결론·해석을 제거했다.

[전체 미리보기](slide-overview.png)

| 페이지 | 변경 사항 |
| --- | --- |
| 01 | 챕터명만 표시. 표지에서는 진행 막대도 숨김. |
| 02 | 작은 8칸 연표를 4열 × 2행으로 확대. |
| 03 | 대국 사진 확대, 참가자·전적·일자만 표시. |
| 04 | 퀴즈쇼 사진 확대, 참가자와 진행 방식 표시. |
| 05 | 이세돌 대국 사진 확대, 5국 전적과 일자 표시. |
| 06 | 흑 37수 표시 화면과 실제 착수 중계 캡처를 나란히 배치. |
| 07 | 잘못 들어간 37수 이미지를 백 78수 기보로 교체. 실제 착수 중계 화면 추가. |
| 08 | 동일 너비 3열: 체스 사진·Webb 우주 사진·바둑 사진. 숫자와 설명의 기준선을 통일. |
| 09 | Lee: Google 공식 대국 사진. Master: DeepMind 공식 커제 행사 사진. Zero: DeepMind 공식 Elo 그래프. 날짜·전적·학습 방식 정렬. |
| 10 | 기사 제목 재구성임을 명시. 영어·수학 점수만 크게 표시. |
| 11 | 중복 점수와 장식 박스 제거. 국어·영어·수학을 동일 순서로 정렬. 서로 다른 실험임을 명시. |
| 12 | 작품을 크게 배치하고 작가·행사·수상 기록 표시. |
| 13 | 공개 화면의 읽기 면적 확보. 서비스 공개일과 기능 표시. |
| 14 | 이미지 프레임의 흰 여백 제거. 입력 종류를 간결하게 정렬. |
| 15 | 시험별 결과와 평가 대상을 분리. 사진이 시험 현장 사진이 아님을 명시. |
| 16 | 확인되지 않은 연도 비교와 평가 문구 제거. 영상 소재 설명으로 변경. |
| 17 | 긴 세로 프레임을 가로 이미지에 맞게 조정. 세 서비스의 이름·연도·기능 정렬. |
| 18 | 은·금메달 수준과 점수를 크게 정렬. 결론 대신 모델·평가 기록 표시. |
| 19 | 발전 속도에 대한 결론을 제거하고 사건 목록으로 변경. |

## 이미지 출처

새 이미지 10개를 로컬에 저장했고 모든 이미지에 대체 텍스트를 추가했다. 원본 비율을 유지하며 다운로드한 이미지 자체를 가공하지 않았다. 전체 이력은 [sources.json](../assets/images/sources.json)에 있다.

- 37수 표시: [중앙일보 기사](https://v.daum.net/v/20260312000506849)
- 37·78수 착수 화면: [Go Magic — AlphaGo 역사](https://gomagic.org/the-story-of-alphago-how-ai-conquered-the-hardest-board-game/), AlphaGo Documentary 중계 캡처
- 78수 기보: [Axd / Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lee-sedol-alphago-divine-move.jpg), CC BY-SA 4.0
- 체스: [Bubba73 / Jud McCranie](https://commons.wikimedia.org/wiki/File:ChessStartingPosition.jpg), CC BY-SA 3.0
- 우주: [NASA — Webb’s First Deep Field](https://science.nasa.gov/asset/webb/webbs-first-deep-field-unveiled-nircam-image/), NASA / ESA / CSA / STScI
- 바둑: [Donarreiskoffer](https://commons.wikimedia.org/wiki/File:Go_board.jpg), CC BY-SA 3.0
- Lee: [Google — AlphaGo’s ultimate challenge](https://blog.google/innovation-and-ai/products/alphagos-ultimate-challenge/)
- Master: [DeepMind — AlphaGo’s next move](https://deepmind.google/blog/alphagos-next-move/)
- Zero: [DeepMind — AlphaGo Zero: Starting from scratch](https://deepmind.google/blog/alphago-zero-starting-from-scratch/)

## 검증

- 로컬 Chrome으로 19장 전체를 렌더링하고 스크린샷 검토.
- 1920×1080, 1600×900, 1440×900, 1280×720, 1024×768, 390×844에서 총 114개 페이지 상태 검사: 화면 밖 넘침·텍스트 잘림 없음.
- 21개 이미지 요소 로딩 성공. 외부 네트워크 요청 0건. JavaScript 오류 0건.
- 방향키·Space·Home·End 및 첫 장/마지막 장 경계 동작 확인.
- 작은 세로 화면에서는 16:9 발표 화면 전체를 축소 표시하므로 글자가 작다. 발표용 가로 화면을 기준으로 설계.

## 별도 콘텐츠 검토 사항

- 11페이지의 95 / 92 / 82–96점은 기존 자료를 유지했다. 개별 보도 링크, 모델, 시험 연도, 풀이 조건을 대조하기 전에는 동일 조건의 전후 비교로 설명할 수 없다.
- 16페이지의 비교 이미지는 사용자 지정 YouTube 영상으로 교체했다. 영상 제목 외에 제작 모델·연도에 대한 추가 주장은 넣지 않았다.
- 8페이지의 규모 수치는 기존 근삿값을 유지하되 체스의 “게임 트리/포지션” 혼합 표기를 “포지션”으로 정리했다. 엄밀한 수치 설명에는 계산 정의에 맞춘 출처 확인이 필요하다.
- 이번 작업은 레이아웃·이미지 적합성·사건 중심 문구에 대한 검토이며 나머지 모든 통계와 연혁을 새로 검증한 작업은 아니다.


## 2026-09-16 추가 작업: 영상 재생 및 20·21페이지

- 16·17페이지: 사용자 지정 YouTube iframe. 직접 파일 열기(`file://`)에서 오류 153을 재현했고 HTTP로 열었을 때 해결됨을 확인했다. `슬라이드 열기.command`는 localhost 서버를 실행하고 브라우저를 연다. 실행 터미널을 유지하고 종료할 때 Ctrl+C를 누른다. Python 3 필요.
- 직접 파일을 열면 영상 영역에 실행 안내와 로컬 웹 주소를 표시한다. YouTube 원본 링크도 유지한다.
- 실제 재생 검증: 16페이지 currentTime 3.59초 / 17페이지 4.40초, 모두 paused=false / readyState=4. 다음 페이지 이동 후 비활성 iframe src 제거 확인.
- 20페이지: Higgsfield 공식 Cinema Studio 4.0 장르 예시 6편(Epic, Drama, Noir, Comedy, Action, General)을 3열×2행으로 배치. 첫 5–6초, 480×270, 12fps, 무음 반복 GIF로 로컬 저장. 공식 페이지의 현재 예시를 2026.09.16에 수집한 것이며 개별 업로드일은 단정하지 않는다. [GIF 출처](../assets/gifs/sources.json).
- 21페이지: GPT 계열 11개, Opus 계열 8개의 출시 월. 동일한 2022.09–2026.09 시간축으로 표시. 모델명 클릭 시 공식 출처로 이동. 세부 파생 모델을 제외한 선별 연표이며, GPT-3.5는 ChatGPT 출시 월을 사용한다. API·ChatGPT 배포일이 하루 다른 사례는 월 단위로 표시한다. [그래프 데이터와 출처](../assets/data/model-releases.json).
- GIF 6개 프레임 수 61–72개 확인. 이미지·GIF는 로컬, YouTube 영상은 인터넷 연결 필요.

현재 자료는 21장이다. 위의 19장/114개 상태 검증은 이전 버전의 기록이다.

최종 검증: 21장 × 화면 크기 6종 = 126개 상태에서 화면 밖 넘침·텍스트 잘림 0건, JavaScript 오류 0건. 첫 장/마지막 장 경계와 페이지 번호 21장 반영 확인. 20·21페이지 전체 크기 화면을 직접 확인했다.

페이지 순서 변경: Higgsfield 영상 사례(기존 20페이지)를 18페이지로 이동. IMO는 19페이지, 사건 목록은 20페이지, 모델 출시 연표는 21페이지. 위 기록의 페이지 번호는 각 작업 당시 기준이다.

## 2026-09-16 THE QUESTION 추가

현재 총 29장. 22페이지 챕터 표지와 23–29페이지 사건 7장. 새 챕터에도 표지 진행 막대 숨김 적용. [출처와 사실 검토](question-source-review.md), [8장 미리보기](question-overview.png). 29장 × 6개 화면 크기에서 넘침 0건, JS 오류 0건.

## THE ENGINEER / THE CHOICE 추가

현재 총 41장. THE ENGINEER 30–37페이지, THE CHOICE 38–41페이지. 직업·업무 자료, 개발 도구, NASA 시험, BEFORE / AFTER 비교, 성찰 질문 구성. [구성과 출처](engineer-choice-notes.md), [미리보기](engineer-choice-overview.png), [검증 결과](engineer-choice-layout-check.json).


## 2026-09-16 · newbie 자료 반영 / 53장

THE ENGINEER 7장, THE CHOICE 5장 추가. 역사 사진 2개, 연구 원본 도표 3개, 사고 사진 1개를 로컬 참조. 기존 1–29장 보존. 53장 × 6 뷰포트 경계 검사 통과, JavaScript 오류 0. 이미지·페이지 이동 확인. 최신 렌더: engineer-choice-overview.png, slide-30.png–slide-53.png.


## 21페이지 성능 향상 주기 추가 · 2026-09-17

출시 연표 하단에 METR의 50% task-completion time horizon 배증 주기를 추가. 2026-01-29 Time Horizon 1.1 기준 장기 혼합 추세 196.5일(약 7개월), 2023년 이후 TH1.1 구간 130.8일(약 4.3개월). 평가 과제는 소프트웨어·추론 중심이며 ‘시간’은 사람이 과제를 수행할 시간이다. AI가 연속으로 동작하는 시간이 아니다. 모델 성능 전체·정확도·생산성·출시 간격이 2배가 된다는 뜻이 아니다. 기존 출시 모델 전체를 대상으로 계산한 배증 주기도 아니다.

발표 예시: “출시 간격과 별개로, 수행할 수 있는 과제가 얼마나 길어졌는지도 측정합니다. METR의 이 지표에서는 과제 길이가 장기적으로 약 7개월, 2023년 이후 구간에서는 약 4.3개월마다 두 배가 되는 추세를 보였습니다.”

과제 구성·회귀 구간·평가 환경에 따라 추정값이 달라지며 향후 고정 주기를 보장하지 않는다. 2026-03-20 METR은 평가 포화에 따라 모델링 선택에 대한 민감성이 커짐을 설명했으므로 최신 모델에 대한 무제한 외삽은 하지 않는다.
출처: https://metr.org/blog/2026-1-29-time-horizon-1-1/ 및 https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/


21페이지 추가 갱신: METR 2026년 5월 Frontier Risk Report 135쪽의 공개 모델 추세 배증 105일(약 3.5개월)을 함께 표시. 2024-01-01 이후 모델을 대상으로 2026년 2–3월 평가 보고서에서 사용한 추세이며 2025년 단독·2026년 단독 수치가 아니다. 7개월·4.3개월은 1월 발표, 3.5개월은 5월 발표로 구분했다. 자료·방법과 구간이 다른 추정값으로, 이 세 숫자만으로 가속의 인과적 증거라 단정하지 않는다.
