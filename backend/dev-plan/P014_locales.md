# P014 Locale Expansion
Add locales only after English behavior and core module parity are stable.

## Requirements

- The `en` catalog must remain complete and authoritative.
- A non-English locale may ship only when the active module's system messages, errors, statuses, consent/safety text, notifications, and frontend ARB copy are complete together.
- Locale completeness checks must run during release verification.
- User-entered content must remain unchanged.

## Acceptance

- Shipped locales must not omit critical workflow text.
- Consent, privacy, clinical guidance, alert, and export-sensitive copy must have owner approval before rollout.
- Fallback behavior must be deterministic and tested.
