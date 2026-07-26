# 13 - API and Repository Readiness
Prepare the reusable network boundary; each product slice must then implement and connect its real backend contract.

## Applicable Rules
You must follow [`00-execution-policy.md`](./00-execution-policy.md), [`network_api.mdc`](../.cursor/network_api.mdc), [`repository-pattern-example.mdc`](../.cursor/reference/repository-pattern-example.mdc), [`architecture.mdc`](../.cursor/architecture.mdc), [`error_handling.mdc`](../.cursor/error_handling.mdc), and [`environment_configuration.mdc`](../.cursor/environment_configuration.mdc).

## Implementation
1. Create an API client abstraction under `lib/core/network/`.
2. Add an HTTP package only when implementing a real client.
3. Put repository contracts in feature domain layers and implementations in data layers.
4. Use fake or in-memory implementations only while building the UI-first half of an active slice.
5. Network errors must map to typed failures.
6. Derive each product contract from the implemented screen and user action using the derivation table in [`25-slice-execution-playbook.md`](./25-slice-execution-playbook.md); implement its backend before closing that slice.
7. Keep fixture and backend response shapes contract-tested so switching repositories does not change presentation behavior.
8. Treat every fake repository as temporary. Delete it when the real one lands, unless a test still overrides it.

## Acceptance Criteria
- The shared foundation and widget tests must run without a live backend.
- Widgets must not call API clients directly.
- Repositories must be override-friendly in tests.
- API contracts, a repository example, a starter fake, and failure mapping must be available.
- Completed product slices must use the real backend outside test/demo fixture modes.
