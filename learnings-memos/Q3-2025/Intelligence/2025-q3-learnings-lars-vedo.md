---
id: learnings-2025-030
title: Q3 2025 Learnings Memo - Lars Vedo
type: doc
status: approved
team: intelligence
owner: '[[teams/intelligence/_people/lars-vedo]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- intelligence
related: []
---
## **Metric Alignment**



**North Star Metric: Agent Adoption in Production**



Our H1 focus centered on launching the Agentic AI platform and enabling

adoption across ZoomInfo products.



**Key Achievements:**



- **Platform Launch**: Successfully deployed production-ready agentic

  platform with AI Action credits, multi-model support (Anthropic,

  OpenAI), entitlements, agent-to-agent communication, MCP integrations,

  an API, and an embeddable chat framework



- **Agent Development**: 8+ teams built agents including SalesOS,

  Chorus, Workbooks, Copilot Workspace, Web Search, Advanced Search,

  Marketing (audiences, intent, website), and Research agents



- **Production Adoption**: 2 agents live in production (Chorus, Copilot

  Workspace) with peak usage of nearly 1k sellers testing Copilot

  Workspace in production in Oct



- **Platform Enablement**: Reduced agent development time from weeks to

  days---teams can now embed chat frameworks and connect agents within

  24 hours



## **Key Learnings**



1.  **Velocity is existential in AI**: User expectations evolve so

    rapidly that 3-6 month old MVPs become outdated; ship early and

    iterate or miss the wave



2.  **MCP is the integration standard**: Building data sources as MCP

    servers enables seamless availability across ZoomInfo, Claude,

    ChatGPT, Salesforce Agentforce, etc



3.  **Context quality \> context quantity**: Overstuffed agent context

    increases both error rates and costs; precision in what information

    you provide is critical



4.  **Platform investment validated**: Our hypothesis that internal

    teams would successfully build on the agentic platform proved more

    true than anticipated---the shift from SalesOS to Copilot Workspace

    demonstrates the company\'s commitment



5.  **Consistency matters**: As AI-powered chat experiences proliferate

    across products, maintaining unified UX through centralized

    frameworks becomes strategically important for consistency,

    efficiency, and driving powerful UX paradigms



6.  **SDK complexity limits adoption**: While engineering teams thrive

    with the SDK, democratization requires no-code agent builders for

    non-technical teams



7.  **Tool definition precision drives LLM success**: MCP tools must be

    specific in scope and extremely descriptive in their definitions for

    LLMs to use them effectively



8.  **AI-first product development**: Recording + transcription + LLM

    summarization unlocks faster documentation



9.  **Automation multiplier**: Combining AI with automation tools

    (Zapier, internal workflows) for feedback analysis, ticket

    generation, and prompt improvement dramatically increases throughput



10. **Vibe coding breakthrough**: Non-engineers can now prototype and

    ship production-grade code using AI pair programming tools like

    Cline (and rigorous standards + code reviews)



## **Hypotheses & Results**



**Hypothesis 1: Platform Investment Will Enable Team Success**



- **Expectation**: If we build a robust agentic platform, internal teams

  can independently build agents



- **Result**: ✅ **Exceeded expectations**---8+ teams successfully built

  agents with minimal support; Copilot Workspace launched as AI-first

  product in \<3 months



**Hypothesis 2: Chat Framework Reusability**



- **Expectation**: Centralized chat framework can reduce duplicate

  effort across products



- **Result**: ✅ **Validated**---teams can embed chat + agent in \<1

  day; now need to increase extensibility through widgets/add-ons



**Hypothesis 3: MCP Will Simplify Data Integration**



- **Expectation**: MCP standard will make data sources universally

  accessible



- **Result**: ✅ **Strongly validated**---MCP became our gold standard;

  services built once become available across all AI platforms (Claude,

  ChatGPT, Agentforce, ZoomInfo)



**Hypothesis 4: Production Adoption Would Be Immediate**



- **Expectation**: Once agents are built, production adoption would

  follow quickly



- **Result**: ⚠️ **Mixed**---only 2 of 8+ agents reached production

  despite technical readiness; learnings: production deployment requires

  GTM readiness, not just engineering completion



**Hypothesis 5: Context Optimization Is Tactical**



- **Expectation**: Providing comprehensive context improves agent

  accuracy



- **Result**: ❌ **Reversed our thinking**---more context often degrades

  performance; learned that precision \> volume and irrelevant

  information distracts LLMs, increasing errors and costs



## **Go-Forward Changes &** **Plan**



**Q3-Q4 Priorities:**



**1. Platform Extensibility**



- Inner-source chat framework with widget/add-on architecture



- Expand agentic platform extensibility through tools, MCP, and API

  access



- Enable other teams to contribute without core team bottlenecks



**2. Democratize Agent Creation**



- Ship no-code agent builder for non-engineering teams



- Reduce barrier from \"engineers only\" to \"anyone who understands

  customer problems\"



- Transform agent creation from code to configuration



**3. Production Deployment Support**



- Develop agent deployment playbooks that address more than technical

  requirements



- Focus on adoption metrics, not just build completion



**4. Maintain Consistent UX**



- Establish design patterns for AI interactions across all products



- Continue investment in extensible chat interface



- Prevent fragmentation as AI proliferates across product suite



## **Leveraging AI**



**Most Impactful Use Cases:**



1.  **Vibe Coding with Cline (VS Code)** - [[Demo

    prototype]{.underline}](https://zoominfo.zoom.us/clips/share/mIr3vvpjS_2rGhEzRKZMVQ)

    (Passcode: QLjB2nL\*)



    - Enabled non-engineers to build production-grade prototypes



    - Accelerated development cycles by 10x for exploratory work



    - Democratized technical contribution across product team



2.  **Documentation Automation**



    - Recording + transcription → LLM summarization for meeting notes,

      product specs, and technical documentation



    - **Key learning**: Brevity matters---always edit AI output for

      conciseness



3.  **AI-Powered Workflows**



    - User feedback analysis → automated Jira ticket creation



    - Continuous prompt improvement through automated testing



    - Reduced manual operational overhead by \~40%

