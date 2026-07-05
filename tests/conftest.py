"""Test configuration for Multi-Cloud Deployment Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "multi-cloud-deployment-agent", "category": "Cloud Engineering"}
