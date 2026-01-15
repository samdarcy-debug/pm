---
id: learnings-2025-006
title: Q3 2025 Learnings Memo - Hayden Cowell
type: doc
status: approved
team: data
owner: '[[teams/data/_people/hayden-cowell]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- data
related: []
---
#### **Metric Alignment**



This quarter marked a significant investment in Polaris metrics, a

comprehensive framework designed to elevate our understanding and

measurement of data North Star metrics. These metrics provide

organization-wide visibility into data health, establishing a foundation

for strategic decision making across the data organization.



Polaris metrics will serve as the cornerstone measurement system for

evaluating accuracy, coverage, and depth across our data landscape. With

company metrics launching in Q4 and contact metrics completing by end of

Q3, we\'re positioning the organization to replace existing \"company

coverage\" and \"company perfect accuracy\" driver metrics with a more

robust, holistic measurement approach. This enhanced visibility will

empower teams across the organization to make data-driven product

decisions that directly influence both our North Star and driver

metrics.



#### **Key Learnings**



This quarter revealed a critical opportunity to expand our approach to

data feedback loops. Working alongside Heather Ma and Lars Vedo on the

\"3 new Data Feedback Loops per quarter\" North Star metric, I initially

focused on the feedback API as a bridge between customers and our data

organization through application team integrations.



Through collaboration with Heather, we identified a broader opportunity:

extending our data model to capture feedback from Copilot Chat

interactions. This strategic expansion allows us to scale existing

feedback mechanisms while capturing dual insights, both agent

performance feedback and organic data feedback that emerges naturally

from user interactions. This integration transforms passive product

usage into an active feedback channel, creating a continuous improvement

loop between customer experience and data quality.



#### **Hypotheses & Results**



**Hypothesis:** A confidence score would be the optimal method for

communicating email deliverability information to customers.



**Result:** Customer research revealed this approach would create more

confusion than clarity. Through analysis of customer use cases and

historical data, we discovered that reductive scoring systems erode

trust rather than build it. Our revised approach focuses on surfacing

the underlying metrics that inform our profilers\' decisions. This

transparency first strategy builds authentic customer trust by revealing

our decision making process rather than obscuring it behind simplified

scores. This insight is now shaping the foundation of our broader data

transparency initiative.



**Hypothesis:** Sampling from live data would introduce noise into

Polaris metrics by capturing less relevant data, while sampling from

match logs would yield more accurate results that better represent

actual customer perception.



**Result:** Our analysis confirmed this hypothesis, but revealed

important segmentation patterns in the data itself. For records about

smaller companies and lower-level employees, match log sampling proved

significantly more representative, these profiles are viewed less

frequently by customers, so live data sampling would include substantial

noise from rarely-accessed records. However, for records about larger

companies and senior executives, the distinction between methodologies

diminished since these high-value profiles are consistently viewed

regardless of sampling approach. This created a critical insight:

relying solely on match log sampling would skew our metrics toward

larger companies and senior roles. To ensure Polaris metrics accurately

reflect data quality across our entire dataset, we incorporated both

sampling methodologies, providing balanced visibility into both

high-engagement and long-tail data segments.



#### **Go-forward Changes & Plan**



Next quarter\'s priorities center on strengthening the communication

bridge between our data organization and customers, with three strategic

initiatives:



**Data Transparency Initiative**: We\'re developing a suite of metrics

that illuminate how our profilers make decisions. By exposing the

factors driving our data quality decisions, we build customer confidence

through understanding rather than through assertions. This represents a

fundamental shift from telling customers our data is trustworthy to

showing them why.



**Feedback API Expansion**: Building on this quarter\'s learnings,

we\'ll scale customer feedback collection across multiple touchpoints.

This bi-directional communication channel will directly inform product

decisions, ensuring we\'re building toward actual customer needs rather

than assumed requirements.



**TUI Explainability Tools:** Enabling our CX team with sophisticated

explainability tools will transform how we support customers. Rather

than providing scripted responses, we\'ll empower CX personas to deliver

educated, context-aware answers about our data decisions.



These interconnected initiatives align our success metrics directly with

customer perception. By investing in transparency and feedback loops,

we\'re creating a cycle that should reduce churn, accelerate new

business development, and ensure our metrics reflect what customers

actually value.



#### **Leveraging AI**



This quarter, I discovered an effective AI workflow using Chorus call

transcripts combined with ZI Chat to dramatically accelerate

documentation and knowledge sharing. An unexpected insight emerged:

explicitly discussing context during calls, even when participants

already understand it, significantly improves LLM comprehension. Regular

\"big picture\" recaps further enhanced post-call documentation quality

while creating an unintended benefit of improved team alignment during

discussions.



**Next Quarter\'s AI Strategy:** I\'ll leverage the Slack integration

and weekly recap agent to track productivity patterns and ensure

consistent progress toward goals. This self-monitoring approach should

provide visibility into task alignment and help identify optimization

opportunities in my workflow.

