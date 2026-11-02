# 외부 시각 자료 출처

확인 및 다운로드: 2026-11-03. 아래 네 도해는 Anthropic 공식 자료에서 교육적 해설을 위해 발췌했다. 이미지의 권리는 원저작자 Anthropic에 있으며 이 저장소의 자체 코드와 구분된다. 원본 비율과 내용을 유지하고, 한국어 해설은 이미지 밖에 별도로 작성했다.

HTML에 이미지를 포함하여 오프라인에서도 볼 수 있다. 출처 링크는 각 슬라이드 아래에 표시한다.

## 공식 도해 · 도구가 연결된 LLM

- 작성자: Anthropic
- 저장 파일: `assets/references/augmented-llm.png`
- [원문 페이지](https://www.anthropic.com/research/building-effective-agents)
- [원본 이미지](https://www-cdn.anthropic.com/images/4zrzovbb/website/d3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png)
- 대체 텍스트: 입력과 출력 사이의 LLM에 검색, 도구, 메모리가 양방향으로 연결된 Anthropic 공식 도해

## 공식 도해 · 에이전트의 작업 루프

- 작성자: Anthropic
- 저장 파일: `assets/references/agentic-loop.svg`
- [원문 페이지](https://code.claude.com/docs/en/how-claude-code-works)
- [원본 이미지](https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/agentic-loop.svg)
- 대체 텍스트: 프롬프트 다음에 문맥 수집, 행동, 결과 검증이 반복되며 사용자가 언제든 방향을 조정하는 공식 작업 루프

## 공식 도해 · 위임과 팀 협업

- 작성자: Anthropic
- 저장 파일: `assets/references/agent-teams.png`
- [원문 페이지](https://code.claude.com/docs/en/agent-teams)
- [원본 이미지](https://mintcdn.com/claude-code/nsvRFSDNfpSU5nT7/images/subagents-vs-agent-teams-light.png)
- 대체 텍스트: 왼쪽은 주 에이전트에 결과를 보고하는 서브에이전트, 오른쪽은 공유 작업 목록과 동료 간 통신을 사용하는 Agent teams

## 공식 도해 · 단계 사이의 검증

- 작성자: Anthropic
- 저장 파일: `assets/references/prompt-chaining.png`
- [원문 페이지](https://www.anthropic.com/research/building-effective-agents)
- [원본 이미지](https://www-cdn.anthropic.com/images/4zrzovbb/website/7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png)
- 대체 텍스트: LLM 호출 1의 출력이 Gate를 통과하면 호출 2와 3으로 이어지고 실패하면 종료하는 프롬프트 연쇄 도해

## 자체 작성 도식과 그래프

HTML 도형·비교표·흐름도는 본 교육용으로 작성했다. MCP 구조는 [MCP 공식 아키텍처](https://modelcontextprotocol.io/docs/learn/architecture)를 참고했다.

- 시간 배분 그래프: outline.md의 교육 운영안, 총 360분과 종합 실습 40분. 제품 성능 자료가 아니다.
- 컨텍스트 그래프: 설명용 100칸 모형. 실제 토큰 수나 특정 모델 한도가 아니다.
- 토큰 생성: 개념 시연용 조각. 실제 토크나이저 출력이 아니다.
- 터미널·diff·체크리스트: 가상 온보딩 자료에 기반한 브라우저 내 시연. 실제 시스템에 명령을 실행하지 않는다.
