---
id: learnings-2025-032
title: Q3 2025 Learnings Memo - Unknown PM
type: doc
status: approved
team: intelligence
owner: '[[teams/intelligence/_people/unknown-pm]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- intelligence
related: []
---
# **Metric Alignment**



**North Star Metric:\**

Adoption and trust of APS 3.0+ as the unified prioritization layer

across ZoomInfo's GTM products



**H2 Focus:\**

Deliver APS 3.0+ as the backbone for account and product-level

prioritization, unify legacy scoring (AFS, IMS), optimize Top Contacts

at ReachOut scale, and establish explainability as the new standard for

seller trust.



## **Key Achievements**



**Lookalikes (Account + Contacts)**



- **Lookalike for Accounts delivered for Top 100K:**



  - [**[Company Lookalikes API

    Docs]{.underline}**](https://ds-afs-two-tower.data-apps-primary.prd.zi-int.com/docs#/lookalikeProvider/company_lookalikes_api_v1_lookalikes_company_lookalikes_post)



- **Delivered POC for both Account and Contacts:**



  - **https://ds-company-look-alike.data-apps-primary.dev.zi-int.com/**



**Top Contacts Results + Optimization:**



- [**53--64% stronger results (relative lift)** compared to Buying

  Groups helping users zero in on the right people faster and boosting

  exports/engagement .]{.mark}



- **Performance tuning and load testing scaled throughput to \~250

  calls/sec (up from 50/sec).**



- Now supporting ReachOut campaign demand without cluster instability.



**APS Scoring API (Sync + Batch):**



- Synchronous API enabled real-time APS.



- Batch API unlocked scalable (currently in progress)



**ML Foundational Pipeline:**



- Built and deployed a centralized pipeline feeding APS, AFS v2, IMS

  2.0, and Contact Recommendations.



- Established a foundation for continuous retraining and feature sharing

  across models.



## **Key Learnings**



- **Unified \> fragmented:** Teams shifted from using AFS/IMS in

  isolation to APS as the default scoring lens; the fragmentation

  problem is being solved.



- **Scale ≠ stability without tuning:** Top Contacts wouldn't have

  survived ReachOut campaigns without aggressive performance work.



- **Multi-APS is still open:** Product-level scoring is possible, but

  experiments showed complexity in how sellers interpret multiple

  overlapping APS values.



## **Hypotheses & Results**



**H1: Signals pipeline improves model performance**



- ✅ Validated---central pipeline reduced duplication, enabled

  retraining, and improved IMS stability.



**H2: APS scores accessible everywhere drives adoption**



- ✅ Validated---APIs made APS usable in CoPilot, Workbooks, Plays.



**H3: Top Contacts cannot scale without optimization**



- ✅ Validated---throughput scaled to 200--300 calls/sec, unlocking

  ReachOut.



**H4: LLMs can boost results for our top 100K for Lookalikes**



- ⚠️ Mixed results -- LLMs provide helpful acceleration, but they also

  introduce an additional factor: time required to review and correct

  hallucinations.



**H5: AFS v2 increases APS precision**



- ✅ Validated---tenant-level signals improved APS quality; early lifts

  seen in recall@K.



**H6: Flexible matching expands use cases**



- ✅ Validated---matching system supports ICP generation, lookalikes,

  and free-text matching.



**H7: Multi-APS is required for product-level prioritization**



- ⚠️ Mixed---technically feasible, but UX/design challenges remain

  around multiple scores per account.



## **Go-Forward Plan (Q1--Q2 2026)**



### **Model Improvements**



- Upgrade APS and AFS models from linear regression to XGBoost or Random

  Forest to improve precision.



- Expand the explainability layer and extend it into chatbots, Plays,

  and CRM enrichment.\

  Standardize "Why this account?" explanations across all GTM surfaces.



### **Signals Quality**



- Enhance CIO and external signals for IMS.



- Prioritize **relevance over volume** in the signal pipeline.



### **Scalability & Performance**



- Scale Top Contacts beyond 300 RPS with horizontal scaling.



- Establish clear SLAs for APS API usage across tenants.



### **Consistency Across Products**



- Roll out unified score/UX language across Agents, MCP, and Workspace.



## **Leveraging AI -- Most Impactful Use Cases**



**What I've Learned About AI**



Over the past quarter---working with large structured datasets like the

top-100K---I've seen where LLMs excel, where it fails, and why ML is

still important.



**LLMs Unlock the User Experience but Don't Replace ML\**

LLMs are strong for reasoning and summarization but unreliable for

ranking and scoring due to hallucinations and lack of repeatability.

Tree-based ML methods (XGBoost, CatBoost) remain more accurate and

efficient for tabular tasks Even recent benchmarks confirm deep models

rarely outperform ensembles.



**Explainability Is Non-Negotiable\**

Modern work on LLMs for explainability shows progress but also cautions

on faithfulness and robustness.



**ML + LLM Is the Winning Pattern**



ML delivers precise, scalable scoring. LLMs provide reasoning and

human-friendly interfaces. Anchoring LLMs on ML outputs and semantic

graphs reduces hallucinations and produces decision-ready insights.



**Summary\**

ML remains the backbone for scalable, trustworthy results. LLMs add

flexibility, UX, and explanation. A hybrid ML + AI strategy---anchored

in strong signals and context---is essential for accuracy, adoption, and

differentiation.

