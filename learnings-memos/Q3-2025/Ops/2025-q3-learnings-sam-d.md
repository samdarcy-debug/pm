---
id: learnings-2025-037
title: Q3 2025 Learnings Memo - Sam D
type: doc
status: approved
team: ops
owner: '[[teams/ops/_people/sam-d]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- ops
related: []
---
#### **Metric Alignment**



The primary metric my work is driving towards is SIgnal ROI. By creating

a tool that allows PM's to semantically search through customer call

transcripts, they can get feedback directly from customers and

understand various signals from pain points to features customers love.

I have received 5 different slack messages from various PM's interested

in testing out the VoC tool and now that we have a path forward I am

excited to get them in and testing ideally this/next week.



#### **Key Learnings**



My key learnings were around the nature of our internal infrastructure

ecosystems and how different teams interact with each other.

Programmatically speaking, we exist in separate bubbles that cannot

intersect. This is a very tough challenge as we are a Product team,

deploying code through the Engineering team, using backend data from the

Semantic Data team. That said, by combining ZI Chat microapps with the

Semantic Data team's Agentic Platform, we now have a full

frontend/backend solution that meets all critical infrastructure,

networking, and security standards. This is the platform we can use to

build internal tools going forward without being blocked.



#### **Hypotheses & Results**



#### I had assumed that by creating applications using industry standard tools and frameworks that I would be able to deploy my app to GCP without issue. I quickly learned that this is not something we can easily do within our team and have worked with several heads of various teams to find a solution. 



#### **Go-forward Changes & Plan**



I am very excited about this next quarter as I now finally have A) a

solid understanding of the internal teams and ecosystem within ZI and B)

a working formula for building apps with backend/frontend compatibility.

Going forward I plan on launching the VoC microapp and connecting the

Product Knowledge Graph to ZI Chat this quarter.



#### **Leveraging AI**  One of the most impactful uses of AI I found was the adding LLM reasoning to knowledge graph traversal. We are able to now break our documents and internal notes into isolated, traceable ideas and relationships. We can then attach LLM's to our graph to actually step across these relationships and get a richer understanding of our processes and documents, leading to higher quality responses and results.  Demo here: [[KG_LLM_Traversal.mov]{.underline}](https://drive.google.com/file/d/1HefluslOO9nSq7cT1PxDQ0xQihb8JL59/view?usp=drive_link)  In addition to this tool, Sonnet 4.5 has shown a real improvement in programmatic reasoning and I will continue to utilize AI in my engineering tasks to be more productive as an engineer.

