---
id: learnings-2025-044
title: Q3 2025 Learnings Memo - Intent
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/intent]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



**North Star: DATA ROI**



- **Increased Intent Volume bandwidth with 100%** - supporting custom

  intent customers and DaaS clients (Ziff Davis, Deloitte) who subscribe

  to all standard topics and custom intent customers



- **Established Intent Quality metrics** - score 32 (32 documents out of

  100 is relevant to the topic)



- **Established Persona level intent pipeline** - 180M (daily from

  Clickagy)



- **Intent topic viability test from 1 week to few hours** - testing on

  historical data instead of real data, directly accelerating sales

  cycles and custom intent adoption



These improvements ladder up to customer retention and revenue growth by

preventing churn from competitors, increasing custom intent adoption

rates, and enabling strategic account targeting.



#### **Key Learnings**



- **Intent topic setup speed is a competitive differentiator** - Our

  setup process remains non-competitive in product bake-offs versus

  other GTM platforms, making topic setup acceleration critical for

  winning deals. The ability to show historical intent volume for new

  topics eliminates weeks of waiting and uncertainty for prospects

  evaluating custom intent.



- **Person-level intent is table stakes** - Competitors already offer

  person-level intent as standard; staying at company-level only puts us

  at a disadvantage for enterprise customers who expect granular

  stakeholder targeting.



- **Intent volume directly correlates with customer satisfaction** -

  Without scaling, we risk continued volume decay, reduced satisfaction,

  and potential churn, particularly as we see increased interest from

  clients leaving 6sense.



- **AI-based topic classification can transform accuracy** - Moving

  beyond keyword-based matching to contextual AI understanding

  significantly improves lead quality and reduces irrelevant leads for

  sales teams.



- **Data partnerships create flywheel effects** - Integrating partners

  like PathFactory, Vendr, and Predactive strengthens both our identity

  graph and intent coverage, creating compounding value.



- **Infrastructure augmentation is invisible but critical** - Our 100%

  signal augmentation work required extensive DS, QA, DevOps, and

  infrastructure coordination but delivered material customer impact

  with lowering customer complaints on intent volume.



- **Support structure needs clarity** - Intent support cases revealed

  fragmentation across L1/L2/L3 teams, requiring documented escalation

  processes and ownership alignment.



- **International intent data is a growing blocker** - International

  intent data is still very low compared to competitors who have

  established overseas publishers networks.



- **Cross-team dependencies multiply complexity** - Intent touches GTM

  Config, GTM Store, VRS, and multiple data pipelines, requiring

  proactive coordination to avoid delays.



#### **Hypotheses & Results**



### **Hypothesis 1: Augmenting intent signals capacity by 100% will restore coverage and prevent DaaS client churn**



**Result:** ✅ **VALIDATED\**

Successfully delivered 100% increase in intent signals quality. This

directly supported high-value DaaS clients (Ziff Davis, Deloitte)

subscribed to all standard topics. Key learning: The investment required

extensive cross-functional coordination (DS, QA, DevOps, Infra) but was

essential to restore market leadership position. Volume scaling is

foundational to maintaining enterprise customer confidence. We are now

in a good position to add more standard and custom intent topics and

signals.



### **Hypothesis 2: Persona level intent data will enable more precise targeting and improve competitive positioning**



**Result:** ✅ **DELIVERED\**

Delivered 180M daily person-level intent signals from Clickagy to ZI

(for custom and standard intent). This enables identification of

specific job functions and job levels showing buying intent, addressing

a major competitive gap. Key learning: Clickagy resolution quality

wasn\'t initially at 100% confidence but was \"good enough\" to move

forward with production testing. We learned that waiting for perfect

data would have further delayed a critical competitive feature. Persona

level enriched intent pipeline is now operational for DS consumption

Q4'25 and app experience in Q1'26.



### **Hypothesis 3: Retroactive Intent will dramatically reduce time-to-value for custom intent topics**



**Result:** ✅ **VALIDATED\**

Retroactive Intent reduced the time to test new custom topics on

viability from weeks to hours, through historical data. Demo delivered

successfully, and the feature is now in testing state with the custom

intent team. Key learning: This capability transforms the sales process

by removing uncertainty about topic viability. Prospects can immediately

see potential volume rather than waiting weeks for data collection. This

will accelerate the sales process and be seen as a competitive

advantage.



### **Hypothesis 4: AI-based topic classification will improve intent signal accuracy and reduce false positives**



**Result:** 🔄 **IN PROGRESS - MULTI-QUARTER INITIATIVE\**

Roadmap established for Q4-Q1 implementation:



- Q4: DS model for matching system + quality monitoring + cleaner

  document creation



- Q1: MVP implementation (hybrid approach) in intent pipeline



- Q2: AI Topic Classification GA



Key learning: This is more complex than initially scoped. AI-based

classification understands contextual intent beyond keywords, which is

critical for lead quality. However, achieving this requires foundational

work across web page visit processing,DS modeling, document processing,

and pipeline integration. We aligned the DS team on approach, but

limited DS resources pushed timelines further than ideal.



#### **Go-forward Changes & Plan**



1.  **Testing AI-Based Topic Classification Quality Improvement**



    - DS model for matching system



    - Quality monitoring document for topic matching



    - Improved cleaner document creation



2.  **Standardize on Account Level Intent on whole platform**



    - One type of intent signal available for all applications



    - Make ALI data available in GTM Store



3.  **Persona Level Intent**



    - DS model for persona level intent spikes



    - Increase volume for persona level intent



4.  **Intent Data Partnership Expansion**



    - Operationalize PathFactory, Vendr, and other flywheel partners



    - Expand Intent data acquisition in volume and international



5.  **Intent Roadmap Clarity & DS Alignment**



    - Publish prioritized Intent DS Roadmap with clear dates



    - Align on Workbooks integration timeline (replace Audience Builder)



    - Define GTM Config impact on ZIM Intent workflows



6.  **Intent Topic Spike anomaly detection**



    - Remove sudden spikes proactively and automated



    - Create trust in quality of intent signal



#### **Leveraging AI**



1.  **ZI Keyword & Topic Compliance Agent**



Built a workable chatbot to test keywords and topics for legal

compliance. This initiative reduces the risk of regulatory violations,

protects the organization from potential fines or legal challenges, and

enables teams to move faster with confidence.



**Impact:**



- Reduced compliance review time from days to hours



- Enabled self-service compliance checking for GTM and sales teams



- Reduced legal team bottleneck for routine compliance questions



- De-risked international expansion by catching compliance issues

  earlier



**Demo:** Successfully tested with the legal team, who accepted it as a

solution. We identified and resolved setup requirements for appropriate

user permissions.



2.  **Intent Quality Metrics System**



Built an LLM-based quality scoring system that achieves **90% accuracy

in manual validation** while enabling systematic baseline measurement

across all intent topics. The system includes both batch processing and

API access to support monthly assessment cycles.



**Impact:**



- **Replaces subjective evaluation with data-driven quality

  management** - Eliminates inconsistent, gut-feel quality assessments

  with quantifiable metrics



- **Identifies lowest-performing topic groups** - Monthly cycles

  systematically surface topics requiring attention



- **Enables targeted 10-20% improvement initiatives** - Data-driven

  identification of specific topics for enhancement campaigns



- **Scales quality assessment** - What previously required weeks of

  manual review per topic now runs systematically across all topics

  monthly



- **Creates quality audit trail** - Historical baseline measurements

  enable trend analysis and regression detection



**Business Value:** This system transformed intent quality from an

ad-hoc, reactive problem into a proactive, measurable program. We can

now confidently tell customers \"we systematically monitor and improve

quality across all topics\" rather than \"we fix issues when reported.\"



**How will you expand your use of AI in the coming quarter?**



1.  **AI-Based Topic Classification**



    - Moving beyond keyword matching to contextual AI understanding



    - Implementing DS model for matching system with quality monitoring



    - This will fundamentally improve intent accuracy and lead quality



2.  **AI based Topic Spike Anomaly detection**



    - Leveraging LLM ability to analyse relevant intent data



    - Using for intent pipeline analysis and troubleshooting



3.  **Intent Topic Analysis and Creation Automation**



    - Automated analysis of missing standard intent topics



    - Automated analysis of viable standard intent topics



    - Automated creation of standard and custom intent topics



4.  **GTM Config Agent Integration**



    - Intent data as input to GTM Configuration agent



    - Enabling conversational access to intent insights



    - Supporting GTM Config 0 launch with intent context



**Key Learning:** AI tools are most impactful when they reduce

bottlenecks (legal compliance, data analysis) or improve quality at

scale (topic classification). The key is identifying high-friction,

high-volume workflows where AI can compound efficiency gains.

