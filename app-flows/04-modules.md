# 04 — Proposed modules & screens

SoT: §2.4, §4, §7, §11.1.

These are **proposed product modules** for FCHIP — not the current HIS workspaces in the repo.

## Module map (how they connect)

```mermaid
flowchart TB
  subgraph field_ui [Field]
    M1[CHW / VHT Mobile]
    M2[Community / caregiver mobile<br/>optional self-report]
  end

  subgraph programmes [Programmes]
    M3[Outreach & school health]
    M4[Cascade metrics / M&E]
    M5[CHIS & livelihoods<br/>optional]
  end

  subgraph facility_ui [Facility]
    M6[Facility intelligence dashboard]
    M7[Referrals desk]
    M8[EMR / HMS connector<br/>secure APIs]
  end

  subgraph intel [Intelligence]
    M9[Ingest & sync pipeline]
    M10[AI / predictive engine]
    M11[GIS maps]
    M12[Climate fusion]
    M13[Alerts & worklists engine]
  end

  subgraph partners [Partners & governance]
    M14[District / MoH console]
    M15[NGO / partner M&E]
    M16[Research evidence exports]
    M17[Admin · consent · access]
  end

  M1 & M2 & M3 & M8 --> M9
  M9 --> M10 & M11 & M12
  M10 & M11 & M12 --> M13
  M13 --> M1 & M6 & M7 & M14
  M4 --> M14 & M15
  M5 --> M14 & M15
  M6 --> M7
  M16 --> M15
  M17 --> M1 & M6 & M8 & M14
```

---

## Module details

### 1. CHW / VHT Mobile

**Users:** Community Health Workers / Village Health Teams  

```mermaid
flowchart LR
  HOME[Home · worklist] --> VISIT[Household visit form]
  VISIT --> SYM[Symptoms · vitals]
  VISIT --> MCH[Maternal / child indicators]
  VISIT --> REF[Create referral]
  HOME --> ALERT[Alerts inbox]
  ALERT --> ACT[Act · follow up]
  VISIT --> SYNC[Offline queue → cloud sync]
```

| Screens (proposed) | Job |
| --- | --- |
| Worklist | Today’s visits, follow-ups, alert tasks |
| Visit / form | Offline structured capture |
| Referral | Send household to facility; track completion |
| Alerts | Risk flags from intelligence core |
| Sync status | Offline queue health |

**Connects to:** Ingest pipeline · Alerts engine · Referrals desk · Cascade metrics  

---

### 2. Community / caregiver mobile (optional)

**Users:** Patients / caregivers (where used)  

```mermaid
flowchart LR
  ME[My household] --> REP[Self-report symptoms / needs]
  ME --> MSG[Guidance · appointment hints]
  REP --> ING[Ingest]
```

**Connects to:** Ingest · CHW follow-up worklists  

---

### 3. Outreach & school health

**Users:** Programme managers, CHW supervisors  

```mermaid
flowchart LR
  PLAN[Plan campaign / school session] --> FIELD[CHW field capture]
  FIELD --> MET[Session & screening metrics]
  MET --> DASH[Facility / district views]
```

| Screens | Job |
| --- | --- |
| Campaign planner | Outreach, screening, school health |
| Session log | Attendance, topics, outcomes |
| Coverage map | Where programmes ran |

**Connects to:** CHW mobile · Cascade metrics · GIS  

---

### 4. Cascade metrics / M&E

**Users:** Programme managers, NGOs, districts  

```mermaid
flowchart LR
  IND[Indicator store] --> GAP[Gap detection]
  GAP --> ALERT[Cascade gap alerts]
  IND --> REP[Partner reports]
```

Tracks SoT indicators: active CHWs, outreach, completed referrals, MCH visits, education sessions, optional CHIS/IGA.

**Connects to:** All capture modules · District / NGO consoles · AI cascade-gap use case  

---

### 5. CHIS & livelihoods (optional)

**Users:** Partners who run financial protection / IGAs  

```mermaid
flowchart LR
  ENR[Enrolment] --> CONT[Contributions]
  CONT --> CLM[Claims / access]
  ENR --> MET[Cascade metrics]
```

**Not** core product identity — programme intelligence only.

---

### 6. Facility intelligence dashboard

**Users:** Clinics, medical centres (population health view)  

```mermaid
flowchart TB
  FD[Facility dashboard] --> TREND[Trends · alerts]
  FD --> MAP[Catchment GIS]
  FD --> REF[Open referrals]
  FD --> OUT[Outreach priorities]
  FD -.->|does not replace| EMR[External EMR/HMS]
```

| Screens | Job |
| --- | --- |
| Overview | Alerts, caseload risk, cascade gaps |
| Map | Village/parish hotspots + climate overlay |
| Referrals | Inbound from CHWs; completion |
| Stock signal | Demand forecast hints (links to pharmacy partners) |

**Connects to:** EMR connector · Alerts · GIS · Referrals · District console  

---

### 7. Referrals desk

```mermaid
flowchart LR
  CHW[CHW creates referral] --> QUEUE[Facility referral queue]
  QUEUE --> DONE[Completed at facility]
  DONE --> MET[Cascade metrics]
  EMR[EMR clinical outcome] -.-> DONE
```

---

### 8. EMR / HMS connector

**External systems push/sync into FCHIP** — authenticated, consent-aware, least privilege.

```mermaid
flowchart LR
  EMR[Existing EMR/HMS] -->|secure API| CONN[FCHIP connector]
  CONN --> ING[Ingest pipeline]
  ING --> CORE[Intelligence core]
```

FCHIP **does not** become the hospital EMR.

---

### 9–13. Intelligence stack (shared services)

```mermaid
flowchart TB
  ING[9. Ingest & sync] --> AI[10. AI / predictive]
  ING --> GIS[11. GIS]
  ING --> CL[12. Climate fusion]
  AI & GIS & CL --> AL[13. Alerts & worklists]
  AL --> MOB[CHW mobile]
  AL --> FD[Facility dashboard]
  AL --> DC[District console]
```

---

### 14. District / MoH console

**Users:** District health offices, ministries  

```mermaid
flowchart LR
  MAP[Population map] --> WARN[Early warnings]
  WARN --> ACT[Deploy testing · stock · outreach]
  MET[Cascade M&E] --> PLAN[Planning]
```

---

### 15. NGO / partner M&E

Real-time programme monitoring, impact evidence, optimisation — same metrics spine, partner-scoped.

---

### 16. Research evidence exports

Anonymised datasets for approved research — no raw PHI dumps.

---

### 17. Admin · consent · access

```mermaid
flowchart LR
  ORG[Org · catchment · facilities] --> USERS[Users · roles]
  USERS --> CHW[CHW]
  USERS --> FAC[Facility]
  USERS --> DIST[District / partner]
  CONSENT[Consent · privacy] --> API[EMR API scopes]
```

---

## User → module matrix

| User (SoT §7) | Primary modules |
| --- | --- |
| CHW / VHT | Mobile, Alerts, Referrals |
| Medical centres & clinics | Facility dashboard, Referrals, EMR connector |
| District health offices | District console, GIS, Alerts, Cascade metrics |
| NGOs & partners | Partner M&E, Cascade metrics, Outreach |
| Ministries of health | District/national console, early warning |
| Insurance companies | Population insights (prevention-focused) |
| Research institutions | Evidence exports |

Next: [05 Use cases](05-use-cases.md)
