# 03 — Care spine (modules connected)

This is the main **patient path** across workspaces. Shared key: **patient → visit queue / appointment → encounter**.

## End-to-end care flow

```mermaid
flowchart TB
  PAT[Patients<br/>registry] --> REC[Reception<br/>appointments · queue · payment gate]
  REC --> BRANCH{Path}

  BRANCH -->|Outpatient| OPD[OPD<br/>queue · triage · encounter]
  BRANCH -->|Emergency| ED[Emergency<br/>board · ambulance · handoff]
  BRANCH -->|Admit| IPD[IPD<br/>admissions · transfers]

  OPD --> CLI[Clinical<br/>notes · consults]
  ED --> CLI
  IPD --> RB[Rooms & beds]
  IPD --> NUR[Nursing]
  IPD --> ICU[ICU<br/>when critical]

  CLI --> ORD[Orders]
  OPD --> ORD
  ED --> ORD
  NUR --> ORD

  ORD --> LAB[Lab]
  ORD --> RAD[Radiology]
  ORD --> PH[Pharmacy]
  ORD --> TH[Theater]
  ORD --> PHY[Physiotherapy]

  IPD --> DIS[Discharge]
  OPD --> DIS
  ICU --> DIS
  TH --> DIS

  DIS --> BIL[Billing]
  REC --> BIL
  PH --> BIL
  LAB --> BIL
  BIL --> CLM[Claims]

  CLI -.-> COM[Communications]
  DIS -.-> COM
  ALL[All care events] -.-> REP[Reports]
```

## Domain spine (backend)

```mermaid
flowchart LR
  P[patient] --> A[appointment]
  P --> VQ[visit_queue]
  P --> E[encounter]
  E --> CN[clinical_note · diagnosis · vitals]
  E --> AD[admission · bed_assignment]
  E --> LO[lab_order]
  E --> RO[radiology_order]
  E --> PO[pharmacy_order]
  E --> TC[theatre_case]
  AD --> DS[discharge_summary]
  E --> INV[invoice · payment]
  INV --> IC[insurance_claim]
```

Flow engines (fat services): `opd-flow`, `ipd-flow`, `theatre-flow`, `therapy-flow`, plus `triage` / `emergency-case`.

## Typical outpatient path

```mermaid
sequenceDiagram
  actor Rec as Reception
  actor Doc as OPD / Clinical
  actor Lab as Lab
  actor Ph as Pharmacy
  actor Bil as Billing

  Rec->>Rec: Find / register patient
  Rec->>Rec: Appointment or walk-in queue
  Rec->>Doc: Visit ready
  Doc->>Doc: Encounter + notes
  Doc->>Lab: Lab order
  Doc->>Ph: Pharmacy order
  Lab-->>Doc: Results
  Ph-->>Doc: Dispense
  Doc->>Bil: Charges
  Bil->>Bil: Invoice / payment / claim
```

## Typical inpatient path

```mermaid
sequenceDiagram
  actor Clin as OPD / ED / Clinical
  actor IPD as IPD
  actor Bed as Rooms & beds
  actor Nur as Nursing
  actor ICU as ICU
  actor Dis as Discharge
  actor Bil as Billing

  Clin->>IPD: Admit
  IPD->>Bed: Assign bed
  Bed->>Nur: Ward worklist
  Nur->>Nur: Notes · meds · vitals
  Nur-->>ICU: Escalate if needed
  ICU-->>Nur: Step down
  Nur->>Dis: Discharge planning
  Dis->>Bil: Final charges
```

## Cross-cutting always on

```mermaid
flowchart LR
  WS[Any workspace] --> API[Backend API]
  WS --> RT[WebSocket realtime refresh]
  WS --> OFF[Offline / sync helpers]
  WS --> BADGE[Shell badge counts]
  WS --> PERM[Permission gate]
```

Next: [04 Workspaces](04-workspaces.md)
