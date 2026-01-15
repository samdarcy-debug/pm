---
id: learnings-2025-043
title: Q3 2025 Learnings Memo - Brett Elliot
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/brett-elliot]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



1.  Northstar: Converting Actions per User per Month



2.  Driver: Joint ZIM + Copilot Customer Activation



#### **Key Learnings**



- Visitor Resolution Service now deployed across almost all ZI

  applications, enabling centralized identity graph updates. (Match

  Service integration in progress.)



- The Average 30D Visitor Resolution Rate of WebSights is 2.18% which

  might seem low, but it's pretty incredible that we can resolve 2% of

  random internet website traffic to people in our database. The VRR of

  the bidder is higher: we can resolve 16% of all bid requests to a

  person in our database (because ad exchanges prioritize sending us

  requests from devices we have cookie synced with).



#### **Hypotheses & Results**



- We believed that switching the logic inside the Visitor Resolution

  Service to identify people before companies will double the Visitor

  Resolution Rate.



  - After the switch, the average 30D VRR tripled, going from 0.7% to

    2.18%.



- We believed Enhanced Visitor Resolution (EVI) would double the VRR for

  tenants that enabled it.



  - Long term results (3 months) show that the VRR for tenants with EVI

    enabled is 3.17%, a 50% increase over the 2.12% VRR for tenants

    without EVI.



- We believed that we could deliver retroactive intent by solving a hard

  compute problem and enabling new topic intent forecasts in minutes,

  not weeks.



  - The new UI enables iterative creation of new topics and keywords and

    get volume estimates in minutes instead of weeks.



#### **Go-forward Changes & Plan**



- International advertising



  - Data deletion and other data compliance enhancements



  - Consent string and browser signal handling in the bidder



  - Country specific data and compliance features



- Agentic Runtime



#### **Leveraging AI**



- I write a lot of SQL and use AI to help there.



- Sometimes I need to make UI screens, and I have used AI to wireframe

  them up.



- I use AI to find holes in my PRDs and make them cleaner, shorter, and

  more to the point.

