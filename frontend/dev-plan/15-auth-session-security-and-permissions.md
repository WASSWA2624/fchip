# 15 - Auth, Session, Security, and Permissions
Prepare secure session and access controls for the shared FCHIP entry flow.

## Applicable Rules
You must follow [`00-execution-policy.md`](./00-execution-policy.md), [`authentication_session.mdc`](../.cursor/authentication_session.mdc), [`security.mdc`](../.cursor/security.mdc), [`permissions.mdc`](../.cursor/permissions.mdc), [`navigation.mdc`](../.cursor/navigation.mdc), and [`storage_strategy.mdc`](../.cursor/storage_strategy.mdc).

## Implementation
1. Define unknown, unauthenticated, authenticated, expired, and forbidden session states.
2. Create a provider-neutral auth repository contract.
3. When tokens are used, create secure session storage.
4. Connect route guards to session state.
5. Add centralized permission types and helpers.
6. Logout must clear sensitive local session data.
7. Use `app-ui/00-shared` entry and access screen contracts; implement their real backend behavior during Wave 0 of step `24`.

## Acceptance Criteria
- Enabled protected routes must block users without a valid session.
- Token values must never be logged.
- Permission checks must be centralized.
- Auth/session contracts, a session provider, permission helpers, and a guarded route example must exist.
- Offline PIN must unlock only saved device work and must never act as account authentication.
