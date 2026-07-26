# 01 — Proposed overview

SoT: §1, §4.1, §4.4.

## What FCHIP is

**FCHIP** turns fragmented community and facility health signals into **predictive, climate-aware intelligence**. It powers the cascade **Data & Feedback** loop.

| Is | Is not |
| --- | --- |
| Intelligence platform on the cascade | A hospital / EMR product |
| Connects CHWs, facilities, districts, partners | A replacement for clinic software |
| AI + GIS + climate fusion | Single-purpose booking or SMS tool |

## Proposed big picture

```mermaid
flowchart TB
  subgraph field [Last mile]
    COM[Community members]
    CHW[CHWs / VHTs]
    OUT[Outreach programmes]
    SCH[Schools · pharmacies · labs · MCH]
  end

  subgraph clinical [Clinical feeds — external]
    FAC[Clinics · hospitals]
    EMR[Existing EMR / HMS]
  end

  subgraph climate [Place & climate]
    GIS[GIS layers]
    CLI[Climate APIs]
  end

  subgraph fchip [Proposed FCHIP app]
    CAP[Capture & sync]
    CORE[AI/ML · Predictive · GIS · Climate fusion · Clinical support]
    OUT_UI[CHW app · Facility dashboard · District / partner console]
  end

  subgraph action [Action]
    REF[Referrals]
    CAMP[Outreach · testing · stock]
    LEARN[Learn · improve · serve again]
  end

  field --> CAP
  clinical --> CAP
  climate --> CORE
  CAP --> CORE --> OUT_UI --> action --> LEARN
  LEARN -.-> field
```

## Who uses which surface

```mermaid
flowchart LR
  CHW[CHW / VHT] --> MOB[Mobile app<br/>capture · worklists · alerts]
  FAC[Facility teams] --> FD[Facility dashboard<br/>trends · referrals · maps]
  DIST[District · NGO · MoH] --> DC[District / partner console<br/>early warning · M&E]
  RES[Research] --> EV[Anonymised evidence exports]
  EMR[External EMR/HMS] --> API[Secure FCHIP data APIs]
```

## Theory of change FCHIP supports

```text
Participation → Prevention → Access → Earlier care → Better health → Livelihoods → Learning → Better services
```

Next: [02 Cascade](02-cascade.md)
