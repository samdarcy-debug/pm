---
id: weekly-data-platform-2025-28
title: "GTM Data Platform Weekly Report - July 11, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-07-11
updated: 2026-01-06
week_ending: 2025-07-11
reporting_period: "July 7-11, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Data Platform Team Executive Roundup - w.o. 7/7/25**

## **Executive Summary**

The Data Platform team successfully delivered all H2 one-pagers on
schedule while making critical progress on unified profile architecture
and resolving longstanding Advanced Search integration blockers. Most
significantly, Menna Rashwan identified the root cause of AFS (Account
Fit Score) production delays and proposed a solution leveraging the GTM
Data Model that will eliminate duplicate tagging issues and enable ICP
deprecation. The team also achieved key alignment with internal
Operations teams on unified profile requirements, validating our
platform direction while establishing clear boundaries for legacy
workflow support.

## **This Week\'s Progress**

### **Key Momentum Areas**

The team completed all H2 one-pagers on schedule, with the Product
Operations AI-based process facilitated by well-documented prior work.
The efficiency demonstrated by the Product Ops tools validates our
documentation practices and positions the team well for detailed product
design phases ahead.

Adwait Kirtikar secured critical alignment with the internal Operations
team on unified profile strategy, with both teams reaching consensus on
handling duplicate records and leveraging ZoomInfo company matching
capabilities. This validation confirms our platform hypothesis and
establishes Operations as our first customer for unified profile.

Menna Rashwan identified why AFS was not deployed to production for
SalesOS, and proposing that duplicate tagging issues can be eliminated
by basing AFS on the GTM Data Model rather than continuing HBase joins.
This plan enables both Advanced Search delivery and strategic ICP
deprecation in favor of intelligent ML-driven prioritization.

### **Goals & Progress**

**Advanced Search Integration**: Menna achieved 100% completion on AFS
current state analysis, identifying three potential paths forward with
the preferred solution being GTM Data Model integration. The team
discovered that AFS was previously integrated behind a feature flag but
never enabled due to duplicate tagging where companies appeared in
multiple fit segments. Next week\'s focus shifts to partnering with AI
Enterprise team to define the onboarding path for AFS into the GTM Data
Model.

**Unified Profile Architecture**: Adwait completed alignment sessions
with Operations teams and achieved consensus between Data and AI
Engineering teams on output schema general direction. The unified
profile approach directly addresses SDR pain points around duplicate
contact tracking in Salesforce, as confirmed by Henry\'s recent survey
findings. Next week the team will analyze a proposal to have a generic
unified profile entity that will serve as the standard entity for all
Unified Profiles.

### **Strategic Challenges**

Resource allocation unpredictability continues to impact planning
effectiveness, with engineering teams maintaining open capacity for
shifting priorities mid-cycle. Adwait\'s engineering crew faces tight
constraints with competing demands from multiple workstreams, making
fixed monthly planning difficult when workbook requirements remain fluid
and can redirect resources without advance notice.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The current operations workflow expects duplicates by design, primarily
because provisioning systems rely on them for various processes.
However, the future unified profile approach with a unique \'golden\'
record will serve as a single source of truth, validating our platform
hypothesis and reinforcing the MVP direction. This discovery positions
the team to leverage Unified Profiles to mitigate these duplicates by
design. Ideally, the internal ZI provisioning systems wouldn't create
duplicate Accounts in the first place, but we'll see similar scenarios
with most customers.

### **Cross-Team Dependencies**

Our collaboration with the AI Enterprise team on AFS onboarding to the
GTM Data Model is now critical for unlocking Advanced Search production
delivery. This partnership will eliminate the root cause of duplicate
tagging issues while aligning with long-term platform direction,
requiring coordination on implementation timeline and resource
allocation.

## **Looking Ahead**

Next week\'s primary focus centers on finalizing architectural decisions
and accelerating implementation planning across all three major
workstreams. The team will lock in GTM Data Model integration approaches
while maintaining momentum on unified profile development and Advanced
Search production readiness.

Top priorities include partnering with the AI Enterprise team to define
the AFS onboarding path, collaborating with UI Design team to scope
Milestone 1.6 requirements for unified profile, and completing the
architectural review for federated vs. direct API access. Success
depends on resolving ownership boundaries quickly while keeping all
stakeholders aligned on implementation sequencing.

The team enters next week with strong momentum on strategic initiatives,
clear validation of platform direction from internal customers, and
concrete solutions to longstanding technical blockers. With
architectural decisions landing and procurement obstacles addressed, the
Data Platform team is positioned to accelerate delivery across all major
workstreams while maintaining focus on foundational platform
capabilities.

*Source: Data Platform Team 1-2-3 Operating Framework entries from
7/7/2025 - 7/11/2025*
