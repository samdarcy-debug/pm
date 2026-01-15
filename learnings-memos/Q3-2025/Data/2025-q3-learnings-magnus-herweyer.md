---
id: learnings-2025-010
title: Q3 2025 Learnings Memo - Magnus Herweyer
type: doc
status: approved
team: data
owner: '[[teams/data/_people/magnus-herweyer]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- data
related: []
---
#### **Metric Alignment**



**Data ROI**



**NeverBounce** [[H2 2025

roadmap]{.underline}](https://docs.google.com/document/d/1qwZFTyMds-W7_R04yACVPOnydeSaq4M8CnhxgGfyUFQ/edit?usp=sharing) -

Currently reducing decade-long tech debt to improve email validation

accuracy and volume---a critical dependency for the person pipeline that

powers SalesOS, TalentOS, and all downstream applications: upgrading

unsupported PHP code to Java, migrating DB's to managed DB's, and

rewriting core services to be more performant. Engineering capacity

doubled (2→4 ICs) to address this backlog, but additional investment is

[[likely

needed]{.underline}](https://docs.google.com/document/d/18IITxJjHynyj4rV4SvbrcARIRP0BqBhb16v5YsBd0W0/edit?usp=sharing)

to reduce bounce rates from 10%→3% for legal compliance on privacy

notices. High bounce rates directly throttle email throughput, which

blocks contact publication and prevents us from realizing value from

person data.



**Automated AI inference** **per record under management**



[Currently in build phase - project \~3mo new.]{.underline} [[Shared

Services]{.underline}](https://docs.google.com/presentation/d/1g9504nNv6Fe_jE_SW5MebFgoJPZ1lzHB4E9KETn1bk8/edit?usp=sharing)

enables net-new data quality capabilities (API, libraries) within

applications like GTM Studio. Customers will be able to [[normalize,

validate,

classify]{.underline}](https://docs.google.com/spreadsheets/d/1DrFNzxI2i9aSfnQ5wRWrZDnqwZsfyZJ-tcOBm6MK-c0/edit?usp=sharing),

etc attributes to ZI standards via these suite of services---at scale,

on-demand. This infrastructure drives automated AI inference per record

under management, allowing customers to continuously improve their data

quality rather than relying on one-time enrichment.



#### **Key Learnings**



**Email

[[Complexity]{.underline}](https://docs.google.com/document/d/18IITxJjHynyj4rV4SvbrcARIRP0BqBhb16v5YsBd0W0/edit?usp=sharing)

& Regulatory Requirements**: EU, Canadian, and Brazilian laws---plus a

growing list of countries---require contact notification and opt-out

mechanisms. Publishing millions of net-new contacts demands \<3% hard

bounce rates, spam trap removal, and predictable send rates. Failure

risks Spamhaus blacklisting our IPs/domains, blocking contact

publication entirely. Long-term business continuity requires sustained

email data quality.



**Sales Demand vs. Engineering Resourcing Gap**: Strategic accounts (Rob

Lotterman\'s org) are requesting Shared Services collateral for customer

conversations with Amazon, ServiceNow, and Walmart at Dreamforce to

address ongoing data quality pain. However, data engineering leadership

cannot commit to a concrete start date for development. We have

validated customer demand, have excited sellers, and blue ocean

opportunity---but lack the engineering resources to capitalize.



**RingLead + Shared Services Requires Cross-Org** **Alignment**: There

is immense opportunity if the data org ([[Brandon

Tucker]{.underline}](mailto:brandon.tucker@zoominfo.com), Shared

Services---15 years of ZI data quality IP) and RingLead ([[Sneh

Kakileti]{.underline}](mailto:sneh.kakileti@zoominfo.com), CRM-focused

capabilities) work collaboratively rather than in silos. Together, we

can deliver comprehensive data quality infrastructure: normalization,

enrichment, classification, validation, and de-duplication across all

entity types. This requires product leaders and organizations to align

on a unified strategy, not compete for territory. We have nearly 2

decades of combined IP to beat Clay by getting data quality as a feature

in Studio and Copilot right, and in the hands of DaaS. We need to

aggressively work together to beat our common enemy - not have excessive

disputes internally that last more than 1 day (time being set up with B

and S to address for the week of Oct 13).



#### **Hypotheses & Results**



**H 1 - Email Throughput Constraints:** Low email throughput and growing

unpublished contact backlog stemmed from our ESP\'s throttling to avoid

Spamhaus listings. **Result:** ESP caution was justified by *historical*

poor-quality sends. Since then, we\'ve systematically improved email

quality: added two validation vendors, deployed threat detection to

remove spam traps, eliminated high-bounce email generation (previously

5x worse than CN contacts), and built an EU backlog delivering at \~95%.

**We can now clear the backlog**---the infrastructure supports higher

throughput given recent DQ investments. Long-term challenge remains

maximizing email coverage through expanded validation capabilities.



**H2 - Enterprise Customer Want Better Data Quality Tools:** Sellers

would embrace Shared Services as a differentiated offering---enabling

customers to maintain ongoing 1P data hygiene with minimal cost, setup,

and implementation complexity. **Result**: Validated through sales

kickoffs with account owners managing our largest strategic accounts

(Amazon, IBM, ServiceNow) under Ryan Smit and Rob Lotterman. Sellers

immediately requested collateral to initiate customer conversations,

confirming strong commercial interest.



As i know that many of my customers would benefit from \[Shared

Services\]. As you well know - Amazon would massively benefit, and would

like \[Shared Services\] to be a possible discussion topic for our

Dreamforce attendees from AWS next month - **Mike Fawkes, Amazon account

owner** (Slack DM, Sept 24, 2025)







**H3** - **Over-Engineering NeverBounce:** Reducing SMTP calls for

NeverBounce would reduce reliance on proxy providers and harden the

service from IP blocking. **Result**: Confirmed - WRONG! Reducing SMTP

calls for email validation decreased valid rates from [[97%

(2021]{.underline}](https://docs.google.com/presentation/d/1XxaOknFvCIDL5NbpyKK_m2ZzuIIveCBQ8RoJSY7a_9s/edit?usp=sharing))

to

[[now]{.underline}](https://10ay.online.tableau.com/t/discoverorgllc/views/EmailHealthDashboard_16492954457490/EMAIL_HEALTH_DASHBOARD)

only 93%. In H1 we will expand proxy providers to increase SMTP calls.



#### **Go-forward Changes & Plan**



**Shared Services:** Deliver the infrastructure required to stand up an

Address Normalization, Address Parsing, Phone Service, and Email

Validation Service for App (GTM Studio) and DaaS consumption. Success

would look like giving Studio the capabilities to *normalize customer

provided addresses* to the "ZI way" like we have in SalesOS, *allow

customers to validate, normalize, categorize phone numbers*, and

*validate their emails*(valid, invalid, etc) inside of the application.

As we move into H1 and H2 2026, we will expand this functionality to

more attributes and verbs. Building the roadmap beyond Q3-Q4 2025

currently. We expect this roadmap to change as we get more feedback and

release functionality.



**Email Validation:** We likely need long term software engineering

investments made into email validation that will support the business

and legal needs of our business to send privacy notices at scale. For

brevity's sake, please see [[Solving Privacy Notice Delivery and Contact

Publication Constraints (Data

Org)]{.underline}](https://docs.google.com/document/d/18IITxJjHynyj4rV4SvbrcARIRP0BqBhb16v5YsBd0W0/edit?usp=sharing).



#### **Leveraging AI**



**1. Prototyping Shared Services Vision** To shift thinking beyond

internal engineering efficiency toward Shared Services as a \>\$100M ARR

product line, I used Cline to prototype data quality capabilities within

GTM Studio. This tangible demo made the business case clear: Shared

Services could fuel Studio growth while solving recurring customer data

quality pain points---eliminating lengthy conceptual debates with

engineering leadership.



*[Demo Video:]{.underline}* [[\[READ THIS\] Shared Services Product

Documentation]{.underline}](https://docs.google.com/document/d/1mfm6yLn0RRDsqxHDzv4wocpp0l0MEcgUzR8NyjnGuFY/edit?tab=t.a01g0zomm2pb)



**2. Documenting Email Infrastructure Complexity** After interviewing

stakeholders across data engineering, MarOps, privacy, and NeverBounce,

I used Chorus and Claude to iterate through 40+ versions of our email

infrastructure documentation. This AI-assisted refinement clarified a

complex, cross-functional problem and aligned data product and

engineering teams---eliminating the need for repeated justification of

email validation\'s business criticality and regulatory requirements.

*[Doc: [Solving Privacy Notice Delivery and Contact Publication

Constraints (Data

Org)](https://docs.google.com/document/d/18IITxJjHynyj4rV4SvbrcARIRP0BqBhb16v5YsBd0W0/edit?usp=drive_link)]{.underline}*



**3. Building Service Inventory with Copilot** Traditional engineering

ticket-based discovery proved too slow (2+ sprint delays, incomplete

deliverables). Instead, I used GitHub Copilot to directly analyze

codebases across Company, Person, and WDA teams, systematically

documenting existing services, capabilities, and gaps. The resulting

Service Inventory (August 2025) became our strategic roadmap foundation,

identifying \"quick win\" opportunities where existing business logic

only required API wrappers versus ground-up development.



*[Inventory (used to expedite roadmap + prioritization convo): [Service

Inventory List (Aug

2025)](https://docs.google.com/document/d/1ahiuM-9fbnB0h0FAVNoawB2aAmuc0yMXb6ZEEi7YB0k/edit?usp=sharing)]{.underline}*



Moving into Q4, I\'ll continue using AI for complex documentation,

prototyping to drive alignment on early-stage initiatives, and building

an agent for email/phone validation. (still tinkering here).

