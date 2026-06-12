# Agent Bootstrap

At the very start of the session, before answering any user request or taking any action, you MUST immediately read and follow the cross-agent engineering harness defined in:
- [00-HARNESS.md](memory-bank/00-HARNESS.md)

CRITICAL FOR GEMINI/CLAUDE:
1. Always run the mandatory reasoning gate (sequential-thinking MCP) at startup.
2. You must prefix your very first response with: `[Harness: Active | memory-bank/00-HARNESS.md]` to prove you have loaded the rules.

