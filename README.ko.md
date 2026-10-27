# AI Prompt Optimizer · 한국어

[English](README.md) · [简体中文](README.zh-CN.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

**v2.5.0 · MIT · ko**

**원래 의도를 유지하면서 모호한 요청을 명확하고 실행 가능한 AI 지시로 바꿉니다.**

개발, 디자인, 글쓰기, 조사, 이미지·영상 요청에 사용할 수 있습니다. 숫자, 제약, 변수를 보존하고 사실과 가정을 구분합니다. 원래 작업은 명시적으로 요청한 경우에만 실행합니다.

**Install, update and verify / 安装、更新与验证:** [English](docs/INSTALL.md) · [简体中文](docs/INSTALL.zh-CN.md) · [Candidate evidence / 候选验证](evals/v2.5.0/revision-20261027/README.md)

## 설치

프로젝트 전체를 내려받아 압축을 풀고 폴더 이름을 ai-prompt-optimizer로 바꿉니다. 아래 스킬 경로 중 한 곳에 넣고 SKILL.md가 바로 안에 있는지 확인한 다음 새 대화를 시작하세요.

```text
~/.agents/skills/ai-prompt-optimizer/
<project>/.agents/skills/ai-prompt-optimizer/
%USERPROFILE%\.agents\skills\ai-prompt-optimizer\
```

## 세 가지 사용 방식

- 최적화만: 복사해 쓸 지시문을 만들며 그 안의 작업은 실행하지 않습니다.
- 정리 후 실행: 꼭 필요한 내용만 확인한 뒤 허용된 작업을 수행합니다.
- 검토: 중요한 충돌이나 누락을 찾아 필요한 부분만 수정합니다.

## 예시

```text
$ai-prompt-optimizer 지시문만 개선하고 실행하지 마세요: 보고서를 더 전문적으로 작성하되 모든 사실과 숫자를 유지하고 자료에 근거하지 않은 결론은 추가하지 마세요. 한국어로 출력하세요.
```

[사용 안내](docs/USER_GUIDE.ko.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

## 범위와 검증

이 페이지는 AI가 작성한 현지화 입문 문서로, 원어민의 전문 교정을 받지 않았습니다. 결과는 모델과 클라이언트에 따라 달라집니다. 30개 언어 항목은 모든 모델에서 검증했다는 뜻이 아닙니다. 상세 유지보수·조사 문서는 주로 영어와 중국어 간체로 제공됩니다.

[MIT](LICENSE)
