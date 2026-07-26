# P008 Performance
Keep field, sync, worklist, map, alert, dashboard, and export operations responsive under realistic load.

## Requirements

- Queries must use pagination, appropriate indexes, and reviewed query shapes.
- Expensive exports, reporting, and reconciliation should run outside request threads.
- Add readiness and performance checks for hot endpoints.
- N+1 queries and unnecessary payload fields must be removed.

## Acceptance

- User-critical reads, field saves, sync, and actions must have measurable performance budgets.
- Readiness checks must reflect actual dependencies and bottlenecks.
- Performance regressions must be resolved before release.
