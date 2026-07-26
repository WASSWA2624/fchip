# 02 — Cascade (field context)

SoT: §2. FCHIP digitises and amplifies this — it does not replace it.

## Core cascade (do not reorder)

```mermaid
flowchart TB
  L1[1. Community members]
  L2[2. CHWs / VHTs — The Bridge]
  L3[3. Outreach programmes]
  L4[4. Facilities — clinics & hospitals]
  L5[5. Research · partners · skills]
  L6[6. Empowerment · CHIS where used]
  FB[Data & Feedback — FCHIP]

  L1 --> L2 --> L3 --> L4 --> L5 --> L6
  L6 -.-> FB
  FB -.-> L1
```

## Proposed FCHIP role per layer

```mermaid
flowchart LR
  subgraph cascade [Cascade]
    L1[Communities]
    L2[CHWs]
    L3[Outreach]
    L4[Facilities]
    L5[Research]
    L6[Empowerment]
  end

  subgraph app [Proposed FCHIP pieces]
    A1[Household / needs capture]
    A2[Offline mobile · worklists · alerts]
    A3[Programme planning · metrics]
    A4[Facility dashboard · EMR ingest APIs]
    A5[Partner reporting · anonymised evidence]
    A6[Optional CHIS / IGA indicators]
    A7[GIS · climate · AI early warning]
  end

  L1 --- A1
  L2 --- A2
  L3 --- A3
  L4 --- A4
  L5 --- A5
  L6 --- A6
  A1 & A2 & A3 & A4 & A5 & A6 --> A7
```

| Layer | Proposed FCHIP role |
| --- | --- |
| Community members | Capture needs, participation, household signals |
| CHWs / VHTs | Offline mobile tools, worklists, alerts, structured collection |
| Outreach programmes | Planning, screening campaigns, school/community education metrics |
| Facilities | Facility dashboard, referrals, **secure EMR/HMS ingest** (not replace EMR) |
| Research · partners | Anonymised evidence, training analytics, partner reporting |
| Empowerment / CHIS / IGAs | Enrolment, contributions/claims, livelihood-linked access (where data exists) |
| **Data & Feedback** | GIS maps, climate fusion, AI early warning, continuous improvement |

## Community journey (same cascade, plain words)

```mermaid
flowchart LR
  A[It starts with you] --> B[Health workers come to you]
  B --> C[Care close to home]
  C --> D[Facilities treat you]
  D --> E[We learn and improve]
  E --> F[Families grow stronger]
  F --> A
```

## Indicators the app should digitise

```mermaid
mindmap
  root((Cascade metrics))
    CHWs active and supervised
    Outreach events and screenings
    Referrals completed to facilities
    MCH visits / home visits
    School and community education sessions
    Livelihoods / IGAs where tracked
    CHIS enrolment / contributions / claims where used
```

Next: [03 Architecture](03-architecture.md)
