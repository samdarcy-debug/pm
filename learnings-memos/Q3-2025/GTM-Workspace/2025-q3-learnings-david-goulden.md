---
id: learnings-2025-025
title: Q3 2025 Learnings Memo - David Goulden
type: doc
status: approved
team: gtm workspace
owner: '[[teams/gtm workspace/_people/david-goulden]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- gtm workspace
related: []
---
## Learnings Memo - David Goulden - Q3 2025



#### **Metric Alignment**



- \# Converting Actions per User per Month



  - Whitespace recommendations aim to get better suggestions for

    prospects in front of users.



- \[TTV\] Time to first aha moment per user



  - Admin defined territories aim to enable Admins to pre-configure the

    system better for new users.



  - Priority Accounts should aggregate recommendations and accounts from

    CRM to populate a users' feed.



  - New source, Calendar events, should enable faster time to initial

    value by generating initial target accounts when calendar first

    connected



#### **Key Learnings**



#### **Key Learnings in Territories**



- Whitespace prospecting is more complex than just serving up relevant

  companies in the feed. After configuring Admin Defined Territories,

  and seeing 200-300% better conversion ("user adds Target Account") we

  see that the ongoing retention is not better than user-defined. That

  points to a mix of downstream issues ranging from: users don't know

  how to prospect well, or don't get enough decent signals, or Team

  Leads want to co-review and coach on signals, recurring issues we have

  heard for Copilot v1.



- Additionally, territory rules are experimental: teams are trying out

  rules, getting feedback from users and tweaking accordingly.



- We are learning that larger companies see consistent turnover in sales

  team personnel, leading to a need to update Territories on a weekly

  basis. As we do not yet offer any public APIs for integrators to build

  their own middleware and the solution delivered by R&D for uploading

  lists of updates is too technical. We will need to provide a selection

  of simpler templates as well as create APIs.



- We have also uncovered that customers that heavily use Territories in

  Salesforce will need a different method of associating existing CRM

  Accounts to Users, similar to what we have planned for Account Team

  object. That will need to sync into Target Accounts.



- We also see that customers expect more synergy between features. A

  good start is using Territories for Admins to activate GTM Workbooks,

  but most of our customers have very autonomous users who are using

  Search and Intent, and want to use Territories as default searches

  there. With the rumours of classic Search going into maintenance mode

  without a replacement, it's unclear how we might provide a solution.



**Key Learnings in Target & Priority Accounts**



- We are still trying to understand the way forward to getting a single

  solution which can solve for backwards compatibility, and also unlock

  the GTM DM CRM data which we need to query to unlock more types of

  account book relationships.



- Priority Accounts APIs were not centralized and needed 4 different

  endpoints to understand a user's "target market". We are bringing them

  together.



- Whilst we added options for users to Dismiss / Hard Dismiss we did not

  provide a way for users to be able to review & manage which companies

  they've actively blocked as being not interesting resulting in

  questions from some users about how to manage their Target Accounts

  list.


