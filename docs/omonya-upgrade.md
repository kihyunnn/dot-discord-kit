# Omonya integration notes / Omonya 연동 메모

This is a documentation-only integration guide. It does not change private Omonya code.

이 문서는 private Omonya 코드를 변경하지 않는 문서용 연동 가이드입니다.

```text
#dot parent channel -> Omonya
#dot child threads -> Dot bridge
```

Use one owner for each guild/parent/thread tree. Retire the legacy relay before enabling another bridge. Apply an author allowlist before Dot/CDP/DevSpace handoff. Choose exactly one result writer: `dot_devspace` or `bridge_discord`.

부모 `#dot` 채널은 Omonya가 소유하고 자식 스레드만 Dot bridge가 소유합니다. 기존 relay를 먼저 마이그레이션하고, 작성자 allowlist와 결과 writer를 하나만 설정합니다.
