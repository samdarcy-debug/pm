---
id: weekly-mcp-2025-36
title: "MCP Weekly Report - September 06, 2025"
type: weekly-report
status: approved
team: mcp
owner:
created: 2025-09-06
updated: 2026-01-06
week_ending: 2025-09-06
reporting_period: "September 2-6, 2025"
tags: ["weekly-report", "Q32025"]
---

# **MCP Team Executive Roundup - September 5th, 2025**

## **Executive Summary**

The MCP team achieved 100% of planned goals plus additional deliverables
this week, successfully demonstrating end-to-end tool orchestration with
Claude desktop querying both semantic data and advanced search agents.
This milestone represents six months of foundational work coming to
fruition, with Rowan Bailey describing it as \"a real cherry on top\"
and the project he\'s most excited about. The team now has working
GraphQL implementations, public tool exposure capabilities, and live
agent-to-agent communication - positioning us perfectly for Dreamforce
demonstrations and broader rollout.

## **This Week\'s Progress**

### **Key Momentum Areas**

Carter Vanhuss successfully wired the semantic data agent with Claude
desktop, demonstrating multi-tool orchestration where Claude queries the
advanced search agent to get company IDs, then uses those results to
query the semantic data agent for deeper insights. This \"deep research
over semantic data\" capability shows Claude making intelligent
decisions about which tools to use and chaining queries together - a
critical capability that\'s been six months in the making.

Topher Dennis delivered GraphQL implementations with swagger
documentation, providing both programmatic access and user-friendly
testing interfaces with pre-populated staging IDs for immediate
validation. The financial filings endpoint is now operational using
GraphQL, with performance showing promising results including potential
caching benefits that improve response times after initial queries.

Zheng Zhong created an elegant solution for exposing internal tools to
public users through configuration files and feature flags, allowing
tenant-specific tool visibility. The implementation allows tools to
appear or disappear based on tenant configuration, providing the
flexibility needed for controlled rollouts and customer-specific
experiences while maintaining security boundaries.

### **Goals & Progress**

**GraphQL Migration**: One query fully migrated to GraphQL with
financial filings endpoint complete and operational. Topher has built
comprehensive swagger documentation making the APIs discoverable and
testable. 3-4 additional endpoints remain for conversion next week, with
the team exploring potential consolidation into a single GraphQL
endpoint to reduce tool proliferation. The lack of GraphQL team
documentation required extra discovery effort, but Topher \"spent extra
hours figuring this out\" to maintain momentum.

**Semantic Data Integration**: Carter\'s semantic data agent integration
is fully operational in Claude desktop, successfully performing complex
multi-hop queries across tools. The system demonstrates intelligent tool
selection and query chaining, with Claude making multiple calls and
using results from one query to inform subsequent queries. Test accounts
identified include Apple, Sisense, Invideo, and UserTesting for
comprehensive validation.

**Public Tool Exposure**: Zheng\'s configuration-based approach for
exposing internal tools is complete and demonstrated, using downstream
MCP server configuration and JSON tagging to mark tools as
public-facing. The feature flag system provides tenant-level control,
with tools automatically appearing or disappearing based on tenant
configuration - described by Rowan as \"super elegant.\"

### **Strategic Challenges**

The GraphQL team\'s lack of documentation created significant discovery
overhead, with the schema alone containing 77,000 rows that required
manual parsing to identify useful query construction patterns. This
blind spot extended timelines but was overcome through additional effort
from Topher, highlighting the need for better cross-team documentation
standards when building on shared infrastructure.

The question of tool proliferation versus consolidation remains open,
with the team needing to balance between specific, well-defined GraphQL
queries and a more flexible single endpoint approach. Rowan expressed
concern about \"tripping up the orchestrator\" with too many tools,
especially as multiple CPAs each with underlying tools get added to the
system.

Batch operations across all tools are needed to improve user experience,
as current sequential processing (enriching contacts one at a time)
creates a \"cumbersome experience\" that could be parallelized. Young
will focus on making the API more efficient with batch support as a
priority for the coming weeks.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The successful demonstration of agent-to-agent communication validates
the microservices architecture approach, where specialized agents handle
domain-specific queries and compress responses before returning to the
orchestrator. This pattern prevents context window explosion while
maintaining query sophistication, as demonstrated by the semantic data
agent\'s ability to iterate up to five times on a single query.

Testing revealed that Claude\'s ability to intelligently chain tool
calls exceeds initial expectations, with the system autonomously
deciding to query the advanced search agent first to obtain IDs before
querying semantic data. This emergent behavior suggests the
orchestration layer is more sophisticated than anticipated and can
handle complex research workflows without explicit programming.

The combination of REST endpoints wrapped as tools and direct GraphQL
access provides flexibility in abstraction levels, allowing the team to
start with specific implementations while exploring consolidation
opportunities. This dual approach enables immediate testing of use cases
while the optimal architecture emerges through usage patterns.

### **Cross-Team Dependencies**

Collaboration with Frank\'s team on the actual MCP gateway
implementation is upcoming, with Young/Zheng assigned to this
integration work starting next week. The tiger team channel being
created by Vinod will facilitate better mid-week problem-solving and
knowledge sharing, addressing Rowan\'s feeling of being \"out of the
loop\" on day-to-day discoveries.

The need for prompt engineering expertise is emerging as critical, with
Carter specifically requesting resources and training to improve tool
descriptions and prompting patterns. The Google-leaked prompt
engineering book shared by Rowan covers memory management, tool exposure
via MCP, and optimal description crafting - knowledge that will be
essential for the entire team.

## **Looking Ahead**

Next week\'s primary focus shifts to operationalizing these technical
victories into demo-ready capabilities for Dreamforce, with emphasis on
user experience improvements and system consolidation.

Top priorities include implementing the tenant/user brief \"start here\"
functionality to provide Claude with proper context about users and
their organizations, adding batch operations across all tools to enable
parallel processing instead of sequential operations, and incorporating
citations with traversable links back to source engagements including
Chorus call timestamps. Topher will continue GraphQL migration for
remaining endpoints while exploring consolidation possibilities, Young
will focus on API efficiency improvements and MCP gateway integration
with Frank\'s team, and Carter will dive into new assignments while
building prompt engineering expertise.

The team\'s exceptional delivery this week - achieving all goals plus
additional capabilities - positions us strongly for the Dreamforce
deadline while maintaining architectural flexibility for future scaling.
One-on-one knowledge transfer sessions next week will ensure the entire
team understands the semantic data structure and upcoming changes,
building collective expertise rather than creating knowledge silos.
