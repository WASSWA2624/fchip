# 03 — Proposed architecture

SoT: §4.2–4.4, §5.

## Layered flow

```mermaid
flowchart TB
  subgraph sources [Data sources]
    CHW[CHWs / VHTs]
    SCH[Schools]
    COM[Communities]
    FAC[Hospitals · clinics]
    EMR[Existing EMR / HMS]
    PAT[Patients · caregivers mobile]
    PH[Pharmacies]
    MCH[ANC / PNC · immunisation · nutrition]
    CORP[Corporate / school wellness]
    LAB[Labs / PoC]
    NCD[Gericare / NCD cohorts]
    CHIS[CHIS / livelihoods where used]
    HMIS[HMIS / DHIS2 where approved]
    RES[Research / NGO M&E]
    CLI[Climate API]
  end

  subgraph capture [Capture layer]
    OFF[Offline mobile forms]
    API[Secure EMR/HMS data APIs]
    ING[Climate + multi-source ingest]
    SYNC[Cloud sync · validate · store]
  end

  subgraph core [FCHIP intelligence core]
    AI[AI / ML engine]
    PRED[Predictive analytics]
    GIS[GIS maps]
    FUS[Climate–health fusion]
    CS[Clinical support guidance]
  end

  subgraph consumers [Consumer surfaces]
    MOB[CHW / VHT mobile<br/>alerts · worklists]
    FD[Facility dashboard]
    DC[District · NGO · partner console]
  end

  ACT[Actions: referrals · outreach · stock · surveillance]

  sources --> capture --> core --> consumers --> ACT
  ACT -.->|learn · improve| sources
```

## Intelligence core (deep tech)

```mermaid
flowchart LR
  IN[Ingested signals] --> AI[AI]
  IN --> ML[ML]
  IN --> GIS[GIS]
  IN --> CL[Climate fusion]
  IN --> NLP[NLP — later / where needed]
  AI & ML & GIS & CL --> SCORE[Risk scores · hotspots · early warnings]
  SCORE --> OUT[Explainable alerts to CHW · facility · district]
```

| Technology | Proposed function |
| --- | --- |
| AI | Disease risk, outbreak warning, maternal / NCD scoring |
| ML | Patterns from history, seasons, outreach outcomes |
| GIS | Disease distribution, hotspots, resource gaps |
| Climate APIs | Rainfall, temperature, extremes fused with health |
| Secure EMR/HMS APIs | Real-time clinical share — **do not replace** facility EMR |
| Mobile capture | Offline CHW/VHT structured forms |
| Cloud | Sync across facilities and admin levels |
| Dashboards | Trends, maps, alerts for facilities and districts |
| NLP | Local-language symptom reporting / summarisation where appropriate |

## Early detection path (example)

```mermaid
sequenceDiagram
  participant VHT as VHT mobile
  participant Clim as Climate API
  participant GIS as GIS layer
  participant Core as FCHIP core
  participant Dist as District / outreach
  participant Pharm as Pharmacy stock

  VHT->>Core: Fever reports (3 villages)
  Clim->>Core: Heavy rainfall
  GIS->>Core: Geographic cluster
  Core->>Core: Risk score · malaria/outbreak window
  Core->>Dist: Explainable early warning
  Core->>VHT: Field alert / worklist
  Dist->>Pharm: Pre-stock · testing · nets
```

Next: [04 Modules](04-modules.md)
