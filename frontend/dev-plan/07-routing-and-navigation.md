# 07 - Routing and Navigation
Create centralized, guard-ready routes with readable URLs and persistent navigation.

## Applicable Rules
You must follow [`00-execution-policy.md`](./00-execution-policy.md), [`navigation.mdc`](../.cursor/navigation.mdc), [`authentication_session.mdc`](../.cursor/authentication_session.mdc), [`permissions.mdc`](../.cursor/permissions.mdc), and [`layouts.mdc`](../.cursor/layouts.mdc).

## Implementation
1. Create `app_routes.dart` for route names and paths.
2. Configure `go_router` in `app_router.dart`.
3. Register route metadata from `app-ui/**/screen.json`, including parent route, role, tabs, primary action, and declared shell.
4. Add the shared entry routes, each role home, access-denied, and localized not-found routes exactly as described by `app-flows/07-navigation.md`.
5. Add session, RBAC, ABAC, subscription, and assigned-module guards with fixture policy data; wire real policy responses in the relevant product slice.
6. Use shared shell routes: mobile bottom navigation, tablet compact rail, and desktop side navigation.
7. Pages must not contain raw route strings.

## Acceptance Criteria
- Web URLs must be readable.
- Unknown routes must show localized not-found UI.
- Protected routing must be enableable without restructuring routes.
- Central configuration, route helpers, guards, and the responsive shell must work together.
- Every catalogued route is either registered behind its phase/feature gate or documented as intentionally deferred.
