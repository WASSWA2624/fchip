# P002 Prisma Foundation
Create a stable database layer for all later domain phases.

## Runtime and Schema

- Configure the Prisma client, adapter, connection lifecycle, and ordered migration workflow.
- Models, tables, columns, migrations, and documentation must use lowercase `snake_case`.
- Add tenancy, access, audit, entitlement, and baseline operational schema support.
- Later domain models should inherit indexes, audit/version fields, the approved soft-delete strategy, `tenant_id`, and only the applicable catchment, facility, programme, feeder, geography, or ownership scope.

## Acceptance

- Migrations must run cleanly in order.
- Repository code must rely on stable tenancy and audit fields.
- Prisma, SQL, and documentation must not diverge in naming.
