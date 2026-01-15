---
id: learnings-2025-021
title: Q3 2025 Learnings Memo - Tanvi Vaidya
type: doc
status: approved
team: gtm studio
owner: '[[teams/gtm studio/_people/tanvi-vaidya]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- gtm studio
related: []
---
#### **Metric Alignment**



My work contributes to the north star metric, \"Credits per records

under management\" by expanding the data richness and usability of

Workbooks, which is the key activation product within GTM Studio.



Last Quarter - Expanding Data Depth & Usability:



Focused on enabling customers to build more valuable, actionable

workbooks by adding critical signal types (Websights Buyer ID,

Employment Changes) so that customers can build higher-confidence

prospect lists worth activating and improved workbook discoverability

and transparency ( page organization, filter/source visibility).



Next Quarter - Removing Activation Blockers:



Prioritizing the maintenance, performance capabilities and advanced use

cases that remove the biggest friction points preventing customers from

building and exporting larger, more complex workbooks.



Business Impact:



Together, these investments create a virtuous cycle, better data and

usability drives better targeting and more workbook creation, which

drives higher exports and activation, thus increasing credit

consumption.



#### **Key Learnings**



Customer & User Insights:



- Customers need more guidance and starter templates - Early access

  users feel overwhelmed by available data and functionality in

  workbooks, consistently requesting clear starting points, workbook use

  case examples, and the ability to learn from other customer

  implementations.



- Workbook activation to sales engagement tools - Customers want to send

  workbook data into Outreach and Marketo sequences, bulk tag companies

  with sales tags for easy visibility for the sales team or have any

  other process by which they can share workbooks with sales and

  marketing teams.



Technical Learnings:



- Signals limitations - In current state we cannot join data across

  sources (e.g., signal fields with person/company fields), we also

  cannot support nested query logic like \"(signal type A AND person

  name B) OR (signal type C AND person name D)\", so adding additional

  signals in workbooks would be blocked until we have GraphQL, new

  metadata registry and new person and company collection integration.



#### **Hypotheses & Results**



**Hypotheses 1:** Giving customers maximum flexibility and all available

data upfront will empower them to build custom workbooks for their

unique needs



Learning: While power users appreciated the flexibility, the majority of

customers felt overwhelmed by available data and functionality. They

consistently requested starter templates, clear use case examples, and

the ability to learn from other customer implementations. The lack of

prescriptive guidance became a barrier to adoption (mentioned as a

"barrier" recently by Salary.com). We learned that lack of direction

created analysis-paralysis.



**Hypotheses 2:** Enriching workbooks with diverse signal types would

enable customers to build richer prospect profiles, leading to

higher-confidence targeting and increased activation.



Learning: Customers confirmed that additional signal data that they can

configure further is valuable, but we learned that raw data alone has

limited impact and users need aggregated views from the start. The

\"what\" (signal types) matters, but the \"how it\'s presented\"

(aggregation, more details) is equally critical for customers to make

prioritization decisions. We incorporated this feedback into our feature

design.



**Hypotheses 3:** Adding new signal types to workbooks would be a

relatively straightforward implementation work as long as data exists in

Solr and/or GSO



Learning: We uncovered fundamental architectural limitations.

Signal-based work revealed that we cannot join data across different

sources (e.g., signal fields with person/company fields), and don't have

support for nested query logic. Additionally, we experienced significant

back-and-forth on data types, and supported operators for required

fields, further complicated by multiple teams working from their own

understanding of requirements. We learned that including IC engineers

(not just leads) in detailed field-level requirements discussions from

the start is critical, and that our current data architecture requires

temporary workarounds until GraphQL work is completed.



#### **Go-forward Changes & Plan**



- Unblocking Core Workbook Functionality & Maintenance - Enable users to

  edit sheet criteria and column configurations, understand what

  criteria was used to create columns, and duplicate/clone sheets,

  thereby addressing the recurring customer pain point of being unable

  to modify workbooks or change column configurations after creation.



- Improving Performance & User Experience - Queue column jobs to run in

  the background and provide clear cell-level response and error states

  to solve the bottlenecks where large enrichments take significant time

  and block the user from taking any other action and addressing user

  confusion about blank cells and processing status.



- Unlocking Signal Value & Advanced Use Cases - Surface signal details

  (exact intent topics, and scoops descriptions) and enable dynamic

  contact finding based on varying row-by-row criteria or custom input,

  delivering the key information users need for prioritization and buyer

  group identification.



#### **Leveraging AI**



1\. Slack Feedback Agent (ZI Chatbot) - Used the [[slack feedback

detection]{.underline}](https://zoominfo-chatbot-ui.zi-ext.com/56/agents/1204)

agent in ZI chatbot to aggregate and summarize user feedback from

multiple Slack channels with direct links to threads. This transformed

weeks of manual channel-scrolling into minutes of comprehensive insight

gathering.

[[Here]{.underline}](https://docs.google.com/document/d/1HOtl9-kyiNo8-AbltAWq0bJIEKguUq9KS7FAikl_ITk/edit?tab=t.xx6rqy7v4ypq)

is the document that it created for me.



2\. Claude for Functional Specification Generation - Created a prompt in

claude along with giving it a template where I provide the user story

and key user flow bullet points, and Claude generates the complete PRD

following the template format. This reduced PRD creation time and

ensured consistency across specifications.



Prompt:



(after uploading a previous PRD)



"Help me create a Functional requirement document that is at a feature

level



1.  Review the attached docs, ONLY use the sections, style and format

    from that and NOT the content



2.  Always include the following sections: 1. Introduction 2. Problem

    Statement 3. Use cases 4. Functional Requirements details 5. Not in

    scope 6. Open Questions



3.  Wait for me to give information about my features



4.  Create requirement doc for me



5.  Keep this formatting and style in context for any other requests

    from me"



3\. Cline for Rapid Prototyping - Used Cline to quickly create

interactive prototypes to validate user flows before engineering

investment. For instance, I built a prototype for signals flow, showed

it to customers within days, and validated the concept before writing

detailed requirements. This de-risked engineering effort and ensured we

built what customers actually needed.



I plan to use AI for the following as well in the upcoming quarter:



- Competitive Intelligence: Monitor competitor releases, feature

  updates, and customer reviews (Clay, Common Room, UnifyGTM) to

  maintain awareness of competitive positioning and identify

  differentiation opportunities.



- Test Plan Generation: Leverage Claude to generate comprehensive test

  plans from PRDs, including edge cases, error scenarios, and acceptance

  criteria, ensuring better QA coverage and faster validation cycles.

