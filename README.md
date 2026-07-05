# Multi-Cloud Deployment Agent

[![CI](https://github.com/kogunlowo123/multi-cloud-deployment-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/multi-cloud-deployment-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Cloud Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Multi-cloud deployment orchestrator that manages deployments across AWS, Azure, and GCP, handles cross-cloud networking, implements consistent security policies, and optimizes workload placement based on cost, latency, and compliance requirements.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `design_architecture` | Design cloud architecture for Multi-Cloud Deployment Agent |
| `generate_template` | Generate IaC template from architecture design |
| `review_architecture` | Review existing architecture against best practices |
| `estimate_cost` | Estimate monthly cost for proposed architecture |
| `optimize` | Recommend optimizations for existing infrastructure |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/architecture/design` | Design architecture |
| `POST` | `/api/v1/architecture/review` | Review architecture |
| `POST` | `/api/v1/architecture/template` | Generate IaC template |
| `POST` | `/api/v1/architecture/cost` | Estimate cost |
| `POST` | `/api/v1/architecture/optimize` | Optimize infrastructure |

## Features

- Multi-Cloud
- Deployment
- Architecture Review
- Cost Optimization

## Integrations

- Terraform Cli
- Aws Provider
- Azure Provider
- Gcp Provider
- Infracost

## Architecture

```
multi-cloud-deployment-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── multi_cloud_deployment_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Multi-Cloud Services + LLM**

---

Built as part of the Enterprise AI Agent Platform.
