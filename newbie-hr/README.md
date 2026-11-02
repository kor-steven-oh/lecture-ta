# Claude Code 교육용 HTML 슬라이드 덱

`index.html`을 브라우저로 열면 시작합니다. 별도 설치·서버·CDN 없이 슬라이드를 볼 수 있습니다. Claude Code 실습에는 인터넷과 사용 가능한 계정이 필요합니다.

총 113장: 57장의 설명 도식·비교표·그래프, 공식 원문 도해 4장, 클릭으로 조작하는 학습 예제를 포함합니다. 외부 원문 이미지의 출처는 `MEDIA_CREDITS.md`에 정리했습니다.

## 조작

- ← / → / Space: 이동, Home / End: 처음·끝
- T: 목차·전체 내용 검색, Esc: 목차 닫기
- N: 강사 노트 (현재 화면에 표시되므로 청중에게도 보임)
- F: 전체 화면, P: 인쇄 또는 PDF 저장
- 코드 블록의 복사 버튼, 퀴즈의 정답 확인 버튼
- 토큰 생성·컨텍스트 슬라이더·폴더 이동·diff·검증 체크리스트 조작
- 공식 참고 이미지 클릭: 확대, Esc: 닫기
- 슬라이드 진입 모션, OS의 동작 줄이기 설정 지원
- `index.html#25`처럼 슬라이드 번호로 직접 열기

인쇄는 모든 슬라이드를 포함합니다. 강사 노트를 켜고 인쇄하면 노트도 포함됩니다. PDF 저장 시 브라우저의 머리글·바닥글은 끄는 것을 권장합니다. 노트 포함 인쇄는 긴 페이지가 생길 수 있습니다.

## 교육 자료

- `outline.md`: 먼저 확정한 목차와 시간 배분
- `content-plan.md`: 슬라이드별 내용·예제·강사 노트·출처
- `sources.md`: 공식 자료 목록 (2026-11-02 확인)
- `workshop/`: 가상 실습 자료와 결과 폴더
- `examples/`: 검토 후 복사하는 Skill·서브에이전트·Hook 설정
- `slides.json`: 슬라이드 내용의 생성 결과
- `scripts/build_deck.py`: 내용과 HTML을 생성하는 원본 (Python 표준 라이브러리만 사용)
- `scripts/visuals.py`: 도식·그래프·이미지 구성
- `assets/visuals.css`, `assets/visuals.js`: 시각 디자인·조작 예제
- `assets/references/`, `MEDIA_CREDITS.md`: 공식 도해 원본과 출처

내용을 수정하려면 `scripts/build_deck.py`를 편집한 뒤 `python3 scripts/build_deck.py`를 실행합니다. `slides.json`과 `content-plan.md`, `index.html`은 다시 생성됩니다.

수업은 360분 + 휴식 30분을 권장합니다. OS별 설치는 두 환경을 모두 수행하는 대신 자신의 환경에 맞는 쪽을 선택합니다. 가격·모델·기능·계정 정책은 바뀔 수 있으므로 강의 직전 공식 문서와 `claude --help`, 내부 `/` 메뉴를 다시 확인하세요.

## 재생성과 검증

```sh
python3 scripts/build_deck.py
npm ci
npx playwright install chromium
npm test
python3 scripts/package_deck.py
```

`npm test`는 전체 슬라이드의 화면 넘침, 이미지 로딩, 검색·이동·노트, 조작 예제, 확대 대화상자, 복사, 오프라인 실행을 확인합니다. 브라우저 경로는 `CHROME_PATH`로 지정할 수 있습니다. macOS에 Google Chrome이 있으면 자동 사용합니다. QA 결과와 PDF는 `.qa/`에 저장되며 Git에서 제외됩니다. 프레젠테이션을 보는 데 npm은 필요하지 않습니다.
