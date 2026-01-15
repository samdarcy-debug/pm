---
id: learnings-2025-022
title: Q3 2025 Learnings Memo - Tingting Wu
type: doc
status: approved
team: gtm studio
owner: '[[teams/gtm studio/_people/tingting-wu]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- gtm studio
related: []
---
#### Metric Alignmen​​t



#### This quarter\'s work contributes to GTM Studio\'s north star of driving credit and AI credit consumption by establishing the foundation for more intelligent, context-aware AI platform. The GTM Config Agent ensures customers can manage the GTM context (offerings, personas, messaging, competitors) that enables AI agents to generate more relevant, personalized recommendations. Better context = more accurate signals, recommendations, artifacts = higher AI credit consumption as customers trust and use AI features.



#### Key Learnings



1.  **We were solving for a narrowly scoped problem.** Multi-offering

    configuration was thought to be a major blocker for enterprise

    customers, but VOC analysis across 14,861 feedback instances

    revealed only 6 customers ([[\$849K

    ARR]{.underline}](https://docs.google.com/document/d/1hPCVxTBe9gUoajVUMQLbIFMbaLrkfaqB9mHjGy22II8/edit?tab=t.0))

    with explicit product-specific configuration pain. The real issue:

    customers need an easier and more flexible way to power the system

    with their GTM context.



2.  **Configuration complexity, not missing features, drives adoption

    failure.** Customers report \"constantly having to unselect and

    reselect intent topics\" that are relevant to specific products

    ([[Snippet]{.underline}](https://hello.chorus.ai/listen?guid=9893183a8abc4d38b648ddee5c997bf1)

    \|

    [[FR]{.underline}](https://discoverorg.atlassian.net/jira/polaris/projects/ZIDEAS/ideas/view/4614379?selectedIssue=ZIDEAS-127))

    and \"I just abandoned it altogether\"

    ([[Snippet]{.underline}](https://hello.chorus.ai/listen?guid=8fe16ba6bf4343ba8cc3ae7a4fe33dbd))

    when describing buying group setup. The current structured-first

    approach forces premature knowledge structuring before customers

    understand their own GTM strategy in the platform context.



3.  **Current onboarding optimizes for data capture, not customer

    success.** Admins spend anywhere from a few weeks to months in

    manual setup, while agents lack the qualitative context needed for

    relevant recommendations. The system is a \"black box\" - customers

    cannot see or control how their configurations generate the \~30

    recommended signals

    ([[Snippet]{.underline}](https://hello.chorus.ai/listen?guid=351ab6b660bc4b54a0ffe60d2f75dfde)

    \|

    [[Snippet]{.underline}](https://hello.chorus.ai/listen?guid=f691213cbf8e42d7b8b6e09a733accc7)),

    leading to distrust, feature abandonment, or custom projects.



4.  **The solution requires architectural inversion: from structured

    input to AI extraction.** Instead of forcing admins to populate

    rigid settings, enable conversational \"brain dump\" or system

    integrations where AI extracts and structures GTM knowledge. This

    mirrors how successful onboarding managers work today - gathering

    unstructured context through conversation, then organizing it

    systematically.



#### Hypotheses & Results



**Hypothesis 1:** Multi-offering support is the primary blocker for

Copilot adoption among enterprise customers



> **Method:** Leveraged AI to analyze 14,861 customer feedback instances

> on multi-product pain points, and mapped them to opportunity value and

> deal sizes.

>

> **Result:** Invalid - Only [[6

> customers]{.underline}](https://docs.google.com/document/d/1hPCVxTBe9gUoajVUMQLbIFMbaLrkfaqB9mHjGy22II8/edit?tab=t.0)

> with \$849K total ARR showed explicit multi-product configuration

> struggles. Average deal size of \$141K indicates enterprise

> concentration, but frequency doesn\'t justify standalone feature

> investment. Pain manifests as: manual intent topic reconfiguration

> (SWK Technologies), separate workflow creation for product suites

> (Inovalon), and complete buying group abandonment (DKA).

>

> **Decision:** Pivot from multi-offerings as a standalone feature to a

> systemic GTM Config Agent that addresses configuration complexity

> holistically. Multi-offering context becomes part of offering-centric

> intelligence architecture, not a separate UI.



**Hypothesis 2:** GTM-context improves signal relevance and reduces

\"black box\" perception.



> **Method:** Mapped customer pain points (from VOC) to GTM Config Agent

> architecture. Created a prototype demonstrating AI-powered GTM context

> extraction and user-offering assignments.

>

> **Result:** Validated - [[Customers explicitly

> report]{.underline}](https://docs.google.com/document/d/1hznTJVowaYbXs7vryYb6ZBR-Q8Vv9dCqND0QPFz6lVs/edit?tab=t.0#bookmark=id.ng7i3qqtgn53):

> inability to "serve signals that are specific to products,\"

> \"different buying groups need different buying signals,\" and

> frustration with generic LLM-generated defaults. Need for

> offering-level context extends beyond multi-product companies to any

> customer with diverse GTM strategies (e.g., different personas for

> different market segments) \| [[Thread

> 1]{.underline}](https://zoominfo.slack.com/archives/C06TFJ42GH3/p1759092251376429)

> \| [[Thread

> 2]{.underline}](https://zoominfo.slack.com/archives/C06TFJ42GH3/p1758554635614349)

> \| [[Thread

> 3]{.underline}](https://zoominfo.slack.com/archives/C09FJLA3QK1/p1758228467649069).

>

> **Decision:** Build the GTM Config Agent with offering as a central

> organizing principle. Each offering bundles related configs (target

> personas, intent topics, messaging, competitors) and provides visual

> mapping of how configs generate specific signals, enabling admin

> customization.



**Hypothesis 3:** Phased Admin-controlled Copilot rollout for Copilot V1

will improve TTV and increase "Aha moments", leading to increased

Copilot adoption rates



> **Method:** Designed and developed the "Launch Copilot" experience to

> prevent negative first impressions of the Copilot Homepage Feed and

> support R&G customers' phased rollout of Copilot until Admins have

> configured the minimum number of steps to power homepage

> recommendations.

>

> **Result:** Validated Problem, Solution Paused - During internal Beta,

> the Copilot team pivoted from V1 (Copilot Homepage Feed) to V2

> (Workspaces). Additional research also revealed that \"launching\"

> isn\'t the core issue. Customers struggle because: (1) GTM configs are

> fragmented across multiple pages, (2) intelligent defaults did not

> support complex GTM motions, and (3) GTM configs did not evolve.. The

> launch button doesn\'t solve these systemic problems.

>

> **Decision:** Release was paused due to the Copilot team's priority

> shift. However, learnings directly informed GTM Config Agent

> requirements: conversational onboarding, AI-generated 0-config

> defaults, flexible customizations.



#### Go-forward Changes & Plan



- **GTM Config Agent MVP Development ([[GTM Config 2025/2026

  Roadmap]{.underline}](https://docs.google.com/presentation/d/1b0nY8mt_zPTfWW4JYDUiBwspL7kcBJpQB2WGUDmMrgw/edit?slide=id.g27221718934_0_0#slide=id.g27221718934_0_0))** -

  Conversational AI interface for validating 0-config GTM context

  defaults, managing and maintaining GTM context relevance over time.

  Enable offering-specific context (target personas, intent topics,

  messaging, competitors, etc.) to flow into AI agents. Provides

  \"unified GTM context\" that agents can query for relevant

  recommendations. Critical dependency: GTM AI Context data product

  finalization with Rowan Bailey\'s team.



- **GTM User Context** - Develop POV on the management of GTM context x

  user context based on customers' unique sales org structure, so that

  users receive recommendations and signals only for the products they

  sell or accounts they manage. Critical dependency: GTM User Context

  data with David Goulden.



- **Signal Transparency & Customization** - Visual mapping showing how

  GTM configs contribute to \~30 recommended signals and how custom

  signals fit into the roadmap. Allow admins to adjust

  parameters/weights for signal generation, addressing \"black box\"

  perception. Critical dependency: Custom signals with Srivatsa Marthi.



#### Leveraging AI



1.  **Most impactful - v0 for rapid prototype validation**. Created

    interactive prototypes for GTM Studio Onboarding, GTM Config

    Library, and GTM Config Agent. These prototypes enabled stakeholder

    alignment and pivots as concepts diverged and converged without

    engineering resources. [[GTM Studio

    Onboarding]{.underline}](https://gtm-studio-ob.vercel.app/) \| [[GTM

    Config

    Library]{.underline}](https://v0-gtm-solutions-gtm-config-library.vercel.app/)

    \| [[GTM Config

    Agent]{.underline}](https://gtms-onboarding.vercel.app/)



2.  **Accelerated customer research** - ZI Chat rapidly analyzed

    customer pain points around GTM configs / multi-offerings /

    onboarding from Chorus calls during VOC analysis. Also helped

    identify customers that would benefit from early user feedback

    sessions.



3.  **Roadmap and research planning** - Used AI to transform high-level

    strategy documents (PRDs, customer research) into actionable

    roadmaps and [[research

    plans]{.underline}](https://docs.google.com/document/d/1znWNWqoQusJXuyTuNgK63--hbF0KvvXMYQ-ekC6CdJ0/edit?tab=t.q6zwj81qxjir)

    with concrete milestones and click-stops.



4.  **User research synthesis at scale** - Will use AI to systematically

    analyze upcoming user research interviews (planned for next 2-3

    months), extracting key themes, pain points, and workflow patterns.

    Goal: Reduce synthesis time by 60-70% while maintaining research

    quality, enabling faster iteration on GTM Config Agent requirements.



5.  **LangSmith for agent error analysis** - Following the learning

    session with Lars, will leverage LangSmith to perform systematic

    error analysis by examining agent traces. This enables

    identification of: (1) where tools fail, (2) customer inputs that

    confuse the model, (3) how to improve prompt engineering. Plan to

    integrate LangSmith into prototype testing workflow to establish

    baseline performance metrics before broader rollout.



**Key mindset shift:** Moving from \"AI as productivity tool\" to \"AI

as product requirement validation tool.\" This quarter proved that

AI-assisted research and prototyping can prevent quarters of wasted

development effort.

