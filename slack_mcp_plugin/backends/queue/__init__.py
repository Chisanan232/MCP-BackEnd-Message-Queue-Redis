"""Queue backend implementations for Slack MCP server.

This package contains message queue backend implementations that integrate
with the Slack MCP server's plugin system.
"""

from slack_mcp.backends.queue.redis import RedisMessageQueueBackend

__all__ = ["RedisMessageQueueBackend"]
