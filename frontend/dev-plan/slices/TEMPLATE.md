# Slice record template

Copy this block into [`tracker.md`](./tracker.md) for each chronology screen. Do not close a screen with unfilled sections; write `n/a` with a reason instead of leaving a blank.

```markdown
### S-NNN · VS-NN · <module>/<screen>

- **Chronology:** `S-NNN` (from `chronology.yaml`)
- **Route:** `/…` (matches `screen.json`)
- **Phase:** shared | mvp | phase-2 | phase-3 | phase-4
- **Status:** not-started | ui-fixtures | contract-defined | backend-in-progress | wired | done
- **Roles / ABAC scope:** …
- **Supported states:** default, loading, empty, error, forbidden, offline, conflict (as declared)

**Frontend**

- Files: `lib/features/…`
- Repository methods: …
- Tests: unit, widget, golden …
- Localization prefix: `<module>.<screen>`

**Backend pairing** (`none` allowed only for a proven static screen)

- Module(s): `backend/src/modules/…`
- Prisma models + migration: …
- Endpoints: `GET /api/v1/…`, `POST /api/v1/…/<action>`
- Permissions / entitlement gate: …
- Consent + audit: …
- Offline: idempotency key, version field, conflict rule …
- Realtime events: … (omit when the UI needs no live update)
- Seeds: … (must reproduce every declared state)
- Tests: schema, access, service, route, contract, workflow …

**Cross-stack proof**

- Journey exercised: …
- Evidence: test name, command, or run output …

**Notes / deviations:** …
```

## Filling rules

1. Fill **Route**, **Roles**, and **Supported states** from `app-ui/<module>/<screen>/screen.json` — never from memory.
2. Fill **Frontend** while the UI still runs on fixtures.
3. Fill **Backend pairing** in the same atomic unit, before status can pass `contract-defined`.
4. Status reaches `done` only after **Cross-stack proof** names a passing test or command.
5. Update the matching row in `chronology.yaml` (`status` + `backend`) when the screen moves.
6. If a reference conflicts with another, record the decision under **Notes / deviations**.
