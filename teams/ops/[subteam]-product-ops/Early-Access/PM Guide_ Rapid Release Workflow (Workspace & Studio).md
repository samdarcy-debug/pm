# Process

# **Early Access Release Process: GTM Studio & Workspace**

**Last Updated:** Jan 2026  
 **For:** GTM Studio, GTM Workspace PMs only

---

## **What Early Access Is & Why It Helps You**

We're releasing new features every week for GTM Workspace and GTM Studio, which is great for customers but tough on downstream teams who need time to learn and train on updates. Going forward we will shift to an “Early Access” \- *opt-in,* internal users only to start, where we:

* **Ship fast** to Early Access  
* **Ship very deliberately** to GA

You get usage data and feedback BEFORE customer release. Catch issues early, confirm features are valuable, internal teams get time to use it first. Less time firefighting, more time building.

This workflow gives you a simple way to validate features with real users before broad release, while automatically generating the materials everyone needs  
---

## **Customer-Facing Features Get a Feature Flag and Start in Early Access**

**Default:** Customer-facing features deploy behind feature flags. This includes anything that changes what users experience, what data they can access, or how the system behaves. Think about:

* Inputs: What users can query/filter/search  
* Outputs: How the system responds

**Why:** So you can control who sees it (EA users first, then all customers) and turn it off instantly if something breaks.

**Exceptions (skip feature flag \+ Early Access):**

* Bug fixes, Hot fixes, Infrastructure-only changes

**Rule of thumb**: “Does this impact how the user experiences the product?”

* YES → Early Access (could be priority OR changelog)  
* NO → Direct to GA 

**How to set up flags:** Engineering creates them. [Flag naming convention](https://discoverorg.atlassian.net/wiki/spaces/ZE/pages/153820038624/Flag+Naming+Convention) | [LaunchDarkly docs](https://discoverorg.atlassian.net/wiki/spaces/ZE/pages/153819907624/LaunchDarkly+Documentation) 

---

## **Priority Release vs. Changelog**

We focus our validation effort and attention on higher impact features:

**Priority Release** \= Bigger impact features:

* You create: Demo video \+ feature pack \+ release note  
* You validate: user interviews \+ monitor usage  
* You present: Go/No-Go case to DAIs before GA

**Changelog** \= Smaller improvements:

* You create: Release note only  
* You validate: Passively monitor for issues  
* You present: Nothing. Auto-”Go” unless problems get flagged

**How we decide which is which:**

In Monday's meeting, Prod Ops comes in with a preliminary rating for each feature on two things:

**1\. Workflow Impact** \- How much do customer workflows change?

* **High:** Core workflow changes, feature moved, demo flows need updating  
* **Medium:** New capability that impact workflows, but not fundamentally  
* **Low:** One more option in familiar place

**2\. Customer Value** \- How much would customers want to know about this?

* **High:** You'd announce to ALL customers (competitive gap, top pain point)  
* **Medium:** Meaningful for specific segments  
* **Low:** Quality of life improvement

**The rule:**

* **Medium or High on either** → **Priority Release**  
* **Low on both** → **Changelog**

---

## **Your Weekly Workflow**

### **Monday: Determine What Goes Into EA**

**When:** Leads meeting, Monday (each product separately)

**What happens:**

* Prod Ops sends list in advance, and shows list of what deployed last week  
* We decide: EA or not ready? Priority or Changelog?

---

### **Tuesday: Create Your Materials (Due by 5 PM ET)**

**Open [Rapid Release Agent](https://chat.zoominfo.co/127/agents/5535) \- it walks you through everything**

**If you have "Priority Release":**

1. Record 3-5 min demo in Chorus (agent gives you script)  
2. Agent generates: release note, feature pack, LRT ticket  
3. Review and approve, including what success looks like for Early Access  
4. **Time: \~20 min per feature**

**If you have "Changelog":**

1. Agent generates: release note, LRT ticket  
2. Review and approve  
3. **Time: \~5 min per feature**

**Setup requirement:** Make sure Atlassian \+ Google Sheets integrations are connected in ZI Chat or the agent can't create your LRT ticket

**You're done when:** Agent confirms everything's submitted

**Miss this deadline?** Your feature gets pushed to next week.

---

### **Wednesday: Turn On Your Feature (5 min)**

**Two steps, same for all features:**

**1\. Turn on LaunchDarkly flag** to target Early Access users:

* Go to your flag → Environment \= production  
* Add Rule → Target Segment  
* Pick "Early Access Product Releases \- \[Your Product\]"  
* Serve \= TRUE/ON  
* **Visual guide:** [LaunchDarkly documentation](https://discoverorg.atlassian.net/wiki/spaces/ZE/pages/153819907624/LaunchDarkly+Documentation)  
* [More details below](#bookmark=kix.wx5jrrk1mavc)

**2\. Post to EA Slack**:

* Priority: You post individually with demo/materials \- Agent will have it generated at the end  
* Changelog: Prod Ops bundles all changelog items in one post  
* Studio: [\#intl-early-access\_gtm-studio](https://zoominfo.enterprise.slack.com/archives/C0A3TVDME7M)  
* Workspace: [\#intl-early-access\_gtm-workspace](https://zoominfo.enterprise.slack.com/archives/C0A3WU1N2DB)

**You're done when:** Flag is on, Slack post is live

---

### **Wed-Tue: Gather Feedback**

**If you have a Priority Release we *recommend*:**

* Run 2-3 interviews (record in Chorus) \- [Interview scripts](https://claude.ai/chat/2d1be599-03c6-47f0-b7d8-4c9781fea567#interview-scripts) below  
* Monitor your EA Slack thread  
* Track usage numbers

**If you created Changelog:**

* Monitor your EA Slack thread

**Goal:** Answer "should we release this to customers?"

---

### **Next Tuesday: Go/No-Go Meeting (3:30 PM ET)**

There is a standing Go/No-Go Meeting with DAIs each Tuesday. Each week you have option to put any EA feature up for Go/No Go

**If you created Priority Release materials:**

**Monday EOD:**

* Slack bot asks if you're ready (yes/no)  
* If yes:   
  * Use [Go/No-Go Report Agent](https://chat.zoominfo.co/127/agents/6268) to build your case \- helps consolidate   
    * Update [this tracker](https://docs.google.com/spreadsheets/d/1EjcDuS3IdIfTuaQbZQdWIOtyfVPK_qu8WNLAgIzwMaI/edit?gid=0#gid=0) with your justification  
  * OR just fill in the PM justification in [this tracker](https://docs.google.com/spreadsheets/d/1EjcDuS3IdIfTuaQbZQdWIOtyfVPK_qu8WNLAgIzwMaI/edit?gid=0#gid=0)

**Tuesday meeting:**

* Present your case to DAIs  
* They decide: Go or No Go

**If you created Changelog:**

* Auto-approved for GA, unless issues were found

---

### **Following Tuesday: Feature Goes Live to Customers**

Your LRT ticket helps: Enablement inform the field & ProdOps generate external comms 

You: Turn on the flag for General Availability (GA) in LaunchDarkly

---

## **What Actually Matters**

**Don't skip Monday meetings.** That's where we decide what is going into Early Access

**Don't miss Tuesday 5 PM deadline.** Or you're pushed to next week.

**If you created Priority Release materials, do the validation.** You can't present Go/No-Go confidently without the signals

**If something breaks in EA, flag it immediately.** Don't wait for Go/No-Go meeting.

---

## **Quick Answers to "What If..."**

**"I don't know how to use the agent"**  
 It's conversational. Open it, tell it what feature you're working on, it'll walk you through. If it breaks, Slack Product Ops.

**"I missed Tuesday deadline"**  
 Tell AJ Belen. Feature gets pushed to next week.

**"Nobody volunteered for interviews"**  
 DM 3-4 people directly: "Need 15 min this week to test \[feature\]. Free Thursday?"

**"My feature broke in EA"**  
 Post in EA Slack thread immediately. Flag in tracker. We'll decide next steps.

**"I'm not ready for Go/No-Go Tuesday"**  
 Tell AJ Belen Monday AM. Push to next week. Don't present unprepared.

**"Agent won't create my LRT ticket"**  
 Check your ZI Chat integrations: Atlassian \+ Google Sheets must be connected.

**"I forgot to record demo in Chorus"**  
 Agent needs Chorus transcripts. Record there or you'll have to upload transcript manually.

**"Which LaunchDarkly project am I in?"**  
 The segment will be created in the same project as the flag (in production only). If unsure, ask in Monday's meeting.

---

## **Appendix**

### Launch Darkly

Locating the right segment should be very easy:

1. Go to your flag link in LaunchDarkly. Environment \= production  
2. Click Add Rule \> Target Segment  
3. Set the rule to:   
   1. Operator \= is in   
   2. Segments \= Early Access Product Releases \- \[Product\] (Project) \*  
   3. Serve \= TRUE/ON  
4. Review and Request Approval

The Default rule should be FALSE/OFF at this stage  
![][image1]  
\*Note that the specific segment name will vary based on the project you are in. The naming convention is “Early Access Product Releases \- Product (Project)”.

### List of All Segments by Project

If you are having trouble locating the segment, below is a table with all segments available, by Project and Product

| LD Project Key | EA Segment (Workspace) | EA Segment (GTM Studio) |
| ----- | ----- | ----- |
| zi-for-sales | [Early Access Product Releases \- GTM Workspace (ZI for Sales)](https://app.launchdarkly.com/projects/zi-for-sales/segments/early-access-product-releases/targeting?env=production&selected-env=production)  early-access-product-releases | [Early Access Product Releases \- GTM Studio (ZI for Sales)](https://app.launchdarkly.com/projects/zi-for-sales/segments/early-access-product-releases-gtm-studio-zi-for-sales/targeting?env=production&selected-env=production) early-access-product-releases-gtm-studio-zi-for-sales |
| agentic-platform | [Early Access Product Releases \- GTM Workspace (Agentic Platform)](https://app.launchdarkly.com/projects/agentic-platform/segments/early-access-product-releases-phase-1-dai/targeting?env=production&env=test&selected-env=production)  early-access-product-releases-phase-1-dai | [Early Access Product Releases \- GTM Studio (Agentic Platform)](https://app.launchdarkly.com/projects/agentic-platform/segments/early-access-product-releases-gtm-studio-agentic-platform/targeting?env=production&env=test&selected-env=production) early-access-product-releases-gtm-studio-agentic-platform |
| sales-hub | [Early Access Product Releases \- GTM Workspace (SalesHub)](https://app.launchdarkly.com/projects/sales-hub/segments/early-access-product-releases-phase-1-dai-sales-hub/targeting?env=production&selected-env=production) early-access-product-releases-phase-1-dai-sales-hub | [Early Access Product Releases \- GTM Studio (SalesHub)](https://app.launchdarkly.com/projects/sales-hub/segments/early-access-product-releases-gtm-studio-sales-hub/targeting?env=production&selected-env=production) early-access-product-releases-gtm-studio-sales-hub |
| zi-for-marketing | [Early Access Product Releases \- GTM Workspace (ZI for Marketing)](https://app.launchdarkly.com/projects/zi-for-marketing/segments/early-access-product-releases-gtm-workspace-zi-for-marketing/targeting?env=preprod&env=production&selected-env=production) early-access-product-releases-gtm-workspace-zi-for-marketing | [Early Access Product Releases \- GTM Studio (ZI for Marketing)](https://app.launchdarkly.com/projects/zi-for-marketing/segments/early-access-product-releases-gtm-studio-zi-for-marketing/targeting?env=preprod&env=production&selected-env=production) early-access-product-releases-gtm-studio-zi-for-marketing |
| ring-lead | [Early Access Product Releases \- GTM Workspace (RingLead)](https://app.launchdarkly.com/projects/ring-lead/segments/early-access-product-releases-gtm-workspace-ring-lead/targeting?env=test&env=production&selected-env=production) early-access-product-releases-gtm-workspace-ring-lead | [Early Access Product Releases \- GTM Studio (RingLead)](https://app.launchdarkly.com/projects/ring-lead/segments/early-access-product-releases-gtm-studio-ring-lead/targeting?env=test&env=production&selected-env=production) early-access-product-releases-gtm-studio-ring-lead |
| chorus | [Early Access Product Releases \- Phase 1: DAIs (Chorus)](https://app.launchdarkly.com/projects/chorus/segments/early-access-product-releases-phase-1-dai-chorus/targeting?env=staging&env=dev&env=production&env=staging-v2&selected-env=production) early-access-product-releases-phase-1-dai-chorus | [Early Access Product Releases \- GTM Studio (Chorus)](https://app.launchdarkly.com/projects/chorus/segments/early-access-product-releases-gtm-studio-chorus/targeting?env=staging&env=dev&env=production&env=staging-v2&selected-env=production) early-access-product-releases-gtm-studio-chorus |
| engage | [Early Access Product Releases \- Phase 1: DAIs (Engage)](https://app.launchdarkly.com/projects/engage/segments/early-access-product-releases-phase-1-dai-engage/targeting?env=dev&env=production&selected-env=production) early-access-product-releases-phase-1-dai-engage | [Early Access Product Releases \- GTM Studio (Engage)](https://app.launchdarkly.com/projects/engage/segments/early-access-product-releases-gtm-studio-engage/targeting?env=dev&env=production&selected-env=production) early-access-product-releases-gtm-studio-engage |

---

### **Interview Scripts**

**When to use:** Only if you created Priority Release materials

**How many:** 2-4 interviews depending on feature impact

#### **Core Users (AEs, AMs, RevOps) \- 10 min**

*Record in Chorus*

**Setup (1 min):**  
 "Thanks for testing \[feature\]. Critical feedback helps more than praise. Be direct."

**Questions (8 min):**

1. "Walk me through how you used it. What were you trying to do?"  
2. "Better, worse, or same as before?"  
3. "Any bugs, confusing parts, friction?"  
4. "If we released next week, how often would you use it?"  
5. "Would a customer discover this on first login? How?"

**Commitment Test (1 min):**

6. "1-5, how disappointed if we DON'T release?" (1=don't need, 5=would miss)  
7. "Should we release? Yes, no, or not yet?" If not: "What ONE thing must change?"

---

#### **Sell-Side (SCs) \- 10-15 min**

*Record in Chorus*

**Setup (1 min):**  
 "Thanks for testing \[feature\]. Critical feedback helps more than praise. Be direct."

**Questions (10 min):**

1. "Did you test it? What did you do?"  
2. "Any bugs, confusing parts, friction?"  
3. "Would a RevOps leader discover this on first login? How?"  
4. "Pick ONE specific customer in your pipeline. Would they use this? How often?"

**Commitment Test (2 min):**

5. "1-5, how disappointed if we DON'T release?"  
6. "Should we release? Yes, no, or not yet?" If not: "What ONE thing must change?"

---

### **Levels of Early Access**

There are two levels of Early Access that you can use. Remember the purpose is not to have a set time requirement in either, but to act as a quality gate for release items before they go into GA.

**Level 1: DAIs** \- The Product VPs want first access to any new features

**Level 2: Opt-in EA** \- Broader internal access after DAI approval (will eventually expand to customer opt-in as well)

**Level 3: GA** \- The full release

It's up to the team's discretion (and DAI) to determine what level is needed for each release.

---

### **Go/No-Go Report Template**

**Only needed if you created Priority Release materials**

The [Go/No-Go Report Agent](https://chat.zoominfo.co/127/agents/6268) generates this for you. You provide:

* Usage data you pulled  
* KPI results  
* Your take on the interviews/feedback

Agent pulls:

* Slack feedback from EA thread  
* Chorus interview transcripts

**Template structure:**

---

# **Go/No-Go: \[Feature Name\]**

**PM:** \[Name\]  
 **GA Date (if approved):** \[Next Tuesday\]  
 **EA Period:** \[Dates\]

## **Feature Summary**

\[50 words: What it is, why it matters\]

## **Executive Summary**

**Does it work?** \[Bugs fixed/remaining?\]

**Will it be adopted?** \[User excitement? Usage numbers?\]

**Disappointment if not released?** \[Interview signal\]

**Recommendation:** \[Go/No-Go \+ why in one sentence\]

## **Early Access Performance**

\[150 words: User sentiment, value delivered, KPIs\]

## **Risks & Mitigations**

\[100 words: Concerns, what's not perfect, post-GA plan\]

## **Appendix**

* Bugs found  
* Usage metrics  
* Slack feedback summary  
* Interview links/notes  
* GTM plan (if needed)

# Early Access Criteria

**Early Access Criteria**

Early Access will fundamentally change the way we are viewing releases for Platform and Infrastructure changes. The idea is we are building one system that works seamlessly together, which means we should be testing the value delivered across that system before it goes out to customers. 

**INCLUDE in Early Access**

Anything that changes what users experience, what data they can access, or how the system behaves. Think about:

*Inputs*: What users can query/filter/search

*Outputs*: How the system responds

**Specific examples:**

* New agents, sub-agents, or tools users interact with  
* New data sources (MCP servers, integrations)  
* New or changed API endpoints  
* Changes to inputs (new filters, query capabilities)  
* Changes to outputs (response types, artifacts, content generation)  
* Architectural changes to agent routing or decision-making  
* Prompt refactoring that could change behavior

**EXCLUDE from Early Access**

Pure backend changes that are completely transparent to users.

**Specific examples:**

* Database migrations (if truly transparent)  
* Storage optimizations (ex. MongoDB → BigTable)  
* Performance improvements with no behavior change  
* Model updates (IF no quality/behavior change)  
* Internal refactoring with no user impact  
* Build/deployment infrastructure changes

**When in Doubt**  
Include it in Early Access. Better to over-include initially than miss something that causes customer issues.

**Quick Decision test:** “Does this impact how the user experiences the product?” ("Could an *expert* user notice this change?")

* YES → Early Access (could be priority OR changelog)  
* NO → Direct to GA 

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA3wAAAGICAYAAAAaiOIEAABcQ0lEQVR4Xuzdd3BUV6Lv+zm3Xt1/3qu6t17VPXXr1Kl37jlzZuZM8jiNs8fZ4zTOEQdsko2xwSYZMDljMCbYRIMxOWeMycmAyTkHkTNCQkgiCNbTb7XXZvdSS2oJhVb391P1q+7ee3drdzeI/rHW3v2r3EtXDCGEEEIIIYSQ5Muv/AWEEEIIIYQQQpIjFD5CCCGEEEIISdJQ+AghhBBCCCEkSUPhI4QQQgghhJAkDYWPEEIIIYQQQpI0FD5CCCGEEEIISdJQ+AghhBBCCCEkSUPhI4QQQgghhJAkDYWPEEIIIYQQQpI0FD5CCCGEEEIISdJQ+AghhBBCCCEkSUPhI4QQQgghhJAkDYWPEEIIIYQQQpI0FD5CCCGEEEIISdJQ+AghhFTZrFi9zqxet8le37R1hxkxZqK9zLl4ucC2hSUrO9d8UL9JcJl28Ij5tGmrAtsRQgghVTEUPkIIIVU2Hzdsbho1b2OvT5wy07xcrYa9vJBz0S7btnNPfgHcWeB+4SxettKMmTA1uDx5Ot30HTCkwHaEEEJIVQyFjxBCSJWNCp6i67EKX9/+Q0zPvgPNzj37zY/zFpsFi3+yy2f+ON+cTs+w1z/6tJmZNWdBcHnq7Dm7rdbt2L3PjiL6P5cQQgipKqHwEUIIqbJ567265vV36tjrsQqfK4RzFiyxl+/VqW9mzJ5nWrbramrW/cQcP3nGLm/6efvgcuuOPUGJfOXNmqbaux+UaIooIYQQkkih8BFCCKmSUQnr+mVf065zD3s9VuHbvG2nWbdxq73uStyGzduD23MXLjUT8rfPzr0UXLrCt33XXjvSpymhR46dLPDzCSGEkKoQCh8hhJAqGRW3Tl/0Mm07dbelLN7Cd+jIcdO6Qzd7e9rMOYUWPjvt82xk2ichhBBSVUPhI4QQUiXTb/Aw81aND+2Uy/6Dv4+78OlMnD+v2VBs4Vu4dIUth+6xCCGEkKoYCh8hhJAqmXfrfBx1PVbhSzt01Eya9oMdqXOFr9q779uvYCiu8B07cdr06N3fjBo32T6O//MJIYSQqhAKHyGEkCoZV+Dc9ViFT9FJXQZ9NzLYftyk6fZkLEpRhU/b1vukmR1F9H82IYQQUlVC4SOEEJLUyczKMRfyi1x42dlzmQW2Kyz+fQkhhJCqFAofIYQQQgghhCRpKHyEEEIIIYQQkqSh8BFCCCGEEEJIkobCRwghhBBCCCFJGgofIYQQQgghhCRpKHyEEEIIIYQQkqSh8BFCCCGEEEJIkobCRwghhBBCCCFJGgofIYQQQgghhCRpKHyEEEIIIYQQkqSh8BFCCCGEEEJIkobCRwghhBBCCCFJGgofIYSQlEl27qUCywghhJBkDoWPEEJIymTPgaMFlhFCCCHJHAofIYSQlAmFjxBCSKqFwkcIISRlQuEjhBCSaqHwEUIISZlQ+AghhKRaKHyEEEJSJhQ+QgghqRYKHyGEkJQJhY8QQkiqhcJHCCEkZULhI4QQkmqh8BFCCEmZUPgIIYSkWih8hBBCUiYUPkIIIakWCh8hhJCUCYWPEEJIqoXCRwghJGVC4SOEEJJqofARQghJmVD4CCGEpFoofIQQQlImFD5CCCGpFgofIYSQlAmFjxBCSKqFwkcIISRlQuEjhBCSaqHwEUIISZlQ+AghhKRaKHyEEEJSJhQ+QgghqRYKHyGEkJQJhY8QQkiqhcJHCCEkZULhI4QQkmqh8BFCCEmZUPgIIYSkWih8hBBCUiYUPkIIIakWCh8hhJCUCYWPEEJIqoXCRwghJGVC4SOEEJJqofARQghJmVD4CCGEpFoofIQQQlIm+w+fKLCMEEIISeZQ+AghhBBCCCEkSUPhI4QQQgghhJAkTdyFLyMrx5w5d54QQgghhBBCSCXlbEaWyc69VKCvFZa4Cl9W9kWTe/GSAQAAAABUnqvXrtnS53e2whJX4dMDAgAAAAAq35W8q3GP8sVV+BjdAwAAAIDEoUPuCvS2GImr8GnYEAAAAACQGOKd1hlX4QMAAAAAJA6dwMXvbbFC4QMAAACAKobCBwAAAABJisIHAAAAAEmKwgcAAAAASYrCBwAAAABJisIHAAAAAEmKwgcAAAAASYrCBwAAAABJisIHAAAAAEkqqQtf74VjzP9o9KD5Vd3bSh3dX48DAAAAAFVN0ha+z6b0Mf93s4fNr9rmp8OjpU/+/fU4ejwAAAAAqEqSsvBtP74/Uvb88nYD0eP9us3z/o8CAAAAgISVlIXvf2oaZ4zSVqK0D8Uta3a/LZMAAAAAUBVUucKXk5PjLypAxaxAgStB/nvHJ8yqwzvsYx04d8LcMeijYF1VGuUr7rW6ePGiuXr1qr8YAAAAQJKo0MLXf8Ag89TTzweRCRMne1sV7Xe/v8nMnj3HXxzQsXZ+gdMo3T+1fSR6tK6QPPZ9U3Mo46T/sMF9NbWzrMybt8CcOnXaX1xm9FrFcuLECXv5zLMvmjZtO3hrS6ak719RPm/ZxkyeMtVffMOee+EVfxEAAACQEiq08LVt19G89vpbZsmSZTYycNC33lZFU9nLzDzvLw7Ys2uGCtw/tXvU/GunF803c8faS7/g+SnMF8vGRUpf24fNqfPp/upSycrK8heVqcKK8a9/8wd7uXr1GpOWdsBbWzIlff+K8k71mubbId/5i2/Y7/94s78IAAAASAkVXvjqfdQgapkrDMeOHTfjJ0wKlqenp5sFCxebvLw8cy4jI1g+c9YP5ty5c/b6lCnTotaJf7KWP3V7y5zJTDdb0naZ0xnpkdG+do+Yf/rlMqrwtS+88MmTI1rY7fyvadi8ZatZvGRpcHv1mrVm777rx/plZGSa2T/OjSpgc+fND57HrFmzze7de8zESVOC9e75637h5xh+3PnzF9pLjYodPx4ZtdNjZmdnm40bN9nXSvTaum1ycnJt4dM+/vzzarN37z67zZ49e82OnbvsdS1bu269mTN3XjAtVM9h0uSp5uDBQ/a2o/dPo3ybNm8Jli1bttzGOXz4sPnhhx+D2/rZ4fc6NzfXzJg5K2bh035MnTo9uK2CqtvXrl0LbRV5DX9aviK4LqdPn7GX4cLnvzfjxk+Ieu8AAACAZJIQhW/6jFnmTzfdaup8UM+sWbvOLv/Dn24xr7xWzdT9sL7ZuGlzsL0+vOu2pkN+WK+BufveB4N18qvPH4gqcQdOHDH7jx8y/631wybt+GF7WXdUV/PY1/XN+yO6RE3zfHNi56jH8s3etdpud++XNYNlX3T/0tx59/3m8SeescfDafTx6WeeN3+55Q4z9Lvv7TZ6Xt179DS//a8/B/f7z9/+0WzYsNFe13N69bU3zfMvvGJLlrjnf9PNf416/rXf/zC43qRpc/va1a5T175+osdUcZo2fWZQdLTObaMiqcI3aPAQ826N2vb1V3m67a/3mDvuus8+h/4DBptateva+7z0yhv2Me657yH7et9y253Bzxftj56fu6+OC3zokb+bBx9+PNjm1tvvMtXeqm6Lp3t99Nju9bnvbw+b92rWMc8+/3JU4dO2eqyatT4wQ4YOs8s0BbX6u7VMx85dg+1Ez1WP666LK4Dudvi9Eb13DRt/Frx3AAAAQLKp8ML3wouv2pE5NwqjwjFi5GizcNFie7tRk2b2w/f3w0fa29/0GxCz8KnUiNvOifrevV9G7Gp8197erj2sg/ltl0iBOXTymC06/2/7Z4LtR26cH36omLSdvozdUTFbsfJnW3Q0uqYCIRqZ0jpx5SRc1lSAwoXPefPtd6Oev8pZ+Pm74/I0irdq1Wr72knHTpGfocd0I3/ucd1r67ZxUzpd4Rs/fqIdwdNonoqVCt8f/xwpkL/53Z/s5etvvG0vNeoYdvc9D9hLlalRo8eaAwcOmkuXLtlRyUOHDtt1X/WKfIfhtm3bg9dH3OujIikqweHCF2tblULRc7ty5fqfufBrWFjhC783Kp/uMd17BwAAACSbCi98f73zPvPW2++Z9+t+ZJe5KZ2aajh12gx7jJ+mF6o0yNmzZ2MWvh5f9rJTDH3h0T1N2ZTbe9Swt+/4sqZ5a0hru+z/avGQqTW0vflH/8bB9muO7Aw/VEx227q3Bbc1Cqfnc+HCBXv7v/7wl2BKoytWKhiiaZyaoioqvbEKnwpU+Pn7he+Zf7xgL3V/N61R0zffeLO6va7HdKNV7nH12oa38Qtfw0ZN7W3RyJsKn9vWFaw/3XRbMP0zrHXopC+uUGkKp0YQl69YaW9rlO7kqVP2eqzXxxWzRx57MqrwaVTRqVHzfXvZu8/X9lL33Z+WFqyPp/CFf7ZGUvXeLVq8JHjvAAAAgGRT4YUv1pTOfv0HmptvvdNOUdTURlcURAUpVuHT6M6LL71mPm7QMFgnUYXvlxG+p7751N5+5puG5pE+H9tlKoO/7vyqqTO80w0VPo1kaQTrz3+53RYwFZHq79WycaOQbv+1zyob69dvsCUsVuHT1Mjw89c00PDzH/b9CHupxxe9dnod3CiZe0xxj6vXNryNX/j0mjtPPv2cLXyuYLl12ic9Rz1OWN+v+wfXVRIPHzliS6umsLrCpRFElS0dU+e/Piq2u3bttttpFDFc+DTi5zRvESnq7j8I9DjhAlpc4dPPCf9sTQnWe/foY08F7x0AAACQbBKi8OmDvc4YKSoYml7nTg6yZcvWmIXP8U+5HzWlMz95V6+aAXPH24I3aN4E8/+0edJup9v/p0t04SvNlE43mqYTnqxcuco8/veng3VOeH+btWgVNf1S/MIXfv7+CJ/Wbd++wxYocaVIX3khfuHTVEv32rpt/MLXuk374D4a7YtV+Nzxea54OQ0+aRxc1/F1mr6qkq64wqUypbLXq3ffmK+PO7mMnnu48OnYOscdSxhP4dPxiOJGgN06/2f77x0AAACQbBKi8OlYqqVLf7IlxxUMFTkdL6ZRn1iFT98hp1KhEakw/6QtPWZGTgzyxqDP7eV/axOZ5hmr8JXmpC06AYjOdqkSpmKlES+Ncum4Pp3MRcL7r1LzwIOP2euFFT5xz1/H0IXvLy++/Lo9yYm449DcSVL8wqeSptc2vM39DzxiS5grfNp/jTzqDJb6mbEKn44/1Nk0P2sWeR0dnQhGxUn3V8Hr3ecbO5r29Tf9g8KnoqmTxfTp2y94fcS9Pg8/+oTdT5XYcOHTY+isnJcvXza33X63XRZP4dPz0s/Q8ZDhdeH3RlNM3clb3HsHAAAAJJuEKHyjx4yzxUVFxBWMrt16mNervWPWrdsQs/CpTGgq3gd1I1M0Hf9rGXRWzk7TIiVBl+5ELrbwdX3V1B5xvfCV5msZdJITneBEUYmyZ7zMLyc6m6X76oHw/j/2+NP2rJVSVOFzz1+vi1/4VHbc1xzotdPPa9e+k73tFz7RY4S30X6pSLvCJ3rt3TFzsQqfpnLq8dyZMB1NZ9VyHZspGsnTa6FRTFf4dCZVnWxGo43u9VHZcq+PTtSjfVSpDBc+bavXUevccZDxFD6VRBVlHRMaXhd+b0TvnfbDvXcAAABAsqnQwlcUHd8WPjW+u65RvyNHjgbLw06ePOkvKvDF68o/tX3E/I/2T9vLSAn85fv3YnwXX2GK+uJ1N4XR0b7faIFwz19TNgt7/s7Ro8f8RVH02vrb6BjCkvK/89BRyQu/d+7778I0Ouho2xMnIt8b6KgMxqLXVaODJaURw1j890Zn6wy/dwAAAEAySZjC59OxYRohclMX4/XZlD4FCl9J8tj3Tc2hjBhF8pfv69MIYkVwz9+dlRMAAAAASiphC59ObvLU088XOElIPH7V7P4CRa4k+e8dnzCrDu+wj3Xg3Alzx6CPgnW/bhM9pbG8uOfP98MBAAAAKK2ELXw34n82erBAiStxNKLn4pblF8ntx/f7Pw4AAAAAElJSFj6VMv/kLTcaPV5Fje4BAAAAQFlIysInOpbPlj7ve/lKnPz763H0eAAAAABQlSRt4RN9fYK+JN2eubOU0f3DX8MAAAAAAFVFUhc+AAAAAEhlFD4AAAAASFIUPgAAAABIUhQ+AAAAAEhSFD4AAAAASFIUPgAAAABIUhQ+AAAAAEhSFD4AAAAASFIUPgAAAABIUhQ+AAAAAEhSZVr4rl675j8+AAAAAKCSnM3IKtDbYiWuwpd78ZL/+AAAAACASpKRlVOwt8VIXIVP7REAAAAAUPmu5F012bmXCvS2WImr8GVlX2SUDwAAAAAqmQ63i3c6pxJX4VM0ZKgDAwkhhBBCCCGEVE5U9uId3VPiLnyEEEIIIYQQQqpWKHyEEEJSJiX5H1FCCCEkGULhI4QQkjLZc+BogWWEEEJIMofCRwghJGVC4SOEEJJqofARQghJmVD4CCGEpFoofIQQQlImFD5CCCGpFgofIYSQlAmFjxBCSKqFwkcIISRlQuEjhBCSaqHwEUIISZlQ+AghhKRaKHyEEEJSJhQ+QgghqRYKHyGEkJQJhY8QQkiqhcJHCCEkZULhI4QQkmqh8BFCCEmZUPgIIYSkWih8hBBCUiYUPkIIIakWCh8hhJCkzeHjZ8zOfYcLze60oyYzK6fA/QghhJBkCYWPEEJIUuZ0+nmTnpFlipKXd9WWPv++hBBCSLKEwkcIISQpoyIXj4uXLjPKRwghJGlD4SOEEJKUKW50L0xTP/37E0IIIckQCh8hhJCkjKZrxotpnYQQQpI1FD5CCCFJmZLQCVz8+xNCCCHJEAofIYSQpEws5zIy/EUWhY8QQkiyhsJHCCEkKRPL/IVL/EUWhY8QQkiyhsJHCCEkKRMLhY8QQkiqhcJHCCEkKRMLhY8QQkiqhcJHCCEkKROWnZNjNmzcbIYMG2kvlTAKHyGEkGQNhY8QQkhSJmzugkWmfqNm5p2ade2lEkbhI4QQkqyh8BFCCEnKxMKUTkIIIakWCh8hhJCkTCwUPkIIIakWCh8hhJCkTCwUPkIIIakWCh8hhJCkTCzLlq/0F1kUPkIIIckaCh8hhJCkTElQ+AghhCRrKHyEEEKSMnl5V/1eV6jdaUcL3J8QQghJhlD4CCGEJGXSM7L8Xleow8fPFLg/IYQQkgyh8BFCCEnKaNQuHhcvXTaZWTkF7k8IIYQkQyh8hBBCkjKn088XO8qnaZ9M5ySEEJLMofARQghJ2miqpk7IUlhU9hjdI4QQksyh8BFCCEmZ7DnAaB4hhJDUCoWPEEJIyoTCRwghJNVC4SOEEJIyofARQghJtVD4CCGEpEwofIQQQlItFD5CCCEpEwofIYSQVAuFjxBCSMqEwkcIISTVQuEjhBCSMqHwEUIISbVQ+AghhKRMKHyEEEJSLRQ+QgghKRMKHyGEkFQLhY8QQkjKhMJHCCEk1ULhI4QQkjKh8BFCCEm1UPgIIYSkTCh8hBBCUi0UPkIIISmTU2czCywjhBBCkjkUPkIIIYQQQghJ0sRd+DKycsyZc+cJIYQQQgghhFRSzmZkmezcSwX6WmGJq/Bt2HrKXLp02QAAAAAAKs+1aya/9J0v0NkKS1yF76a/jfN/DgAAAACgEly9ejXuUb64Ct+MOQf8nwEAAAAAqCQ65M7vbbESV+HLvZjnPz4AAAAAoJLoWL4CvS1G4ip8AAAAAIDEoRO4+L0tVih8AAAAAFDFUPgAAAAAIElR+AAAAAAgSVVo4Tty/LTZue8wIYQQQgghhCR08vKu+nWmXB07ebbAPhQVbR+PCi18Z9Iz/UUAAAAAkHA0WFVRMs5fMOkZWf7iIml73a84FVr4AAAAAKAq0ChaRdmddtRfFBfdL/fiJX9xFAofAAAAAHgqsvCVdHTP0f2Km9pJ4QMAAAAAT0UWvtIeL6j77SlmdJDCBwAAAACeiix8N6K4/aTwAQAAAICnuCKVKIrbTwofAAAAAHiKK1KJorj9pPABAAAAgKe4IlWYq9eu+YvKVXH7mRCFb8bseTb70w76q6y16zf5iwK6T3r6OX8xAAAAAJRacUWqME1atDGHjxR9IpWyVNx+JkThGzZynFm45CfTrvOX/ipr8Hcj/UWBtp16mH37D/iLAQAAAKDUiitShVHhO3r0mL+4xK5cia9fFbefCVH4Vq1dby9Pnzlrrl27Znbu3mtvb92+0166wrduw2aTk5MbudMvdLuwkUEAAAAAKI3iilRhrl4t3Vcs+Gb+MMeMHT/Z1G/UzGzZut1fHShuPxOq8GVn59gm6wreV30H2kvdTj+XYcZPmm5atutqMjPPB/cVCh8AAACAslRckSpvffsNMo2btTIrfl5tHn7iOTN7znx/E6u4/UyIwjd89ASzc9de883A7+ztWIVvxJiJ9vrk6T+YKTNm2+sOhQ8AAABAWSquSBVm5JjxJivrgr+4xB547BmzactWe10jfE89/5q3RURx+5kQhe+jhi3MgCHD7eidxCp8DZq0Mv0GDbPbuGLoUPgAAAAAlKXiilRhqlWvbbbviByadiM0lVNxxoyfFFp7XXH7mRCFz03pbNS8rb3sP/h7exkufN16fm1Onjxto+mdYRQ+AAAAAGWpuCJVmJOnTvuLysS+/Wn+Iqu4/Uyowjd81AR7qeKnk7f0DBW+H+YssMsWLFpmtmzdEdxXKHwAAAAAylJxRaqiaZqo+pCvuP1MqMJ39my6OX7ipD05S5cefaNG+HS2m1YdvrDLMs9z0hYAAAAA5ae4IlWYydNmlskxfPEqbj8TovDFKy8vz18EAAAAAGWuuCJVmJdef8es37jJX1xuitvPKlX4AAAAAKAiFFekCrN23QZzNcbUy/JS3H5S+AAAAADAU1yRShTF7SeFDwAAAAA8xRWpRFHcflL4AAAAAMBTXJFKFMXtJ4UPAAAAADzFFamylJd31V8UF91vT9pRf3EUCh8AAAAAeCqy8KVnZPmL4qL7HTt51l8chcIHAAAAAJ6KLHy7ixmlK4zul3vxkr84SoUWvjPpmf4iAAAAAEg4R46f9heVm4zzF0o8yqftdb/iVGjh04umpkwIIYQQQgghiZzSHldXWpqa6e9DUSluKqdToYUPAAAAAFBxKHwAAAAAkKQofAAAAACQpCh8AAAAAJCkKHwAAAAAkKQofAAAAACQpCh8AAAAAJCkKHwAAAAAkKTKtPDpwQghhBBCCCGEJE783hYrcRU+AAAAAEDioPABAAAAQJKi8AEAAABAkqLwAQAAAECSovABAAAAQJKi8AEAAABAkqLwAQAAAECSovABAAAAQJKi8AEAAABAkqLwAQAAAECSovABAAAAQJKi8AEAAABAkqLwAQAAAECSovABAAAAQJKi8AEAAABAkqLwAQAAAECSovABAAAAQJKi8AEAAABAkqLwAQAAAECSovABAAAAQJKi8AEAAABAkqLwAQAAAECSovABAAAAQJKi8AEAAABAkqLwlbFjx06Y4aPHm8uXL/urkOB27d5rho8a5y8GAAAAqiwKXxl7/Z06ptfXA037zj3MlSulf03qffKZvwjlrNq7H5h+A4ea74aP8VeVmXETp/qLAAAAgHJT5oVv3759QVLN2fR0M2PWHHv9g48b25G+I0ePmfRzGWbL1u12+bVr18y+tANm6/ad9vaqNevNrNnz7PVNm7eZNes22usvV6thR5wuX75iNuff99jxE3b5gkVLzfyFS8ypU6ftbZSd8ZOm2cuuPfrYS732c+YtDNYvWLzMvu7Llv9s31ddP3rseP57tsGcOXP2+nb571FeXp7Jzs4xubkX7fqc3Fyzbccu806tenabFT+viXpsAAAAoDyUeeE7fPhwkFSzfOXq4Pq0GbNN4+Ztzdz5i02TFm3Nu3U+tstVAuvUa2Rqf/ipvf3+R41Mx2497ahg3fpNgpE9Fb7FS5eb1u27mo8+bWbefPeDYHm7Tt3N3n1p9jbKTovWHYPrKnst23UxPfv0t+9r2sFD9nbz/G303ul9bd2hm3m7Zj3T+Ytepna9hubiRZW7jfn3GWA+a9nelsE+/QabLt172/dR99H7pzL4edvO5puBQ82GjVtCewAAAACUrTIvfKlMZc7ZsGmLee3tWvZD/uEjR83+tIPm4OEj+ctqmzNn0/OXHTMnT522U0Bl4+atdiRQBSAv76p5q0Zdu/z9jxvbUaIly1bY5SoMKB9f9u5nGjVrbUfjNPqm66Ii3u3LvsE2tX4pfBcvXbIFUF55s6bZvnOXqfnBJ8F9VPhWrVlnb7v3bdjIsfa91zo5HRoZBAAAAMpamRe+zMzMIKnGTecUFTR9+FcxCC/TB3+NDClr1280HzdsbtdpxG7wdyPsfVTwXOHTCJFcuJBt0g4cpPCVs9lzF9jROY2+ufdKl5qiK5pO6wqf9Oj1jb18o/r7Zt36TVH3UanTNF8JFz558726pmuP3ubq1av2NgAAAFAeyrzwpfIxfDt27QmOrXNT+Vwx0LF7mu6nD/4qbsqF7GzzcaNI4Xujeh0zYdI0s237zqjC50aWdIyYHpvCVz50VtXMzPP2ul5jnbjlkyYtg/eqaYt2dt2U6T8UW/jcfVT4NGrrHlNc4Tt0+Kj9D4LR4yfb2wAAAEB5KPPCd/78+SCpRlMuP23a0k7Z0xkfVQBVDGbOnmuLQkZGpi1yOjZvz779JicnJyh8mhKoqZ5Dh4+2hU9TAlUSVSQ0VXDAt9/b7Sh85UfH3p0/n2VPrLJ+42ZTvfZHdrnK39iJU826DZvsSF9Rha9Zqw72+L/uX30ds/DpZ+zbf8Au17F8OnYTAAAAKC9lXvhS3dcDhphX36plC4OoGPT+ZpCpWTdybJfOuGlPwvJeZATPFT4VAZXEAYOH2cL349yFtgxMm/mjee/9+vbEL0LhKz86yY6Kt4q66LXX+7RpyzZbvhs2bWWLuztpi/iFT1M4dYIdvXexCl/dBk1t0dPxndrOHcsHAAAAlIcyL3yHDh0Kkqp0tkYnPKUzLNaxW5riGea+x8+/L8qPvkohTCN+ohO0yKixE+0oXlF00pfiXMp/PP/9BgAAAMpamRe+VD6GL5bwSVtQdS1a8pM9qY6+hmHh4mX+agAAACAhlXnhQzR9QTeSg06ysi/tgL8YAAAASFhlXvg0ndEFqErO5RpzNocQQgghhJAbiz5XJooyL3w3OqVzxJgJ9svGdZILXbbr1N1+iTlQnk5eMOboeUIIIYQQQsom+nyZCMq88J0+fTpISZw+c9bU+KCBLXqxoiIIlIeLeQX/ghJCCCGEEHKj0efMylbmha80xk6YUqDgxYq2S3Rph0+YnfsOkwRKZlbRZ8N0o3vvNjfm4XcIIYQQQgi5sehzpT5fJsIoX5kXvlOnTgWJx/60AwWKXVHR9olKxSI7h2MXE83+Q4V/113O5chfxgkLjflpTbY5d+4cIYQQQgghNxR9rtTnS33OrGxlXvhKegzf6+/ULlDqioq2X712vf8wCUGje0g8RZVwHVDrRvcuX75sv/OQEEIIIYSQG4k+V7pRvspW5oVPT86lOCpufqGLN4lI0wdRtegsSvqLqKF3/eUEAAAAbpQ+V+rzZVIWvpIo6eheOIk4tZPCV/WECx8AAABQVpK28JVkSqdf4kqSpp+39x+u0lH4qh4KHwAAAMpD0ha+I0eOBClKvGfmLCqJhsJX9VD4AAAAUB6StvDFyy9vpYm+uy+RUPiqHgofAAAAykPSFr6MjIwgRfHLW2mSaF/GTuGreih8AAAAKA9JW/jiPYbPL2+lSY0PGvgPW6kofFUPhQ8AAADl4UYL38Bvh/mLSqXMC19WVlaQwmzYtKVAeSttEkm48OlUrA0+aRxaG23KlGn+IlQCCh8AAADKw40WvlbtOvuLSqXMC188NBXTL24u1Wt/ZF5/p45p2qJdEH+bkhS+vLw8s2nzlgr5jjV/hO/74SOjboetX7/BX4RKQOEDAABAeUjawnfw4MEghWnXqXuB4ubS6+uBpm6DplHb+9uUpPDdctud5i+33GFefOk1f1WU5i1a+4uiaP3PP6/2F0fxC9/sH+fayx9++DH/9TgUtW7Pnr12/aLFS8y5Yo53RPmh8AEAAKA8JG3hi+cYvvc/blyguPmFT2fgfKN6HRt/m3gLX3p6uund52s7yveP516yy5b9tNwcPnzYXLx40YwZO95MnTrdLv/1b/5gS9jhI0fMuPET7IigLt19tP7V194MHjsWv/A99vjT9nEaNWlm7rnvoah1w74fYdd36drdPPX081HrEJ/0cxlm/cZNUctee6tG/vt+LmpZUWIVvmPHjpueX/Wx6dO33/UVnp27dvmLopw8edIcOXLUX1wmVq9Za/evX/+B5vLly/7qmJavWOkvKlbvPt/Yn7M/Lc1fZZ0+fcZfBAAAAJPEhS8emrLpFze/8J3K/yDpr4uVosyfv9BcvXrVXteHb3n0safMTTf/1Zw9e9aWuFq165pZs2bb6/oQfdvtd5sWn7e2Ja1tu462HK5dt96u//Nfbg8/fAGxCt+pU6dNbm5ugQ/MrvCJfiZK7mp+mX78mReD22vXbTDNWrazy+MVq/Bt2LDRDBk6zEbvU2FmzJzlL4qiMvZlz97+4jLRf8BgM3To9+abfgNMnQ/q+atj+qpXH39RAY8/8UzU7d//8Wb7c/56531Ry50dO4suvQAAAKmqNIXvmwHfmvqNmtk8+3K14PqAwd/5m8atzAufyo1LYfzSFqvwaWTs0qVLZs/e/QW2ibfw6YNq2IEDB82hQ4dNsxatgsInKnj33h8ZgXvz7XfNli1b7boLFy7YcihaP3nK1OCxYolV+ESje/4xe+HCV9zIIQrX6LOWZsPGzfb6o0+9YK5cif8/HqSwwucbO25C8J8GmoqrPwuu8J08dcpeZmRkBtvL439/2vztwUeD40c1Ejdi5OhgvUb/Zs76Ibg9ctSY4PqJEyeCE/vk5OQWmBaswufoz6b+vh0/fsJkZp63jzth4mT790f27t1nNm7aHBQ+t5/u+YyfMCnYD/251/aOCp/dZvxEe6n7Tpw0xf4ccYUvvO8aPf9u2PDgttbNm7fAXtdrMGr02GDd9h07g3UAAADJpDSFr9/AITELX/9BQ/1N41bmhS+eKZ3xjPCdO5dhWrXrekMnbdEUNlc8N27cZFas/NlO79TIS7jwaTTPFT4t++TTxsEZNt02N1L49EH8/gceiVpH4SsbKngqemvWbbDlr6TiKXwqJZ06dzN33/ugva33rXWb9kHh07RhGT5iVHAf0Wiypuu6Yz/ffqeGLV1Tp80wS5f+ZP9M6c+Z/oxq2qRGA3v17mu31X8StGrdzpanZ559scC04HDh03RljSS/U72mncasx9X+Vnurul2v29XfqxUUPlfS9PdD+9G5yxfBfujP++YtW91DB4Xvxznz7OWDDz9u/4PE7Ysey993FV1NhV2yZJktx19/09+8W6O2Xaf/UOnarYf9uVr38KNPBOsAAACqgtffrhnzsCJfaQpfWMJO6VSRcilMPMfwlcWUzuzsbPNR/U/Nvv377YdejU7Mnj3HvPJatQKF75HHnrTXq79by5bCwd8OtSdUGfrd93aERevDozOxxCp8+tmaVqoSGUbhKzuaxvnwE8+VeHRPCit8L79azeaL7l+ac+cixwTW/bC+vXTvmyt8Ki3inxhIRaj/gEHms2af29sqZKKi88BDj9upwqKy9sCDj9nrmjasrzR56+337G09pz/ddFuBacEqfCqDOuHPHXfdZx9DEfe4NWq+by81uqc/g7EKn/bD0f396cX6O/LT8hXBc3QjeSqJosfy992NZqsYtmzV1l53783HDRrayxdefNWuUzEszfsGAABQWfTZM9ZhRb6kLXzxiOcsnWVR+OT1au+Y3/3+JtOmbQd7Wx+ONdLiFz4dr6WSp5GQW2+/y36gvu9vD9sPyh07d7XrS3MMn8rjXff8ze5HGIWv7KgwNG/V3l8cl8IKn0b1FJ3ER4+vwq6zvYpf+DSipTLmRgBF73vfr/vbPzfuz9m3Q74L1rupwo62UUHTpb5GRH9eNBImOpbUnxasP5+333Gv/TO6bdv2oOxphM/Rn7Hwf7zEKnz+fsQqfO/VrBP8/VFB1H6GR/j8fdd/lLz+xtv2P1u2bt1m3nizevDcw9tqnYpk+HUBAABIdPpsGM9hRUlb+HTskUthivoevpImHhoJiYc+pItG9GIp7myIfuFzNNKIxFRY4QvTKJ/KVtPPWtjbfuEbMPBbO61T2zkLFy222yuu8Lmpn/LHP98a9YtBpVGjwYqbhqypx+4smP604PCUTnGFT/d1j6v767b7c+sKn0qZqPBpP8L8wuemdLqz3OpYPrefosLn77tKoY5rVOETTWlt1jwy3bZxk+ZR99ffObcOAACgqojnsKKkLXzxHMO3YdOWAsWttEkkhRU+JK54Cl/Dxp/ZS52ARfzCp3Kj4+w0yufUb9AouD56zDh76aZParRMx7Jp9E//GRAeHVRB1C+QQYOH2KKm6ZmaEupPCy6s8IkeV9w0TE1LVmF0hU/H92n0UlM1tR/i9uOhR/4eeZBfuMKnY/fE7YMblVPh8/e93sef2P1V4XPH9emx9Xz+/uQ/7G1NddU6Hcvn1gEAAFQlxR1WdKOFb+CQyGe6G1XmhU9P2KUofnErTWp80MB/2EpF4at6Cit8f7rp1iA6iYkKnTu5iF/4xB0D6oRHznScnc6IqeKlrz3Yu2+/LWg6RlDTfWX16jW2DLlyqJ+nr0LQCJiKkz8tuKjCp8fVcXWulD359HP257rCp3U6U61G+Ozxg/lF1O2HjtH7fvhI91BB4Zs+Y5Y962eTps3tc33t9bfschU+f991LKO20X7rZ2jdbX+9x67T2Tu1PyqyWqey6NYBAABUJcUdVnSjha+slHnhi5df3koTTQ1NJBS+qidW4YvFffVCYfTVBvE4cyb6ZEbhry9xJ4dx3NcqSEmnBZ8/H/3bxX01RCz6ioXwfripzYVxX8kQ5u97eMRO01Ld92FK+LhC7Vd4HQAAQLJI2sIXz5RO8ctbaXLa+/Bc2Sh8VU+8ha8o+oqGeI8TBQAAQGpI2sJ39OjRIEUZO2FKgQJX0iQaCl/VUxaFT19yDgAAAIQlbeErCb/AlSRNPy98vmxlofBVPWVR+AAAAABf0hY+HcvjUpzX36ldoMjFm/1pB/yHq3QUvqqHwgcAAIDykLSFL95j+GT12vUFily8SUQUvqqHwgcAAIDykLSF78KFC0HiUdJRPm2vopiI0g4X/mXzqDzZOYWfUIXCBwAAgPKQtIWvpDQ10y91RSURp3I6mVnZRZYLVI79h477iwIUPgAAAJSHpC18Bw4cCBKveM/Yqe0SnUb5NLWTJE5UxAtD4QMAAEB5SNrCt3///iAloe/Uq/FBgwIlzyXRvmQdyYHCBwAAgPKQtIXvRqnYvf9xY1vydNmuU3ezYdMWfzOgTMQqfNeuXSOEEEIIIaRUcSh8QAIIFz7/LyshhBBCCCGlDYUPSADXC1/0X9CrV68SQgghhBBSokQXvmsUPqCypedcM0cyr5nqzSJ/SfPy8gghhBBCCLmh6HOlPl/qc6bKX2Wi8CFl6S9f9qVr5nDGVTN+wVWzZtMVc+VKdC5fvkwIIYQQQkiR8T9D6nOlPl/qc6Yb8assFD6kLDd18/j5q+bQuTzzWv0T5t6Xj/ySw4QQQgghhJQwkc+S+lypz5f6nEnhAypB+Fi97Et5ZuuBMyY795K/GQAAAFBi+lxpP19eikzvrMzSR+FDSnJlz82z3n/0tL8JAAAAUGr6fOmO53OlrzJQ+JCSwoVP86wvXWJ0DwAAAGVHny/1OZPCB1QCV/jciVkAAACAsqbPmW6Uj8IHVBA3h5rRPQAAAJQnfc50hxBV1nF8FD6knPB0Tv2vC4UPAAAA5cFN66zMUT4KH1JOuPDpL+HFixf9TQAAAIAbps+ZFD6ggoWP31Phy83N9TcBAAAAbpg+Z7ovZqfwARUkXPj0vy4UPgAAAJQHCl8FOHbyrNmTdtTs3HeYJFj0vuRerPjj5/zCl5OT428CAAAA3DB9zqTwlaOM8xdMekaWycu76q9CAtD7sju/9FU0Ch8AAAAqgj5nhr+Pj8JXxiqjTKBkLl66XOGjfCUpfNru+ImT5mz6uWDZ6TNn7TJFB+CK/udm3/4DwV9it145dfqMyc29aDLPn7fr9Jc+Jyc3//Jy1Ha6r7uUk6dOR/1S0LpY1y/mv345ubnBfmmfnc1bt9uf73P3z7qQHbUPegztZ3iZHm/Xnn0mOzv263QuI9M+jhO+r6PnceTosahtwnT7cv77EX5tlfDr5rbzXzf3WHo/jx47EWwLAABQ2Sh85Uyje0h8mnZbkVzhU0nTvOqiCp+KzEcNW9gsWrrcLuv0Ra9g2dmz6baofNK0tb3drec3dhu3Xmnd4QuzYdMW07JdV7tux87dZvnPa8zefWlR26m02cucyDGFU2bMNmvWbbTXtb+NW7Sz193jO1u377Tbuf1q1LytGTtxarCd0m/QsGB7t1xmz10YtQ9dv+xrxk+aHrXMvQYfN/rczF2wOOpxVMbcdipiEr6v/Jj/M5p+3sHeVgF124SLqG4fOnwk6rVVwq+b285/3dzP+fSX90CvLwAAQCJwhU+fOyl85YCpnFWDjuWrSH7hy86+PjrlU9n5bsRYs23HrqBYqJSkHTxkoxG+gUNGmGkz55g9+UXks1YdbQHUtm6bw0eO2eLi7u8KX+7Fi3a921b7pOuu8GnkrlX7bvb6TytXm4VLIoVT3GNJuPAdOHTYjJkwNVivS+17izZdTPovo5Tnz2eZ7r362f3S6Jx+dt8BQ+zlseMnbOHbuWtvsP96Dbp072NWrVkf9XNl+KgJZu36TWbWj/Pzy+ASuyz83N3twd+NMlu27jANmrQKls2cPc9e1/uhkuoKn7uvEn7d3P38103RyOCAb4ebnbv3RhVjAACAyqTPmRQ+pDydwKUilbTwTZwy014PF76wcCFZt2GzLR1+MVJxUTE8cPBwUPgcv9C4wuduq/g1b9M5aqpmYYXP0YiauO00nXLytFn2+pJlK83uPfvMlOmzg+2HDh8TXFfhC+9D+DUY8v1oOxLpqAg6e/cfsJfhfdNr3bPvwGDfv/p6ULBN647d7frde/fb18YVvrDw6+bu54Svb9y8LRgNVQEFAABIBBQ+wFTNwrdpy3ab8PIwLXPbaNRMxUVlsEuPviUqfBp50+ih/zOKKnwqiJre6G+n4iVf9hlgL8NTJf3Cp8dz+x9+DfQ8NPrnaFSvd79vTUZmZrAs/NyPnzhl5i9aFqwLb6PsyS97I8dOMvMXLg0Kn7uvimD4dXMjoOHHcPReNmnR3o6yAgAAJAoKH2ASv/CpWGjKYfsuPe2y8HFm4pcxt8xl0tRZQXHR7R279sRd+E6ePG2XaVppWPg+4cKnctX1y6/t8Xb+dholDC8Lr/MLX3j/w4VPU0aXLV8VbKvXsWO3XvbnuZG/8H1V3NZv3GKX9/5msOn+Vb9gG03vHD1usp2Cqemq/jF8eh7h102lMLzP4esyKv+xtGzDpq1RywEAACoLha8SbMut2BOEoHhVofApOmumqJToODJFwsVDj63j+rTMbaOzMqm4aKrht8NG2XK2fOXq4D5+iQkXPrfMP9Nm+D46Nk6Prf1q0baLnQLpSk94u68HDA2WhY/zE7/wpZ/LCPY/XPhWr91g9qcdDLZ1dAyfCpeEn7uOrdOJYUQnfPn0szbBNoOGjrDHFup6uPC5++qXY/h1a9isbYHXyqfjFd1xggAAAJUtpQvf3PmLzYxZc/zF5e6B3RNNlxPXR1dQ+RK98Kns6GsJ3DFw/nFm4eKxYPFPdsqjX0ZccdHUxx69+pe48IW/9kA+b9s1+IUxPf/v0bHjJwvsl7jHVilUKXPLVP50qRPMiF/4CjuGT9NC3X1E5dIJj96Fdej6lf16hfA6XW7ass1eauQxXPjCwq+bRgL918pZ8fOaqBFGAACARJCyhe9i/pNu3Lxt/ofWzvb4poqyKvuEuWvXOJuKf6lRmKpQ+ERfvSAqJStXrbVRkZk0daYdrVq6/Gc7uuSONXPbqLC44iJaV1Th00lVdD/9cnDL/MKnr2zQWSn1OPUbt7TL/LIkuq+mQuqYPh3bp2I4ZvwUu27BomXBSKBf+Nw+KPrZ+hk6yYv7WY7Kqx5//OTpZuqMH+2y8HMX3Udf96CvZ2jWulOwjUZCm7XqaKe8hgufu68Sft30+vqvlaORPZXYn1evY4QPAAAkjJQtfGvXb7RPWk94+crI8UCnTp3O/4AXGXlblv/BTte3bNthRwFk8S/fgab/yV+4uOBJIOJx3+4JQeFrdWyluVpM7Rs/YZK/CDfgaiF/wKtK4XPHxYWPM3Nfjq5RLN3WCUjErVc0zTJcXHTSlKIKn4umVbplfuHTz2zZrptdp688kMIKnwqQCqLM+GFucNIVPf6goSPtdb/whffDTWvVz9NIYZi+4kFlssnn7YMvoQ/fV3QMnkYGGzZrY0/i4raRCZNn2K+HiHUMnxJ+3fSc3f3Cj+HoJDR6j/b9crZQAACAypayhe/EiZNmwaKlwW0d0/R2zXqmUbPW9ninWh9+alq07mjmLVhsanzQwG7zyps17Yfrjt16mg5dvizxyODirCNB2XP57OhP/mZRnvnHC2ba9Jlm9o9zzeQpU832HTvN8hUr7bqFiyJfQD1r1mwzcVJkxATRRo2dEFxPO3DIbNu+M7T2ukQufCXhT8WsCBe8IlgZ9FrGwxXC8uS+/B0AACARpGzhkzr1GpkevSLH/NT84BM70qcXYtGSn2zhk+zsHFPt3Q/s9bYdvzA9+/QP7v91/2+D6/G4Z9f4AoVPKcrtd9xrvh3ynXns8adN6zbtzcZNm03dD+vbda+9/pY5duy4adO2g2nxeev8MhoZucB1z738ppkwaWpwvTDJUvgAAACAsJQufBrJ6z94mFmzboN5uVoN82nTlqZ1h27m+5HjgsInvb4eaF+YJctW2O20jdKkRdvQoxXPL3rxFL7vh0emu6nwOeHC1/Sz61PKunbrEVxHxIGDh8xTz79mv/R7+KjorxUIo/ABAAAgGaVs4dOXLTt9+g22RU7H5qUdOGjOnE2PKnw6hk9TAXWil48+bWa3UVQiSqLjidUFyt4L+yPHZhWmuML3u9/fZGrUfN/m3Rq1g21w3a7de8zTL7zmL45C4QMAAEAyStnCp9G6TZu32S+gnjbzR9OsVQczcMj39gQQe/elRRU+vSgt2kTO7Ddi9ARzPivLHgukqZ8loZc2XPae3TfdnLyS428WJVbhq1krMsVUhe/Z5182+/bvt9H0TsQ2bWbkhCGFqejCNzlvsvniyhem6+WupsvFLqZzbmfTPa87IaSYpF1L8/42AQCAoqRs4dOT1Ula3qpR107tPJuebkvdG9XrBCdtCdMIoKjo6T46rk9n9SypNsd/DgrfscsX/NUFTJ063V6GC9+f/3K73f9XX3vT9O7zTfCmLViwKNgGJVPRha/WlVrmny/9s/lfl/5XkH++/M+EkGKy5OoS/68TAAAoQsoWPtGT9Z+wXojiqPRdKOUUPH0Ng8re0/um+atiysrKMo8+9lRU4dNJWnT2To3waV/uf+AR88hjT5aqgCKiogvfi1deNL+69CtCSAkz7+o8/68TAAAoQkoXvsry+bEV5sCl8/7iQhV3qn29eZmZ8T8eCqrowvfSlZcKfJAlhBQfCh8AACVD4QNMxRc+N8JX/XJ10/5ie9Mut53pnNeZEFJIfnf5dxQ+AABKgcIHmIovfG6Eb+zlseZw7mFzMPugOXXtFCGkkDxz5RkKHwAApUDhA0zlFb7Zl2fztQxAHNzfGQofAAAlQ+EDDIUPSHQUPgAASofCV87y8q76i5CA9qQd9ReVKwofUDIUPgAASofCV87SM7L8RUhAx06e9ReVKwofUDIUPgAASofCV852V/DIEUru4qXLJvfiJX9xuaLwASVD4QMAoHQofOUs4/wFO8rH1M7EpPelMko5hQ8oGQofAAClQ+GrAJouqGPEdGIQkljR+1LRo3tC4QNKhsIHAEDpUPiASkDhA0qGwgcAQOlQ+IBKQOEDSobCBwBA6VD4gEpA4QNKhsIHAEDpUPiASkDhQ1lZtWq1v6hS6R+S8kDhAwCgdCh8QCWIp/B17dYjSFEmT5nmL4qi+x8+fMRfXCbc/i1atMRfFdPIUWPMgQMH/cXF0s8YMXK0v9gaNHiIv6jc7Nu337Rs1dbk5eWZNWvXFXiPwu/V7B/nFnjvvuk3wIwZO95cvlL87yr3C7l1m/b+qijP/OMF+wvc7cfAQd/a5bNnzwm2OXLkqLn7ngfsn7XifD98ZPAYvuL+rEm79p38RWWCwgcAqWPx0uX+onIxf+ESc+LkKdPty772drtO3c3FixfNV30HeFtG0318CxcvM2PGT7aPGZaRkRl1uzJQ+IBKEE/he/LpZ82AgYNtivJezTr+oig33Xy76dK1u7+4TDz19HO2HPzjuZfiGtnRdst+KvqX+J49e/1F5ovuPU2rNu3M4iVL/VXm3vsf8heViwULFpk//vkWM/jboebZ5182mzdvse9N/QYNg/fof//LvwXb33HXfVG39bxUyF55tZp59bU37bJTp04H631X8kuhXtOJEyf7q6Lo/dUvcO2D3ot3a9S2yz9t2CTYpm27jiY9PT24XRgVUT2fRo0/i7lvxf1Zk//6w1/8RWWCwgcAqaNj157+okINHzXOXxS3lm07my1bt5upM36wt78ZONRe/vDj/PBmBeg+vk+atDQzfphjlq+Mnnlz4ODhqNuVgcIHVIJ4Cl/4A7ts277DTJo8Nbh9/MQJs3XbdvshfPqMmcHyCRMmBddFI02333FPcHvGzFlRH+ZHjxln/zdLVGJWr14TtS7z/Hl7PScnxwwfMSpYJ24fVRS0L8tXrAy20WMpol8uWu4K38yZkV+sc+dFfqFqBNLtR6vW7cyo0WPtcufo0WP28u13athLrf/hhx/tdVf4/H2fMnW62bp1m72ufRv2/YiglC5ZuszsT0sLtg2vK4yKjJs+qefhuOciKnPOy6+8EVX4vuzZy17qddTrNnXaDNPzq97BiKfez3nzF9jres8yMjLsPi1d9pNdpl/Seo18H9arH1zfvmOHfRwJ//nRfkybPsNeD78veo2Gfve9ycyM/O/jypWrgvu457p48VKzcOFie90VPu2LRgIdvX7aZwm/NmWJwgcAqcMvfOnnMsyc+YuC27PnLjC7du81x46dMK+8WTNYrpG3rdt32vWXL18x8xZE/v2SfWkHbESFZ+78xUHhW7JsRX5RW2Watepg169ctTa4z45de4L7bN+5y36G0n3879h+q0bdqNvO3n1pUSOW2ie3H/q5smDRUlvIflqxyu67zJm3sEAxm7dwiUlPP2eva+RQj3su/7WRCxeyzYqfr38OCqPwAZWgNIXvr3feaz6o+1Fw+/kXXzHrN2y0H8IbNWkWLK9R6/3g+saNm+zlQw//3V6qODVs1NTcfMsd9ramYmr05+FHIuufeOpZu61G1FREOnXuau6570H7i+GRx560I1Q7duyMPLiJ3keVqPsfeMT06t3XdPviS/uYjzz6hF3XvEUr+1ga9VLhcyXNlYNbbrsr2I9atesG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>