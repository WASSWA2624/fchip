# 05 — Proposed use-case flows

SoT: §6. Same pattern: **Signal → Prediction → Action → Learn**.

```mermaid
flowchart LR
  S[Signal] --> P[Prediction] --> A[Action] --> L[Learn]
  L --> S
```

## 1. Disease surveillance (climate-aware)

```mermaid
sequenceDiagram
  participant CHW as CHW/VHT mobile
  participant Clim as Climate API
  participant GIS as GIS
  participant AI as Predictive engine
  participant Dist as District console
  participant Out as Outreach / pharmacy

  CHW->>AI: Fever cluster (villages)
  Clim->>AI: Heavy rainfall
  GIS->>AI: Tight geographic cluster
  AI->>Dist: Outbreak risk ~14 days
  AI->>CHW: Field alert
  Dist->>Out: Testing · nets · pre-stock
```

## 2. Maternal health

```mermaid
flowchart LR
  S[Home-visit BP · Hb proxies · ANC adherence<br/>+ heat where relevant] --> P[High-risk pregnancy · missed ANC · anaemia · pre-eclampsia]
  P --> A[CHW alert · refer before complications]
  A --> L[Referral completion → metrics]
```

**Modules:** CHW mobile · Alerts · Referrals · Facility dashboard · Climate (optional)

## 3. NCDs

```mermaid
flowchart LR
  S[BP from screening · clinics · hospitals · corporate/school] --> P[Hypertension / diabetes hotspots · stroke risk]
  P --> A[Targeted screening · lifestyle campaigns]
  A --> L[Outreach metrics · GIS update]
```

**Modules:** Outreach · Facility dashboard · GIS · Ingest (EMR + field)

## 4. Child health

```mermaid
flowchart LR
  S[Growth · immunisation · diarrhoea<br/>+ flood/sanitation climate] --> P[Malnutrition · low coverage · diarrhoeal clusters]
  P --> A[Nutrition support · immunisation drives]
```

**Modules:** CHW mobile · School health · Climate · District console

## 5. Medicine demand forecasting

```mermaid
flowchart LR
  S[Disease trends · rainfall · consumption · outreach · utilisation] --> P[Demand by facility / community]
  P --> A[Procurement · pharmacy replenishment]
```

**Modules:** Facility dashboard · District console · Climate · Ingest

## 6. Cascade / loop metrics

```mermaid
flowchart LR
  S[CHW activity · referrals · school sessions · CHIS/IGA] --> P[Gap insight e.g. high outreach / low completed referrals]
  P --> A[Rebalance training · camps · capacity]
  A --> L[Learn · improve · serve again]
```

**Modules:** Cascade metrics · District / NGO consoles · Admin

## Cross-use-case wiring

```mermaid
flowchart TB
  CAP[Capture modules] --> CORE[AI · GIS · Climate]
  CORE --> UC1[Surveillance]
  CORE --> UC2[Maternal]
  CORE --> UC3[NCD]
  CORE --> UC4[Child]
  CORE --> UC5[Medicine demand]
  CORE --> UC6[Cascade gaps]
  UC1 & UC2 & UC3 & UC4 & UC5 & UC6 --> SURF[CHW · Facility · District surfaces]
  SURF --> ACT[Community action]
  ACT --> CAP
```

Next: [06 MVP phases](06-mvp-phases.md)
