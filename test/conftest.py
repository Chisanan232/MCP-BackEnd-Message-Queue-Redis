"""Pytest configuration and shared fixtures for all tests.

This module provides common fixtures and configuration for both unit
and integration tests.
"""

import asyncio
import logging
import os
from typing import Generator

import pytest

# Configure logging for tests
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)


@pytest.fixture(scope="session")
def event_loop_policy() -> asyncio.AbstractEventLoopPolicy:
    """Use the default event loop policy for all tests."""
    return asyncio.get_event_loop_policy()


@pytest.fixture(scope="function")
def event_loop(event_loop_policy: asyncio.AbstractEventLoopPolicy) -> Generator:
    """Create an event loop for each test function."""
    loop = event_loop_policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def reset_env_vars() -> Generator:
    """Reset environment variables before each test.

    This ensures tests don't interfere with each other through
    environment variable side effects.
    """
    # Save current environment
    original_env = dict(os.environ)

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def redis_url() -> str:
    """Provide Redis URL for tests."""
    return os.getenv("REDIS_URL", "redis://localhost:6379/1")


@pytest.fixture
def mock_slack_event() -> dict:
    """Provide a sample Slack event for testing."""
    return {
        "token": "test-token",
        "team_id": "T123456",
        "api_app_id": "A123456",
        "event": {
            "type": "message",
            "user": "U123456",
            "text": "Hello, World!",
            "ts": "1234567890.123456",
            "channel": "C123456",
            "event_ts": "1234567890.123456",
        },
        "type": "event_callback",
        "event_id": "Ev123456",
        "event_time": 1234567890,
    }


@pytest.fixture
def mock_slack_command() -> dict:
    """Provide a sample Slack command for testing."""
    return {
        "token": "test-token",
        "team_id": "T123456",
        "team_domain": "test-team",
        "channel_id": "C123456",
        "channel_name": "general",
        "user_id": "U123456",
        "user_name": "testuser",
        "command": "/test",
        "text": "hello",
        "response_url": "https://hooks.slack.com/commands/123/456",
        "trigger_id": "123.456.789",
    }
