# Licenses, terms, and attribution / 라이선스·약관·출처

Checked on 2026-10-04 against the upstream sources linked below. This is a good-faith engineering summary, not legal advice. Re-check the linked sources before you rely on them, especially for commercial use.

2026-10-04에 아래 링크된 원본 자료로 확인한 내용입니다. 법률 자문이 아닌 엔지니어링 관점의 정리이며, 특히 상업적 사용 전에는 링크된 원문을 직접 다시 확인하세요.

## 1. This kit / 이 키트

- Everything to Discord is **MIT** licensed (see [`LICENSE`](../LICENSE)).
- It contains **no code copied from** Agent Messenger, OmO, Omonya, Discord, or OpenAI. It is documentation, profile templates, schemas, and fictional examples. It links to those projects and tells your agent how to use them; it does not redistribute them.
- 이 키트는 **MIT** 라이선스입니다. Agent Messenger, OmO, Omonya, Discord, OpenAI의 코드는 복사하지 않았고, 문서·프로필 템플릿·스키마·가상 예제만 담고 있습니다. 해당 프로젝트는 링크로만 안내하며 재배포하지 않습니다.

## 2. Agent Messenger

| | |
| --- | --- |
| Project | [agent-messenger/agent-messenger](https://github.com/agent-messenger/agent-messenger) · npm [`agent-messenger`](https://www.npmjs.com/package/agent-messenger) (2.39.0 when checked) |
| Declared license | **MIT**, stated in the upstream README ("## License — MIT") |
| Caveat | When checked, the upstream repository had **no `LICENSE` file and no `license` field in `package.json`**, and GitHub reported no detected license. Treat the README statement as the declared license and confirm with the maintainers if you need certainty. |
| How this kit uses it | Your agent may **install it itself** from npm and call its CLI/SDK. Nothing is vendored here, so no upstream license text has to ship in this repository. If you copy upstream code into your own project, keep its copyright and license notice. |

**Use only the official Bot path.** Agent Messenger ships two kinds of Discord tools:

- `agent-discordbot` / `agent-messenger/discordbot` — authenticates with an **official Bot token**. **This is the only Discord path this kit allows.**
- `agent-discord` / `agent-messenger/discord` — acts **as your user account** by extracting a session token from the desktop app or browser, or by QR sign-in. That is user-account automation ("self-botting"). Discord states that [automating user accounts is not allowed](https://support.discord.com/hc/en-us/articles/115002192352-Automated-User-Accounts-Self-Bots) and that automation belongs on a bot account. It can get your account banned. **Do not use it with this kit.**

Agent Messenger 중 이 키트가 허용하는 Discord 경로는 **공식 Bot 토큰(`agent-discordbot`)뿐**입니다. 사용자 세션 토큰을 추출하는 `agent-discord`는 Discord가 금지하는 셀프봇 방식이며 계정 정지 위험이 있어 사용하지 않습니다. 설치는 에이전트가 직접 npm에서 하며, 이 저장소에는 업스트림 코드가 들어 있지 않습니다. 업스트림에 LICENSE 파일이 없다는 점(README에는 MIT 명시)은 위 표의 주의 사항을 보세요.

## 3. Discord

- You must create the application and Bot yourself in the Discord Developer Portal, and approve the OAuth invite yourself. The agent never creates, approves, or scrapes these.
- Follow the [Discord Terms of Service](https://discord.com/terms) (which prohibit scraping or automating the service without consent) and the [Discord Developer Policy](https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy) (for example, do not modify a user's account without their explicit permission).
- Keep the Bot owner-only by default, request the minimum permissions and intents, and never place the Bot token in a repository, prompt, screenshot, or log.
- Discord 개발자 포털에서 애플리케이션·Bot 생성과 OAuth 초대 승인은 사용자가 직접 합니다. 위 이용약관과 개발자 정책을 따르고, 기본은 소유자 전용·최소 권한이며 Bot 토큰은 저장소·프롬프트·스크린샷·로그에 넣지 않습니다.

## 4. Dot (ChatGPT)

- Dot is used through **your own signed-in session** in a browser lane on your own machine. The kit never reads cookies, profiles, or tokens, and raw CDP stays loopback-only.
- That is not an official public API. OpenAI's Terms of Use apply to your account, and automating the web UI may be restricted or may break without notice. We could not retrieve OpenAI's terms automatically when writing this page, so **read the current [OpenAI Terms of Use](https://openai.com/policies/terms-of-use/) yourself** and use this only for your own personal workflow.
- Do not assign tasks that consume other usage limits you did not intend to spend, and do not share your session with other people.
- Dot은 사용자 본인의 로그인 세션을 자기 PC의 브라우저 레인에서 쓰는 방식입니다. 공식 공개 API가 아니므로 OpenAI 이용약관을 직접 확인하고, 본인 개인 워크플로에만 사용하세요(이 문서 작성 시 약관 원문을 자동으로 가져오지 못해 미검증입니다).

## 5. OmO (oh-my-openagent)

- OmO is the agent harness this kit is designed to be run with: [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent). You give your OmO agent this repository's URL and `SETUP_PROMPT.md`.
- OmO is **not MIT**. Its `LICENSE.md` is the **Sustainable Use License 1.0**: use and modify it only for your own internal business purposes or for non-commercial or personal use; distribute it only free of charge for non-commercial purposes; keep all licensing and copyright notices; include a copy of the terms with any copy you give others; and mark modified copies with a prominent modification notice. Third-party components keep their own licenses.
- This kit includes no OmO code, so its MIT license is unaffected. If you build commercial or redistributed products on OmO itself, read its license first. Do not imply that this kit is made, endorsed, or supported by the OmO authors.
- 이 키트는 OmO 에이전트에 저장소 URL과 `SETUP_PROMPT.md`를 주고 실행시키는 용도로 만들었습니다. OmO는 MIT가 아니라 **Sustainable Use License 1.0**(개인·내부 업무·비상업 사용, 재배포는 무료·비상업만, 고지 유지, 수정 시 수정 표시)이므로 OmO 자체를 상업적으로 쓰거나 재배포한다면 라이선스를 먼저 읽으세요. 이 키트에는 OmO 코드가 없고, OmO 제작자의 공식 제품이라는 암시도 하지 않습니다.

## 6. Omonya

Omonya is the author's private personal assistant and is **not included or licensed here**. [`omonya-upgrade.md`](omonya-upgrade.md) is documentation only. The `omonya-hybrid` profile is for people who already run Omonya; everyone else should ignore it.

Omonya는 작성자의 비공개 개인 비서로 이 저장소에 포함되지 않으며 라이선스도 부여하지 않습니다. 관련 문서는 연동 가이드일 뿐이고, `omonya-hybrid` 프로필은 이미 Omonya를 쓰는 사람만 해당됩니다.

## 7. Quick checklist for your agent / 에이전트용 체크리스트

1. Discord = official Bot token only. Never a user token, QR sign-in, or session extraction.
2. Install Agent Messenger from npm yourself; do not copy its source into this repository.
3. Tell the user the OmO license limits (non-commercial/internal) if OmO is the harness.
4. Tell the user to read the Discord and OpenAI terms and approve each human step.
5. Do not ship secrets, real IDs, private captures, or third-party code in any published fork.
