---
id: doc-zap-agent-building-best-practices
title: Building AI Agents: Challenges & Best Practices
type: doc
status: draft
team: intelligence
owner: [[teams/intelligence/people/adam-smith]]
created: 2025-12-16
updated: 2025-12-26
tags: [agents, zap, product-management, best-practices]
related: []
---

# Building AI Agents: Challenges & Best Practices

This document is for Product Managers building features on top of ZoomInfo's Agentic Platform (ZAP). Its purpose is to help you understand how AI agents actually work, why they succeed or fail, and how to design them well.

## Overview

The central argument: building AI agents is fundamentally about shaping probability space. Unlike traditional software where features either work or they don't, agents operate in a probabilistic world. Your job as a PM is no longer to specify a feature that works 99.9% of the time. It's to design the boundary. Where must the agent succeed? Where is failure acceptable? How do you communicate that boundary to users and stakeholders?

This is a different discipline than traditional product management. It requires new mental models, new ways of specifying requirements, and a deeper understanding of how language models actually work.

## Part 1: The Fundamental Shift

### From Deterministic to Probabilistic Design

Traditional software is deterministic. You write code, it executes, and barring bugs or infrastructure failures, it produces the same output for the same input. A database write either succeeds or fails. A form submission either validates or doesn't. You can reason about edge cases, handle them explicitly, and achieve near-perfect reliability.

AI agents are different. They operate probabilistically. When a user submits a query, the agent doesn't execute a fixed procedure. It reasons over possibilities, makes inferences, and generates a response that's statistically likely to be correct given its training and the context you've provided. Even with identical inputs, you might get slightly different outputs. Success isn't binary. A response can be partially correct, directionally right but missing nuance, or completely off-base in ways that are difficult to predict.

This is the nature of the technology. Language models work by predicting likely next tokens based on patterns learned from vast training data. That statistical foundation is what makes them powerful: they can handle natural language, reason over ambiguous inputs, and generalize to novel situations. But it also means they can fail in ways that traditional software cannot.

The old game of product management was to specify features that work reliably all the time. The new game is to shape the probability space. Design systems where success is highly probable in the cases that matter. Understand failure modes, bound them, and communicate them clearly.

### What It Means to Shape Probability Space

Imagine a probability distribution over all possible user queries your agent might receive. Some queries cluster in common patterns: asking about account status, building prospecting lists, researching contacts. Others fall into a long tail of unusual, ambiguous, or edge-case requests.

When you design an agent, you're shaping how it performs across this distribution.

**A narrow, rigid agent is like a laser.** You constrain it to follow specific procedures for specific inputs. If the user asks about an account, always retrieve data from these five sources, always format the response this way. This approach creates a sharp, high-confidence region in your probability space. Within that region, success is nearly guaranteed. But rigidity is fragile. Outside those narrow bounds, the agent either refuses to engage or fails unpredictably. Users who expect it to work first time will be satisfied within the bounds and frustrated outside them.

**A broad, flexible agent is like a floodlight.** You equip it with principles, examples of what good looks like, access to tools, and instructions on how to use them. This approach creates a wider region of moderate confidence. The agent can handle a broader variety of inputs without explicitly failing. But it's more likely to implicitly fail: to miss nuance, to not quite nail the response, to be directionally right but unsatisfying. This approach suits use cases where users expect to iterate, to work with the agent toward a final outcome rather than receiving a perfect answer immediately.

Neither approach is universally correct. The right design depends on your use case, your users, and what you're optimizing for.

Here's a useful heuristic: if you find yourself going too broad, you probably haven't decomposed your problem enough. Ask yourself how a customer would do this task manually today. Walk through that process step by step. You'll usually find a comfortable compromise: a scope where you feel confident the agent will work for the use cases that really matter, but not so rigid that users continuously run up against limitations. Finding this balance is a core PM skill now.

### The Bitter Lesson and Its Implications

Rich Sutton's "Bitter Lesson" observes that over 70 years of AI research, general methods that leverage computation have consistently outperformed methods that encode human knowledge and structure. Chess engines that search deeply beat engines with sophisticated hand-crafted rules. Image recognition systems that learn from pixels outperform systems built on human-designed features.

The implication for agent design is nuanced. You shouldn't over-engineer rigid structures that prevent the model from leveraging its capabilities. Hand-crafted rules become bottlenecks as models improve. But you also can't just throw tools at a language model and hope it figures things out. That approach produces unreliable results and frustrated users.

The resolution: apply structure strategically at the right level. Don't over-structure the reasoning. Let the model decide how to approach problems within its domain. Do structure the requirements. Be explicit about inputs, outputs, success criteria, and boundaries. The structure you need isn't in clever prompt engineering or elaborate reasoning chains. It's in the product definition itself.

**This point cannot be overstated. The structure that matters is in how you define the problem, not in how you constrain the solution.**

## Part 2: How Language Models Actually Work

### The Noisy Channel Model

Think of language models as noisy channels for information transmission. You send a signal in (your prompt, your context, your instructions) and you receive a transformed signal out (the model's response). The "noise" in this channel is what we commonly call hallucination: any information in the output that wasn't grounded in the input.

This framing clarifies what language models are good at. They excel at compression: taking a large amount of context and distilling it into a focused output. They struggle at generation: producing reliable novel information from minimal input. When you ask a model to summarize a document, you're asking it to compress. When you ask it to write a detailed report from a vague prompt, you're asking it to generate, which means relying on its training data to fill in gaps you haven't specified.

For enterprise use cases where reliability matters, any information that emerges from the model's training rather than your provided context should be treated as noise. It might be correct (often it is) but it's unpredictable and unverifiable. You can't audit it against a source. You can't trace it back to ground truth.

**Design principle: structure your agents to perform compression tasks, not generation tasks. Provide rich context and ask for focused outputs.**

### The Information Ratio Problem

Here's the fundamental challenge with chat-based agents. When a user types "What's going on with Seismic?", they've provided ~29 bytes of information. To generate a useful response (an account overview with recent call summaries, deal status, engagement history, news) requires kilobytes of output grounded in tens of kilobytes of retrieved context.

The ratio of user input to required context is extremely low. The agent must expand that tiny input into a massive context retrieval, then compress all that context into a coherent response, with very little explicit guidance about what the user actually wants.

This expansion-compression process is where most failures occur. The user's query is ambiguous. The agent guesses wrong about what they mean. It retrieves irrelevant context. It misses important sources. It generates a response that's technically grounded in something but doesn't address what the user actually wanted.

Two solutions. First, embrace human-in-the-loop patterns. Treat every request as underspecified by default. Have the agent propose a plan before executing. Get user confirmation. This gathers more context and validates assumptions before committing to an expensive operation. Second, for high-frequency use cases, predefine what "good" looks like. Don't leave the agent to guess. Specify exactly what data sources to consult, in what order, and how to synthesize them.

### Context Quality and the 10x Rule

For reliable output, aim for retrieved context that's at least ten times the length of your expected output. If you want a 500-word account summary, you should be working with 5,000 or more words of retrieved context. This gives the model enough signal to compress into a high-quality response without relying on its training data to fill gaps.

Quantity isn't everything. Context quality matters enormously. Noisy, irrelevant, or redundant context degrades performance. The model has limited attention. If you fill the context window with low-value information, you dilute the signal you're trying to amplify.

**Feed the model steak, not popcorn.** Dense, relevant, high-quality context produces dense, relevant, high-quality outputs. Verbose, tangential, low-value context produces unreliable results.

Invest in context curation. Pre-process and filter retrieved data. Don't dump raw API responses into the context window. Summarize, re-rank, and select. The work you put into context quality pays dividends in output quality.

## Part 3: The Intern Model

### Two Ways to Train an Intern

Imagine you're training an intern. There are two approaches, and they produce very different outcomes.

**Rigid procedural instruction.** You give the intern a step-by-step checklist. When a customer asks about account status, do step one, then step two, then step three. Don't deviate. Don't improvise. Follow the procedure exactly.

This approach produces high confidence in a narrow domain. When the intern encounters a problem that fits the checklist, they'll almost certainly get it right. But anything that falls outside the checklist will cause them to stumble. They have no framework for reasoning about novel situations. They can only execute the procedure you gave them.

**Principled enablement.** You give the intern principles of what good looks like. You show them examples of successful outcomes and explain why they succeeded. You give them access to tools and resources. You teach them how to evaluate their own work. Then you let them reason through problems.

This approach produces moderate confidence across a broader domain. The intern can handle a wider variety of situations, adapt to novel inputs, and exercise judgment. But they'll make more mistakes. Their success rate at any single task is lower than the procedurally trained intern working within their narrow domain.

Both approaches are valid. For high-frequency, high-stakes tasks where you know exactly what good looks like and users expect it to work first time, rigid procedures make sense. For exploratory, variable tasks where flexibility matters and users expect to iterate, principled enablement makes sense.

### Applying This to Agent Design

When you design an agent capability, you're implicitly choosing between these approaches. If you define a strict workflow (always retrieve these data sources, always format the response this way, always follow this sequence) you're taking the rigid approach. You'll get high reliability within that workflow and unpredictable behavior outside it.

If you provide the agent with tools, examples, and principles (here's what good looks like, here are the resources available, here's how to evaluate success) you're taking the flexible approach. You'll get broader coverage but less predictable outcomes.

You can combine these approaches strategically. For the core use cases that matter most, where users will be frustrated if they fail, use more rigidity. Define exactly what happens. For the long tail of edge cases and novel requests, use principled enablement and accept that some will fail.

This is what shaping probability space means in practice. You're deciding where to invest in certainty and where to accept variance.

## Part 4: Role of AI PM

### Designing the Boundary

In traditional product management, your job is to specify what the product does. You write requirements, engineering builds them, QA verifies they work, and you ship. Success means the feature works as specified.

In agent-based product management, your job is to specify what the product does and where it's acceptable for it not to work. You're designing a boundary, not a feature. Inside the boundary, success is required. Outside the boundary, failure is acceptable, or at least expected and communicated.

This shift changes what a complete PRD looks like. It's not complete when you've specified the happy path. It's complete when you've specified which unhappy paths matter and which don't. Your release notes don't just describe what the feature does. They describe what it doesn't do, clearly, so users and stakeholders have appropriate expectations.

Most problems we've experienced with our agent platform trace back to implicit boundaries. Capabilities exist somewhere in the combination of prompts and tools, but no one has explicitly defined where success is required versus where failure is acceptable. When users hit failures, we don't know if we've failed or if they've stepped outside our designed boundary. When engineering delivers something that doesn't meet expectations, we can't point to clear requirements because we never wrote them.

Make boundaries explicit. For every capability you design, articulate the cases where it must succeed and the cases where it's acceptable to fail. Write them down. Review them with stakeholders. Communicate them in release notes.

### Critical Paths in GTM

There are a limited number of critical paths in GTM that we need to reliably solve. Account research. List building. Email writing. Contact lookup. Deal prioritization etc. These represent the majority of user interactions and the majority of user value.

Here's the important nuance: we're building agents that serve tens of thousands of users across diverse industries and use cases. One user might be selling medical devices, another enterprise software, another financial services. The contextual adaptation (how the agent adjusts for medical device sales versus software sales) is handled through user context, not through different agent capabilities. The core skill and capability of the agent remains the same. What changes is the contextual information it uses to perform that skill.

When we talk about shaping probability space for critical paths, we're not building separate agents for every industry. We're building agents that reliably perform core GTM tasks while contextually adapting based on user and tenant information.

Each critical path needs clear boundaries around what it means to be inside versus outside that path. Take prospecting. Prospecting is a core GTM use case, especially on ZoomInfo. But "prospecting" is too broad. You need to decompose it: list building is one capability, list prioritization is another, list enrichment is another. Maybe we build lists excellently but can't yet prioritize them. That boundary needs to be explicit.

Email writing is another example. "Email writing" as a category is far too broad. Do we write excellent cold outbound emails to net-new prospects? Do we write excellent follow-up emails for active deals? Do we write excellent emails to existing customers? These are fundamentally different jobs with different data requirements and different definitions of success.

A well-designed email capability might have a parent agent whose only job is routing. Is this a cold outbound email going to a net-new prospect? Is this an email to an active deal? Is this an email to an existing customer? Is this an email to a churned customer we're trying to win back? Each scenario routes to a sub-capability with its own shaped probability space, its own definition of success, its own boundaries.

If we've tuned our email writer for cold outbound, then active deal emails are out of scope until we explicitly build that capability. We can't tell customers we do "email" if we've only shaped the probability space for one type. When customers tell us they need deal emails, we build that capability properly. We don't add it to a vague prompt and hope the model figures it out.

### Task Decomposition

The most common mistake in agent design is treating a broad category as a single capability. "Email writing." "Prospecting." "Account research." These feel like discrete features because that's how we'd label them in a product menu. But each contains multitudes, and treating them as monolithic leads to agents that do many things poorly rather than a few things well.

Decomposition is the practice of breaking a broad capability into its constituent jobs, then treating each job as its own bounded problem. The goal is to reach a level of specificity where you can clearly define inputs, outputs, data requirements, and success criteria. If you can't write test cases, you haven't decomposed far enough.

Consider email writing. A first pass might identify it as a single capability: the agent writes emails. But observe how different the actual jobs are. A cold outbound email to a net-new prospect requires company research, persona inference, value proposition mapping, and a tone calibrated for first contact. An email to an active deal requires opportunity context, conversation history, objection tracking, and awareness of where the deal stands. An email to an existing customer requires account health data, product usage patterns, relationship history, and sensitivity to the ongoing partnership.

The decomposed design has a parent agent whose only job is classification. What type of email is this? Cold outbound, active deal, existing customer, win-back, partner communication? Based on the answer, it routes to a sub-capability built specifically for that job. Each sub-capability has its own probability space, its own data sources, its own success criteria, its own test cases. Each can be evaluated and improved independently.

This structure also makes boundaries enforceable. If you've built cold outbound but not active deal, the parent agent can recognize an active deal request and respond honestly: "I can help with cold outbound emails, but I'm not yet equipped for active deal follow-ups." or "I can do my best on this type of email, want me to try?" Users receive a clear answer rather than a hallucinated attempt. And when you do build active deal support, you add it as a new sub-capability without touching anything else.

"Account research" decomposes into account summary, competitive analysis, stakeholder mapping, recent activity review. Each level of decomposition trades breadth for depth, and you stop when you've reached a scope you can define precisely and execute reliably.

How do you know when to stop? Two tests. First, the manual test: could you write step-by-step instructions for how to accomplish this task? If the instructions remain vague ("research the account and write something relevant"), you haven't decomposed enough. Second, the test case test: can you write twenty specific input-output pairs that define success? If you can only write three or four, the scope is still too broad.

Decomposition feels like it slows you down. You're building five things instead of one. But the alternative is building one thing that fails in five different ways, with no clarity about which failure to fix first or how to evaluate whether you've fixed it. The decomposed approach compounds: each sub-capability you nail becomes a reliable building block. The monolithic approach thrashes: every improvement risks breaking something else, and you never reach a stable state.

Put another way, you've strengthened the probability space across five well defined use cases, that you can now evaluate and improve independently.

### Why Arbitrary Tool Reasoning Fails

A common pattern in agent development is to give the agent a broad prompt, a collection of tools, and let it reason about how to combine them. This feels elegant. It promises flexibility. Without proper boundaries, it fails.

To be clear: reasoning over tools is a legitimate and powerful pattern. ReAct-style agents that observe, reason, and act in loops can solve complex problems. The failure isn't in the pattern itself. The failure is in relying on model compute to reason over arbitrary tools without contextual guidance and shaping of the probability space.

The solution space becomes too large. With many tools and arbitrary queries, the combinatorial space is enormous. Without guidance about which tools are relevant for which types of queries, the agent makes plausible-seeming choices that turn out to be wrong. It calls tools in the wrong order, misinterprets results, generates responses that seem reasonable but miss the user's actual intent.

Failure modes become unpredictable. You can't anticipate all the ways unconstrained reasoning will go wrong. You can't write test cases for failures you haven't imagined. Users discover problems you never expected.

User frustration compounds fastest when the agent tries and fails rather than declining gracefully. Users don't mind when an agent says "I can't do that, but here's what I can help with." They hate when it says "let me try," runs for three minutes, and returns something wrong. The time investment amplifies disappointment. The appearance of effort without success erodes trust faster than honest refusal.

The solution isn't to abandon tool reasoning. It's to constrain and guide it. Shape the probability space so the agent knows which tools are relevant for which query types. Define the boundaries of what combinations make sense. Let the agent reason flexibly within those boundaries.

## Part 5: Human in the Loop

### Why Immediate Execution Fails

The current pattern for many of our agents: user submits request, agent executes immediately, user waits several minutes, result comes back wrong. This maximizes the cost of errors.

The problem is rooted in the information ratio. Users provide minimal input. The agent has to guess what they mean. When it guesses wrong (which happens often, because the input is ambiguous) the user has already invested time waiting. They're primed for disappointment.

### The Better Pattern

Every complex request should follow this flow: user submits request, agent interprets and proposes a plan, user confirms or corrects the plan, agent executes, agent shows result.

This pattern gathers more context. Even a simple "yes, that's right" doubles your confidence in the interpretation. A correction provides explicit guidance you didn't have before. It catches errors early, before investing in execution. It builds trust by keeping users involved and informed. It enables graceful rejection: if the agent can't fulfill the request, it can say so upfront rather than flailing through an execution that was doomed from the start.

The fear with human-in-the-loop is that it slows things down, adds friction, and annoys users. In practice, the opposite is true. Users vastly prefer quick confirmation dialogs to long waits followed by wrong results. The friction of approval is nothing compared to the friction of failure.

### When to Skip Confirmation

For simple, high-confidence operations, you can skip the confirmation step. A lookup that returns a single fact. A calculation with a clear answer. An operation where failure is immediately obvious and cheap to retry.

For anything involving multiple steps, data synthesis from multiple sources, or ambiguity in interpretation: plan first and confirm.

## Part 6: Writing Requirements for Agents

### The Vending Machine Test

Every agent capability you design should pass the vending machine test. A vending machine has clear inputs (specific coins and bills it accepts), clear outputs (you know exactly what you'll get), and clear boundaries (it doesn't try to make you a sandwich).

If your capability can't be described as "put X in, get Y out," with explicit definitions of valid X and expected Y, it's not ready for engineering. If you can't articulate what's in scope and what's out of scope, you haven't finished the design work.

### The Intern Test Restated

If you couldn't hand this task to a smart but literal-minded intern on their first day and have them execute it successfully (either by following your step-by-step instructions or by applying the principles and guidance you've provided) the agent won't be able to execute it either. The agent is that intern. It will do exactly what you tell it, interpret your principles as best it can, and work with the tools you've given it. If your instructions are ambiguous or your principles unclear, its behavior will be unpredictable.

### What the Requirements Must Include

For every agent capability, define inputs explicitly. What query patterns trigger this capability? What identifiers are required (account ID, contact ID, user context)? What's the minimum viable input?

Define the process explicitly. What data sources are consulted? Ideally in what order, though this may vary based on nuances in the user request? For what use cases does each data source become relevant? What transformations are applied? What reasoning steps occur? If you can't describe this, you can't build it yet.

For each agent you build, describe ten to fifteen workflows on the happy path: different variations of how success looks for different query types. Describe ten to fifteen workflows on the unhappy path: queries that should be rejected, queries that should trigger clarifying questions, queries that fall outside your boundaries. What happens when someone asks your email agent to file their taxes? That's an extreme example, but the principle matters for subtler cases too. What happens when someone asks your single-email agent to send emails to everyone on a list? Make these boundaries explicit. Tell the agent what it doesn't support.

Define outputs explicitly. What format is the response? What's always included? What's optional? How is uncertainty communicated?

Define boundaries explicitly. What queries should not trigger this capability? What happens if required data is missing? What are the known limitations? What should the agent tell users when it can't help?

### The Test Case Requirement

Before any engineering work begins, you need test cases. Writing test cases before building forces clarity that no amount of prose requirements can achieve. If you can't write the test cases, you don't understand the problem well enough to build a solution. The exercise exposes ambiguity, surfaces edge cases you hadn't considered, and creates a shared definition of success.

Test cases are the contract between product and engineering. If the agent passes these tests, it's done. If it fails, we know exactly what's broken and exactly what needs to be fixed. No ambiguity about whether we've succeeded.

## Part 7: The Process Change

### Old Way vs New Way

The old way of building agent capabilities: We write a vague requirement ("users should be able to build views from chat"), engineering makes it work for some definition of work, GTM discovers it doesn't work for their use cases, frustration and rework ensue. Everyone is disappointed.

The new way: PM identifies a specific job to be done and defines exactly how it gets accomplished (the intern test, the vending machine test, step by step). PM writes test cases before engineering begins, covering both happy paths and unhappy paths. PM reviews requirements with stakeholders and signs off on boundaries.

Then the PM tries to build the agent themselves. Using our agent platform, the PM attempts to create a working version of what they've specified. This surfaces problems that no amount of documentation can reveal. Does it fail because a required tool doesn't exist? Because a dataset isn't integrated? Because the reasoning doesn't flow the way the PM expected? The PM documents these shortcomings and iterates.

If the PM builds it and it works, we may not need engineering to build anything at all. We just need to productionize what the PM created. If the PM builds it and everything seems available but it's not quite working and they can't figure out why, that's when engineering comes in to help validate the approach and evaluate the test cases.

PMs should get as far as they can by themselves. Think through the problem properly, try building the solution, and only then bring in engineering with a clear understanding of what's working and what isn't. There will be a PRD review process with product leadership before we approve any agent for production.

In the old way, the agent was responsible for figuring out how to do the job. In the new way, the PM is responsible for figuring out how to do the job, and the agent executes the PM's design. The PM owns the intellectual work of defining what success looks like. The agent is an execution layer.

### Questions to Ask Before Building

Before proposing any agent capability, ask yourself:

- Can I describe this as a black box with clear inputs and outputs? If the boundary is fuzzy, the implementation will be fuzzy.
- Can I explain the step-by-step process to accomplish this task, or articulate the principles that should guide how it's done? If I handed these instructions to an intern, could they execute? If not, the agent can't execute either.
- Do I know which data sources are needed, ideally in what order, and for which use cases? If data requirements are unclear, context retrieval will be unreliable.
- Have I written at least 20 test cases (roughly half that must pass and half that must fail or redirect)? If I can't specify success, I can't evaluate success.
- Can I articulate what's not in scope? If everything is in scope, nothing will work well.
- Would I be comfortable telling a customer exactly what this does and doesn't do? If the answer is unclear to me, it will be unclear to users.

If any answer is uncertain, the capability isn't ready for engineering.

## Summary

Building AI agents requires a fundamental shift from deterministic to probabilistic thinking. Your job as a PM is to:

1. **Shape probability space** - Design clear boundaries for where success is required vs acceptable failure
2. **Decompose ruthlessly** - Break broad capabilities into specific, testable jobs
3. **Design the boundary, not the solution** - Structure the problem definition, not the reasoning
4. **Embrace human-in-the-loop** - Get confirmation before expensive execution
5. **Write test cases first** - 20+ cases covering happy and unhappy paths
6. **Build it yourself first** - Prototype using the platform before engaging engineering
7. **Be explicit about what's out of scope** - Users need to know what the agent can't do

The agent is an intern executing your design. If you can't explain the job clearly enough for an intern to succeed, the agent won't succeed either.