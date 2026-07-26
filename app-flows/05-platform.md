# 05 — Platform connections

How frontend workspaces sit on backend domains and shared glue.

## Frontend ↔ backend

```mermaid
flowchart TB
  subgraph fe [Flutter]
    UI[Workspace page]
    CTRL[Riverpod controllers]
    REPO[Repositories / DTOs]
    CORE[core: session · permissions · realtime · sync · network]
    SHARED[shared: shell · dialogs · workflow registry]
  end

  subgraph be [Express]
    RT[Routes /api/v1/…]
    SVC[Services · flow engines]
    PRISMA[Prisma]
  end

  UI --> CTRL --> REPO --> RT
  UI --> SHARED
  CTRL --> CORE
  RT --> SVC --> PRISMA
  CORE <-->|WebSocket /ws| be
```

## Backend domain map (grouped)

```mermaid
flowchart TB
  subgraph access [Access & place]
    auth
    tenant
    facility
    user
    role
    permission
    abac
  end

  subgraph patient [Patient]
    patient
    appointment
    visit_queue
    encounter
  end

  subgraph flows [Flow engines]
    opd_flow
    ipd_flow
    theatre_flow
    therapy_flow
    triage
    emergency_case
  end

  subgraph dx [Diagnostics & pharmacy]
    lab_workspace
    radiology_workspace
    pharmacy_workspace
  end

  subgraph money [Revenue]
    billing
    claims_workspace
    subscriptions_workspace
  end

  access --> patient --> flows
  flows --> dx
  flows --> money
```

Many smaller CRUD modules hang under these hubs (notes, vitals, orders, invoices, HR, housekeeping, etc.). Full list: `backend/src/modules/` (mounted in `backend/src/app/router.js`).

## Shared glue (always between modules)

```mermaid
flowchart LR
  subgraph core [lib/core]
    SEC[security / session]
    PERM[permissions]
    RT[realtime / WebSocket]
    SYNC[sync + storage]
    NET[network / connectivity]
    SUB[subscriptions]
  end

  subgraph shared [lib/shared]
    SHELL[ResponsiveAppShell]
    WSUI[AppWorkspace layouts]
    DLG[Cross-module clinical dialogs]
    WF[workflow_action_registry]
  end

  SEC --> SHELL
  PERM --> SHELL
  RT --> WSUI
  SYNC --> WSUI
  WF --> DLG
  DLG --> FEAT[Feature workspaces]
  SHELL --> FEAT
```

| Concern | What it does for every workspace |
| --- | --- |
| **Session** | Tokens, restore, logout |
| **Permissions** | Hide/disable routes and actions |
| **Realtime** | Live list/detail refresh over `/ws` |
| **Offline** | Queue / ETag / idempotency patterns |
| **Workflow registry** | Open the right dialog/route from another desk |
| **Badges** | Sidebar workload counts |

## Adding a new piece (adapt)

```mermaid
flowchart TD
  A[New workspace] --> B[Feature folder under lib/features]
  B --> C[Page + route in app_routes / app_router]
  C --> D[AccessRequirement · roles · modules]
  D --> E[Sidebar group in _localizedShellDestinations]
  E --> F[Backend module + Prisma if new domain]
  F --> G[Wire neighbours in care spine]
```

Keep the **care spine** stable: patient → queue/encounter → orders → discharge → billing.

← [04 Workspaces](04-workspaces.md) · [Index](README.md)
