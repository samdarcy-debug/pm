---
id: learnings-2025-012
title: Q3 2025 Learnings Memo - Rituparna Das
type: doc
status: approved
team: data
owner: '[[teams/data/_people/rituparna-das]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- data
related: []
---
#### **Metric Alignment**



#### My work has contributed to the Data ROI north star metric. My work has delivered transformative improvements to ZoomInfo\'s core data assets through a comprehensive email and phone coverage enhancement initiative that directly strengthens our competitive positioning. By scaling personal email coverage by 20.5M records (including 1.6M decision makers) and expanding mobile phone coverage by 2.6M records (200K decision makers), I\'ve substantially enhanced our data depth for decision-maker identification and multi-channel outreach capabilities. Most critically, this initiative enabled advanced person-level identification by providing essential email matching data for our Visitor Resolution System (VRS), allowing us to de-anonymize website traffic and convert anonymous visitors into identifiable business professionals. The strategic integration of freemails like Gmail as matching keys through observed behavioral events, cookies, and form submissions has revolutionized our device-to-person identity mapping capabilities, directly supporting ZoomInfo\'s competitive differentiation in data accuracy and coverage while improving overall platform ROI for customers.



#### Simultaneously, I spearheaded the expansion of department classification for international contacts, solving a critical discoverability gap that was preventing customers from accessing valuable data assets we already possessed. Despite having equivalent contact coverage to competitors like Cognism, our international contacts weren\'t surfacing in user searches due to missing department classifications---a fundamental problem since department filtering is the primary search criterion used by DaaS consultants. By increasing department coverage from 57% to 62% with additional improvements planned, I\'ve unlocked significant revenue potential by converting previously \"hidden\" data assets into monetizable, searchable records that directly enhance customer satisfaction and platform utility. This work addresses two critical pillars of ZoomInfo\'s value proposition---data completeness and discoverability---while strengthening our competitive position against key rivals in the international market and enabling customers to reach previously unidentifiable prospects.



#### **Key Learnings**



1.  I**nternational Data Drives Enterprise Revenue**: High-value

    customers like Oracle (\$15M TCV) are specifically seeking enhanced

    international contact capabilities, particularly around title

    classification efforts that properly handle accent marks and special

    characters in international titles, demonstrating that international

    data quality improvements directly correlate with enterprise deal

    value and customer retention.



2.  **Precise Location Data Enables Strategic Business Operations**:

    Accurate physical location data has become mission-critical for

    executive decision-making in the remote work era, enabling seamless

    CRM account alignment for location-based structures, optimal

    regional representative matching, and enhanced product features like

    Copilot\'s time zone functionality---ultimately supporting

    high-impact use cases such as targeted roadshows for prospects in

    specific geographies like London, UK.



3.  **Multiple Employment Representation Requires Sophisticated Data

    Prioritization:** Current job prioritization logic based on latest

    start dates often elevates part-time or self-employment roles over

    more relevant full-time positions, creating a critical gap in

    Copilot and SalesOS functionality that customers actively inquire

    about, highlighting the need for more nuanced employment data

    sorting algorithms that better reflect professional hierarchy and

    relevance.



4.  **Strategic Focus on High-Impact Issues Over Edge Cases Maximizes

    ROI:** While data quality issues like 14K \"Stay at Home\" titles

    exist as edge cases, effective product management requires

    prioritizing initiatives with broad customer impact over low-volume

    anomalies, as ZoomInfo\'s sorting and boosting mechanisms already

    minimize user exposure to these outliers, making large-scale

    improvements more valuable than perfecting rare scenarios.



#### **Hypotheses & Results**



1.  **Business Email Generation Enhancement Through Data Science:**

    Investing in advanced email generation mechanisms using expanded

    training datasets from our gold contributory network and ESP data

    could increase coverage by at least 5% while pushing deliverability

    from our current industry-leading 97% to nearly 99%, helping us

    surpass Cognism (96%) and Apollo (94%) while maintaining our

    superior quality standards through multi-layered validation and spam

    prevention protocols.



2.  **Board Member Data Specialization for Enterprise Clients:**

    Developing comprehensive board member data acquisition,

    classification, and profiling capabilities could unlock significant

    revenue opportunities, as evidenced by our successful Barclays board

    of directors data cube delivery and ServiceNow\'s expressed

    interest, requiring improved title classification to properly

    distinguish board affiliations from traditional employment

    relationships.



3.  **International Data Enrichment and Coverage Expansion for Customer

    Acquisition and Upsell:** Refining our classification of

    international titles with foreign language markers and special

    characters could significantly enhance customer acquisition and

    upsell potential by making our existing international contact

    database more discoverable and valuable, directly addressing the

    synthesized customer feedback patterns from the past year that

    highlight this as a key differentiator in enterprise deals.

    Continuing vendor onboarding initiatives could deliver a 30%

    increase in mobile phone coverage for international contacts,

    addressing a critical gap in multi-channel outreach capabilities and

    strengthening our competitive position in global markets where

    mobile-first communication is increasingly prevalent.[[International

    Data: Customer

    Feedback]{.underline}](https://docs.google.com/document/d/15e9ZLGkUhnbRS2VkDaoiQtsTbwODiW9T4lNy2b0Cg5o/edit?tab=t.0)



#### **Go-forward Changes & Plan**



1.  International Data Improvements: Emails, mobiles, and classification

    coverage



2.  Board of Members acquisition, classification and profiling: Better

    ingestion process, and enhanced capabilities fpr title

    classification to identify these titles properly and PTI to profile

    these under board member affilayions only.



3.  Email Generation Improvements: Find out profiling and pipeline

    improvements to validate and attach more emails, while continue work

    on improving the data science email generation.



4.  Location Improvements to get precise nearest office locationfor the

    contacts who potentially work from office (use case such as I want

    to get the contacts who work at an office location so that I can

    expand the customer base for my internet provider services. I serve

    in a given location in a given building but want to know how can I

    get hold of the people who work in that are and/or the same building

    other offices.



#### **Leveraging AI**



1.  Voice of Customer Tool for customer insights, which customers are

    happy or are at a risk of churn



2.  ZI Chat: Snowflake, Meeting Insights, Release Notes generator, Recap

    my Day



3.  Built an executive moves agent which gathers data for all the

    executive move for given companies, it can also help to identify

    email domains for the given companies based on public data. This has

    helped me with the email generation analysis, and to establish

    employment/left company confirmation. I have provided this to

    researchers to use as well.



Plan for Q4:



1.  I plan to build an agent on top of production data report to explain

    more about the trends in the data. This would utilize traceability

    data in PTI, and would enable users to ask:" I see a dip in the

    number of published contacts from 9/21/2025 until now, can you tell

    me why?"



2.  Keep utilizing ZI chat for creating PRDs, product initiative plans

    and analysis.

