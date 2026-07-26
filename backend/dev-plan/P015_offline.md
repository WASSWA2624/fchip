# P015 Offline Synchronization
Deliver offline behavior with each screen that declares offline, failed-sync, or conflict states.

## Offline Candidates

CHW visits, symptoms/vitals, MCH indicators, referrals, alert follow-up drafts, school/feeder capture, field logs, batch capture, and other explicitly declared field writes may save locally and synchronize later.

## Online-Only Actions

Account authentication and session issuance, role/entitlement changes, consent withdrawal, connector scope changes, research export approval/download authorization, and other security-sensitive approvals remain online-only.

## Acceptance

- Offline-capable endpoints must expose version metadata and idempotency behavior.
- Conflict responses must be deterministic and documented for frontend consumers.
- Synchronization must enforce current authorization when changes reach the server.
- The frontend must prove pending, syncing, synced, failed, and conflict behavior before the slice closes.
- Server time, version metadata, and idempotency keys—not the client clock—control reconciliation.
