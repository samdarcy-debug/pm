---
id: doc-2026-004
title: Prompt Writing Guide for Product Managers
type: doc
status: draft
team: intelligence
owner: [[teams\ops\_people\brett-jacobs]]
created: 2026-01-13
updated: 2026-01-13
tags: []
related: []
---

# Prompt Writing Guide for Product Managers

**Author:** Adam Smith
**Date:** December 17, 2025

## The Mental Model

Think of a language model as a **noisy channel**. You send a signal in (your prompt and context) and you receive a transformed signal out (the response). The "noise" in this channel is any information in the output that wasn't grounded in your input. We call this hallucination, but it's more useful to think of it as noise that can be measured and managed.

This framing changes how you approach prompts. Your job isn't to write clever instructions and hope the model figures it out. **Your job is to maximize signal and minimize noise.** You do this by providing rich context, directing attention to what matters, and giving clear instructions with unambiguous success criteria.

**The core principle: LLMs excel at compression, not generation.** When you provide 10,000 tokens of context and ask for a 500 token summary, you're asking the model to compress. It has plenty of signal to work with. When you provide 50 tokens and ask for 2,000 tokens of output, you're asking the model to generate. It has to fill the gap with its training data, which introduces noise. Design for compression.

## The Three Components of a Prompt

Every effective prompt addresses three requirements: **context**, **attention**, and **instruction**.

### Context

Your prompt must contain all the information you expect to see in the output. If you want the response to reference specific account details, those details must be in the input. If you want the email to mention a recent product launch, that information must be provided. Never rely on the model's training data to fill gaps. That's where noise comes from.

Context quality matters as much as quantity. Dense, relevant information produces better results than verbose, tangential information. **Feed the model steak, not popcorn.** If your context is noisy (raw transcripts full of filler, unstructured data dumps, irrelevant documents mixed with relevant ones), consider a preprocessing step to clean and focus it before it reaches the prompt.

**The 10x rule:** aim for context that's at least ten times the length of your expected output. If you want a 500 word account summary, you should be working with 5,000 words of context. This gives the model enough signal to compress into something useful without relying on its training to fill gaps.

### Attention

Context alone isn't enough. You must tell the model which parts of the context matter for this specific task. Think of this as signal amplification. The model's attention is finite. If you dump 20,000 tokens of context without guidance, the model has to guess what's relevant.

Be explicit about what to focus on: "Pay particular attention to the recent call summaries and any mentions of budget concerns."

Be explicit about what to ignore: "Disregard the marketing collateral in the context. Focus only on the customer's own words."

This is especially important when your context contains mixed information, some relevant and some not. The model doesn't automatically know which is which. You have to tell it.

### Instruction

Finally, define the task itself. What transformation do you want? What rules govern the output? What format should it take?

Instructions can be explicit ("Always include the customer's industry in the first sentence") or implicit (providing examples that demonstrate the pattern you want). Both work. Explicit instructions are clearer. Implicit examples are often more effective for complex patterns that are hard to articulate in rules.

**The key test:** could you hand your instructions to a random person, along with the context and a sample output, and have them evaluate whether the output fulfilled the task? If your success criteria are ambiguous to a human evaluator, they're ambiguous to the model.

## Atomic Prompt Decomposition

Here's the practice that will most improve your prompt quality: **break your prompt into atomic assertions, and attach evaluation criteria to each one.**

An atomic assertion is a single instruction that makes one claim about how the agent should behave. "Always use formal business language" is an atomic assertion. "Be helpful and professional while maintaining a conversational tone that's appropriate for the user's seniority level" is not. It's multiple assertions bundled together, each with different (and potentially conflicting) success criteria.

For every atomic assertion, ask yourself: **how would I evaluate whether this is working?** If you can't articulate the evaluation criteria, the assertion is too vague to be useful. Either sharpen it or remove it.

### The Format

Think of each prompt line as having two parts: the instruction and its evaluation criteria.

**Instruction:** "Always cite the data source when referencing specific metrics or facts"

**Evaluation Criteria:**
- Does the output cite sources when mentioning specific numbers?
- Are the citations accurate (do they match the actual source)?
- Are citations present for all factual claims, not just some?

---

**Instruction:** "If required context is missing, acknowledge the gap rather than guessing"

**Evaluation Criteria:**
- When key data is absent, does the output explicitly note this?
- Does the output avoid fabricating information to fill gaps?
- Is the acknowledgment specific about what's missing?

---

**Instruction:** "Match the user's level of technical sophistication"

**Evaluation Criteria:**
- Does the output use technical terms appropriately for the audience?
- Does it avoid over-explaining to technical users?
- Does it avoid jargon when writing to non-technical users?

### Why This Matters

This practice **forces clarity**. If you can't write evaluation criteria for an instruction, the instruction is doing nothing useful. It's noise in your prompt.

It also **enables systematic evaluation**. When you run evals on agent output, you're not just asking "was this good?" You're asking specific questions: Did it cite sources? Did it acknowledge missing data? Did it match the user's sophistication level? Each atomic assertion becomes a dimension you can measure.

And it **enables prompt hygiene**. Over time, you accumulate assertions. Some contribute to output quality. Others don't. By evaluating at the atomic level, you can identify which assertions are actually doing work and remove the ones that aren't. Shorter, focused prompts generally outperform longer, bloated ones.

### Assertions That Don't Need Evaluation Criteria

Some assertions are foundational and don't require specific evaluation. "You are a GTM intelligence agent" is establishing identity, not making a behavioral claim. "The user is a sales development representative at a mid-market software company" is providing context. These don't need evaluation criteria because they're not instructions about behavior.

**The rule:** if the assertion tells the model to do something or behave in a certain way, it needs evaluation criteria. If it's providing context or establishing framing, it doesn't.

## Structuring the Prompt

A well-structured prompt has clear sections. The model processes prompts linearly, so order matters. Here's a structure that works:

1. **Identity and Role** - Who is this agent? What's its purpose? This establishes the frame for everything that follows.

2. **Context** - The information the agent needs to do its job. This is often the longest section, containing retrieved data, user information, conversation history, and relevant background.

3. **Task** - What specific thing are you asking the agent to do right now? Be precise.

4. **Behavioral Instructions** - The atomic assertions that govern how the agent should behave. Each one should be evaluable.

5. **Output Format** - What structure should the response take? If you want JSON, specify the schema. If you want prose, specify the length and style. If you want a particular sequence of sections, list them.

6. **Examples (if applicable)** - Few-shot examples that demonstrate the pattern you want. Examples are particularly effective when the desired behavior is complex or when natural language instructions would be ambiguous.

### Formatting Conventions

Use clear delimiters between sections. XML-style tags work well:

```xml
<role>
You are an account research agent...
</role>

<context>
{retrieved_account_data}
</context>

<task>
Generate a pre-call briefing for the upcoming meeting...
</task>

<instructions>
- Always cite the data source when referencing specific facts
- If recent call data is unavailable, explicitly note this gap
- Match the formality level to the user's role
</instructions>

<output_format>
Respond with a briefing document containing:
1. Account overview (2-3 sentences)
2. Key contacts and their roles
3. Recent activity summary
4. Recommended talking points
</output_format>
```

The model will follow this structure. Inconsistent or ambiguous formatting introduces noise.

## Prompt Caching

Modern LLM APIs cache token prefixes. If the first N tokens of your prompt match a recent request, those tokens are served from cache rather than reprocessed. This is dramatically cheaper and faster. But it only works if the beginning of your prompt is stable across runs.

**The implication for prompt structure: static content first, dynamic content last.**

### What stays the same across runs:
- Identity and role definition
- Behavioral instructions
- Output format specifications
- Few-shot examples
- Tool definitions

### What changes per request:
- Retrieved context (account data, call summaries, etc.)
- User query
- Conversation history
- Session-specific information

Structure your prompt so all the stable elements come first, in the same order every time. Then append the dynamic, request-specific content at the end.

```xml
<role>
You are an account research agent for GTM intelligence...
[STATIC - same every request]
</role>

<instructions>
- Always cite data sources when referencing specific facts
- If recent call data is unavailable, explicitly note this gap
- Match formality to the user's role
[STATIC - same every request]
</instructions>

<output_format>
Respond with a briefing containing...
[STATIC - same every request]
</output_format>

<examples>
[Example 1]
[Example 2]
[STATIC - same every request]
</examples>

<context>
{retrieved_account_data}
[DYNAMIC - changes per request]
</context>

<user_query>
{user_message}
[DYNAMIC - changes per request]
</user_query>
```

With this structure, if your static prefix is 3,000 tokens and your dynamic context is 2,000 tokens, every request after the first serves those 3,000 tokens from cache. At scale, this compounds into significant cost and latency savings.

**The mistake to avoid:** putting dynamic content early (like the user's query or retrieved context at the top), then following with instructions. This breaks caching entirely because the prefix changes every request.

Think of it as: **instructions are the frame, context fills the frame.** Define the frame first, then fill it.

## Common Failure Patterns

**Too little context, too much expected output** - You're asking for generation, not compression. The model will fill gaps with its training data, introducing noise. Either provide more context or reduce output expectations.

**Conflicting instructions** - "Be concise" and "be thorough" are in tension. "Use casual language" and "maintain professionalism" can conflict. When you have atomic assertions with evaluation criteria, these conflicts become obvious. Without that discipline, they hide in the prompt and cause unpredictable behavior.

**Vague success criteria** - "Write a good email" is not an instruction. Good by what standard? For what audience? With what constraints? The model will interpret "good" according to its training distribution, which may not match your intent.

**Context without attention guidance** - Dumping 50,000 tokens of context without telling the model what matters is like handing someone a filing cabinet and asking for a summary. They'll pick something, but it might not be what you wanted.

**Instructions that can't be evaluated** - "Be helpful" sounds nice but means nothing measurable. "Respond to the user's actual question rather than a related question" is evaluable. Every instruction should have a clear success/failure condition.

## The Iteration Loop

Good prompts are not written, they're iterated. The process:

1. Write initial prompt with atomic assertions and evaluation criteria
2. Run against test cases
3. Evaluate each assertion: Is it contributing to output quality? Is it being followed?
4. Remove assertions that aren't doing work
5. Add or refine assertions where outputs are failing
6. Repeat

This is methodical, not trial-and-error. Because you have evaluation criteria for each assertion, you can diagnose failures precisely. The output didn't cite sources? That assertion isn't working. The output is too verbose? You need a length constraint assertion, or your existing one isn't strong enough.

Over time, you develop intuition for what works. But even with intuition, the discipline of atomic decomposition and explicit evaluation keeps your prompts clean and your iterations productive.

## Summary

The goal is to maximize signal and minimize noise. You do this by:

- Providing rich context (the 10x rule)
- Directing attention to what matters
- Giving clear instructions with unambiguous success criteria
- Decomposing prompts into atomic assertions, each with evaluation criteria
- Structuring prompts with static content first, dynamic content last (for caching)
- Using clear sections and consistent formatting
- Iterating based on systematic evaluation

**Prompts are not magic incantations. They're engineering artifacts. Treat them with the same rigor you'd apply to any other system specification.**

