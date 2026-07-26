# 06 — MVP & phases

SoT: §11.

## MVP components (proposed build set)

```mermaid
flowchart TB
  subgraph mvp [Phase 1 MVP]
    A[CHW/VHT mobile — offline capture]
    B[Multi-source ingest]
    C[Secure EMR/HMS data APIs]
    D[Cascade / loop metrics]
    E[Cloud sync & pipeline]
    F[Climate API integration]
    G[Analytics dashboard]
    H[AI Module v1]
    I[GIS layer v1]
    J[Pilot integration]
  end

  A & C & F --> E
  B --> E
  E --> H & I
  H & I --> G
  D --> G
  J --> A & C & G
```

| MVP piece | Feeds | Surfaces |
| --- | --- | --- |
| CHW/VHT mobile | Visits, vitals, MCH, referrals | Field worklists / alerts |
| Multi-source ingest | School, community, hospital, clinic signals | Pipeline |
| Secure EMR/HMS APIs | Clinical push/sync | Pipeline (not an EMR UI) |
| Cascade metrics | CHW, outreach, referrals, school; CHIS/IGA later | Dashboards |
| Cloud sync | Field + EMR + climate | Core store |
| Climate API | Rainfall, temperature, extremes | Fusion / alerts |
| Analytics dashboard | Trends, alerts, maps, gaps | Facility / programme |
| AI Module v1 | Rule + ML-assisted risk scoring | Alerts |
| GIS layer v1 | Cases, climate overlays, risk zones | Maps |
| Pilot integration | Live catchment workflows | End-to-end loop |

## Phase roadmap

```mermaid
flowchart LR
  P1[Phase 1 Validate<br/>0–12m] --> P2[Phase 2 District<br/>12–24m]
  P2 --> P3[Phase 3 National / regional<br/>24–36m]
  P3 --> P4[Phase 4 Expansion<br/>Year 3+]
```

| Phase | Ship / prove |
| --- | --- |
| **1 Validate** | CHW mobile + GIS + climate + EMR APIs; ≥3 use cases + cascade metrics; alert accuracy |
| **2 District** | Partner facilities; broader EMR onboarding; NGO M&E; optional CHIS dashboards |
| **3 National / regional** | Multi-district Uganda; East Africa; advanced ML; medicine demand forecasting |
| **4 Expansion** | Clinical decision support; NLP; research modules; optional extras |

## Recommended build order (simple)

```mermaid
flowchart TD
  1[1. CHW mobile offline + sync] --> 2[2. Ingest pipeline + cascade metrics]
  2 --> 3[3. Facility dashboard + referrals]
  3 --> 4[4. EMR/HMS secure APIs]
  4 --> 5[5. Climate + GIS overlays]
  5 --> 6[6. AI v1 alerts → CHW + facility + district]
  6 --> 7[7. Prove 3 use cases in live catchment]
```

## Adapt without breaking the product

1. Keep cascade order fixed.  
2. Keep `CAPTURE → FUSE → PREDICT → ALERT → ACT → LEARN`.  
3. Add sources into **ingest**, not as a new product identity.  
4. Add consumers as **surfaces** on the same alerts/metrics spine.  
5. Never replace EMR/HMS — only connect.

← [05 Use cases](05-use-cases.md) · [Index](README.md)
