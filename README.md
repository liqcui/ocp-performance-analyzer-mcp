# OCP Performance Analyzer MCP

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-orange)](https://modelcontextprotocol.io)
[![Demo](https://img.shields.io/badge/Demo-Online-brightgreen)](https://liqcui.github.io/ocp-performance-analyzer-mcp/)

A comprehensive, AI-powered performance analysis and monitoring platform for OpenShift/Kubernetes clusters. This project provides Model Context Protocol (MCP) servers for analyzing etcd, network, and OVN-Kubernetes components with deep performance insights, automated root cause analysis, and actionable recommendations.

## 🎬 Live Demo

**[Try the Interactive Demo →](https://liqcui.github.io/ocp-performance-analyzer-mcp/)**

Experience the full capabilities of OCP Performance Analyzer MCP with our online demo:
- 🤖 AI-powered chat interface with 9 realistic scenarios
- 📊 Complete system architecture visualization
- 🔍 Real-world performance analysis examples
- 📖 Comprehensive documentation and guides

**Quick Links:**
- [Interactive Demo](https://liqcui.github.io/ocp-performance-analyzer-mcp/) - Full AI chat simulation
- [Documentation Demo](https://liqcui.github.io/ocp-performance-analyzer-mcp/demo.html) - Project overview
- [Demo Guide](DEMO.md) - How to use the demos

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Components](#components)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Overview

The OCP Performance Analyzer MCP is a multi-component platform designed to monitor and analyze OpenShift/Kubernetes cluster performance across three main areas:

1. **ETCD Analyzer** - Comprehensive etcd cluster performance monitoring
2. **Network Analyzer** - Network stack performance analysis (L1, sockets, netstat, I/O)
3. **OVN-Kubernetes Analyzer** - OVN-Kubernetes networking component analysis

Each component includes:
- MCP servers exposing performance analysis tools
- AI-powered agents for intelligent analysis and reporting
- Data collection tools for Prometheus metrics
- ELT (Extract-Load-Transform) pipelines for data processing
- Persistent storage using DuckDB
- Web interfaces for interactive analysis

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Layer                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Web UI     │  │   CLI Tools   │  │   REST API    │    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘    │
└─────────┼─────────────────┼─────────────────┼─────────────┘
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
┌───────────────────────────┼───────────────────────────────┐
│                    AI Agent Layer (Port 8080)              │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  LangGraph Agents: Chat, Report, Storage            │  │
│  │  • Streaming responses                              │  │
│  │  • Tool orchestration                               │  │
│  │  • Conversation memory                              │  │
│  └─────────────────────────────────────────────────────┘  │
└───────────────────────────┬───────────────────────────────┘
                            │ MCP Protocol
┌───────────────────────────┼───────────────────────────────┐
│                    MCP Server Layer (Port 8000)            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ ETCD Server  │  │ Network Server│  │ OVNK Server   │  │
│  │ 15+ tools    │  │ 10+ tools     │  │ 8+ tools      │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
└─────────┼─────────────────┼─────────────────┼─────────────┘
          │                 │                 │
┌─────────┼─────────────────┼─────────────────┼─────────────┐
│          │                 │                 │             │
│  ┌───────▼───────┐  ┌───────▼───────┐  ┌───────▼───────┐ │
│  │   Tools/      │  │   Tools/       │  │   Tools/      │ │
│  │   Collectors  │  │   Collectors   │  │   Collectors  │ │
│  └───────┬───────┘  └───────┬───────┘  └───────┬───────┘ │
│          │                 │                 │             │
│  ┌───────▼───────┐  ┌───────▼───────┐  ┌───────▼───────┐ │
│  │   Analysis    │  │   Analysis    │  │   Analysis    │ │
│  │   Modules     │  │   Modules     │  │   Modules     │ │
│  └───────┬───────┘  └───────┬───────┘  └───────┬───────┘ │
│          │                 │                 │             │
│  ┌───────▼───────┐  ┌───────▼───────┐  ┌───────▼───────┐ │
│  │   ELT         │  │   ELT          │  │   ELT         │ │
│  │   Pipeline    │  │   Pipeline     │  │   Pipeline    │ │
│  └───────┬───────┘  └───────┬───────┘  └───────┬───────┘ │
│          │                 │                 │             │
│  ┌───────▼─────────────────▼─────────────────▼───────┐   │
│  │              Storage Layer (DuckDB)                 │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│         OpenShift/Kubernetes Cluster Infrastructure        │
│  • ETCD Cluster    • Prometheus    • Kubernetes API        │
│  • Master Nodes    • OVN-Kubernetes • Network Components   │
└─────────────────────────────────────────────────────────────┘
```

### Component Architecture

Each analyzer (etcd, network, ovnk) follows a consistent architecture:

1. **MCP Server** - FastMCP-based server exposing analysis tools
2. **Tools/Collectors** - Specialized metric collectors for Prometheus queries
3. **Analysis Modules** - Performance analysis and bottleneck detection
4. **ELT Pipeline** - Data transformation and HTML table generation
5. **Storage Modules** - DuckDB persistence for historical data
6. **AI Agents** - LangGraph-based agents for intelligent analysis

## Features

### Core Capabilities

- **Multi-Component Analysis**: ETCD, Network, and OVN-Kubernetes analyzers
- **MCP Protocol**: Model Context Protocol servers for tool exposure
- **AI-Powered**: LangGraph agents with OpenAI integration
- **Real-time Monitoring**: Live metrics collection and analysis
- **Historical Analysis**: DuckDB-based time-series storage
- **Automated Reporting**: Executive-ready performance reports
- **Web Interfaces**: Interactive chat and analysis UIs
- **Streaming Responses**: Real-time result streaming via SSE

### ETCD Analyzer Features

- **15+ Analysis Tools**: Cluster status, WAL fsync, backend commit, disk I/O, network I/O, node usage
- **Deep Drive Analysis**: Multi-subsystem comprehensive review
- **Bottleneck Detection**: Automated performance issue identification
- **Performance Reports**: Executive summaries with recommendations
- **Critical Metrics**: WAL fsync P99 (<10ms), backend commit P99 (<25ms)

### Network Analyzer Features

- **10+ Analysis Tools**: L1 stats, socket statistics (TCP/UDP/IP/mem/softnet), netstat, network I/O
- **Multi-Layer Analysis**: Physical layer to application layer metrics
- **Performance Metrics**: Throughput, latency, packet statistics, connection tracking
- **Comprehensive Coverage**: 95+ network metrics across 9 categories

### OVN-Kubernetes Analyzer Features

- **8+ Analysis Tools**: OVN database, kubelet CNI, latency, OVS usage, pod metrics, API stats
- **OVN-Specific Metrics**: Northbound/Southbound database sizes, sync performance
- **CNI Analysis**: Kubelet and CNI performance metrics
- **OVS Monitoring**: Open vSwitch daemon and flow table statistics

### Shared Features

- **Configuration Management**: YAML-based metrics configuration (11 metric files)
- **Authentication**: OpenShift/Kubernetes cluster authentication
- **Prometheus Integration**: Direct PromQL query execution
- **Data Visualization**: HTML table generation with highlighting
- **Export Capabilities**: Reports, data exports, historical queries

## Project Structure

```
ocp-performance-analyzer-mcp/
│
├── analysis/                    # Performance analysis modules
│   ├── etcd/                    # ETCD-specific analysis
│   │   ├── etcd_performance_deepdrive.py
│   │   └── etcd_performance_report.py
│   ├── net/                     # Network analysis (future)
│   ├── node/                    # Node analysis (future)
│   ├── ovnk/                    # OVN-Kubernetes analysis (future)
│   └── utils/                   # Shared analysis utilities
│       └── analysis_utility.py
│
├── config/                      # Configuration management
│   ├── metrics_config_reader.py # Unified metrics loader
│   ├── metrics-alert.yml        # Alert metrics
│   ├── metrics-api.yml          # API server metrics
│   ├── metrics-cni.yml          # CNI metrics
│   ├── metrics-disk.yml         # Disk I/O metrics
│   ├── metrics-etcd.yml         # ETCD metrics (51 metrics)
│   ├── metrics-latency.yml      # Latency metrics
│   ├── metrics-net.yml           # Network metrics (95 metrics)
│   ├── metrics-node.yml          # Node metrics
│   ├── metrics-ovn.yml           # OVN metrics
│   ├── metrics-ovs.yml           # OVS metrics
│   ├── metrics-pods.yml          # Pod metrics
│   ├── README.md                 # Config documentation
│   └── test_metrics_loading.py   # Configuration tests
│
├── elt/                         # Extract-Load-Transform pipeline
│   ├── etcd/                    # ETCD ELT modules
│   │   ├── analyzer_elt_backend_commit.py
│   │   ├── analyzer_elt_bottleneck_analysis.py
│   │   ├── analyzer_elt_cluster_status.py
│   │   ├── analyzer_elt_compact_defrag.py
│   │   ├── analyzer_elt_general_info.py
│   │   ├── analyzer_elt_performance_deep_drive.py
│   │   ├── analyzer_elt_wal_fsync.py
│   │   └── etcd_analyzer_elt_*.py
│   ├── net/                     # Network ELT modules
│   │   ├── analyzer_elt_network_io.py
│   │   ├── analyzer_elt_network_l1.py
│   │   ├── analyzer_elt_network_netstat4*.py
│   │   └── analyzer_elt_network_socket4*.py
│   ├── node/                    # Node ELT modules
│   │   └── analyzer_elt_node_usage.py
│   ├── ocp/                     # OCP cluster ELT modules
│   │   ├── analyzer_elt_cluster_alert.py
│   │   ├── analyzer_elt_cluster_apistats.py
│   │   └── analyzer_elt_cluster_info.py
│   ├── ovnk/                    # OVN-Kubernetes ELT modules
│   │   ├── analyzer_elt_deepdrive.py
│   │   ├── analyzer_elt_kubelet_cni.py
│   │   ├── analyzer_elt_latency.py
│   │   └── analyzer_elt_ovs.py
│   ├── pods/                    # Pod ELT modules
│   │   └── analyzer_elt_pods_usage.py
│   ├── disk/                    # Disk ELT modules
│   │   └── analyzer_elt_disk_io.py
│   └── utils/                   # ELT utilities
│       ├── analyzer_elt_json2table.py  # Generic orchestrator
│       ├── analyzer_elt_utility.py      # Pure utilities
│       └── README.md                    # ELT documentation
│
├── mcp/                         # MCP servers and agents
│   ├── etcd/                    # ETCD analyzer MCP server
│   │   ├── etcd_analyzer_mcp_server.py      # Main MCP server
│   │   ├── etcd_analyzer_client_chat.py     # Chat client (FastAPI)
│   │   ├── etcd_analyzer_mcp_agent_report.py    # Report agent
│   │   ├── etcd_analyzer_mcp_agent_stor2db.py   # Storage agent
│   │   ├── etcd_analyzer_command.sh             # Management script
│   │   ├── etcd_analyzer_cluster.duckdb         # DuckDB database
│   │   ├── exports/                             # Report exports
│   │   ├── logs/                                # Application logs
│   │   ├── storage/                             # Storage modules
│   │   ├── pyproject.toml                       # Package config
│   │   └── README.md                            # ETCD docs
│   ├── net/                     # Network analyzer MCP server
│   │   ├── network_analyzer_mcp_server.py
│   │   ├── network_analyzer_client_chat.py
│   │   ├── network_analyzer_mcp_command.sh
│   │   ├── exports/
│   │   ├── logs/
│   │   └── storage/
│   └── ovnk/                    # OVN-Kubernetes analyzer MCP server
│       ├── ovnk_analyzer_mcp_server.py
│       ├── ovnk_analyzer_mcp_client_chat.py
│       ├── ovnk_analyzer_mcp_command.sh
│       ├── exports/
│       ├── logs/
│       ├── storage/
│       └── README.md
│
├── ocauth/                      # OpenShift authentication
│   └── openshift_auth.py        # K8s/OCP auth, token management
│
├── storage/                     # DuckDB storage modules
│   ├── etcd/                    # ETCD storage modules
│   │   ├── analyzer_stor_backend_commit.py
│   │   ├── analyzer_stor_cluster_info.py
│   │   ├── analyzer_stor_compact_defrag.py
│   │   ├── analyzer_stor_disk_io.py
│   │   ├── analyzer_stor_disk_wal_fsync.py
│   │   ├── analyzer_stor_general_info.py
│   │   ├── analyzer_stor_network_io.py
│   │   └── analyzer_stor_utility.py
│   ├── net/                     # Network storage (future)
│   └── ovnk/                    # OVN-Kubernetes storage (future)
│
├── tools/                       # Metric collection tools
│   ├── etcd/                    # ETCD collectors
│   │   ├── etcd_cluster_status.py
│   │   ├── etcd_general_info.py
│   │   ├── etcd_disk_wal_fsync.py
│   │   ├── etcd_disk_backend_commit.py
│   │   └── etcd_disk_compact_defrag.py
│   ├── net/                     # Network collectors
│   │   ├── network_io.py
│   │   ├── network_l1.py
│   │   ├── network_netstat4tcp.py
│   │   ├── network_netstat4udp.py
│   │   ├── network_socket4tcp.py
│   │   ├── network_socket4udp.py
│   │   ├── network_socket4ip.py
│   │   ├── network_socket4mem.py
│   │   └── network_socket4softnet.py
│   ├── node/                    # Node collectors
│   │   └── node_usage.py
│   ├── ocp/                     # OCP collectors
│   │   ├── cluster_info.py
│   │   ├── cluster_apistats.py
│   │   └── cluster_alert.py
│   ├── ovnk/                    # OVN-Kubernetes collectors
│   │   ├── ovnk_baseinfo.py
│   │   ├── ovnk_kubelet_cni.py
│   │   ├── ovnk_latency.py
│   │   └── ovnk_ovs_usage.py
│   ├── pods/                    # Pod collectors
│   │   └── pods_usage.py
│   ├── disk/                    # Disk collectors
│   │   └── disk_io.py
│   └── utils/                   # Shared utilities
│       ├── promql_basequery.py  # Base Prometheus queries
│       └── promql_utility.py     # PromQL helpers
│
├── webroot/                     # Web interfaces
│   ├── etcd/                    # ETCD web UI
│   │   └── etcd_analyzer_mcp_llm.html
│   ├── net/                     # Network web UI
│   │   └── network_analyzer_mcp_llm.html
│   └── ovnk/                    # OVN-Kubernetes web UI
│       └── ovnk_analyzer_mcp_llm.html
│
├── exports/                     # Generated reports and exports
├── logs/                        # Application logs
├── pyproject.toml               # Main project configuration
├── LICENSE                      # License file
└── README.md                    # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Access to OpenShift/Kubernetes cluster
- KUBECONFIG configured
- Prometheus/Thanos accessible
- OpenAI API key (for AI features)

### Step 1: Clone Repository

```bash
git clone https://github.com/liqcui/ocp-performance-analyzer-mcp.git
cd ocp-performance-analyzer-mcp
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### Step 3: Install Dependencies

```bash
pip install -e .
```

Or install from the root `pyproject.toml`:

```bash
pip install -r requirements.txt  # If available
```

**Key Dependencies:**
- `fastmcp>=1.12.4` - MCP server framework
- `fastapi>=0.115.7` - Web framework
- `langchain>=0.3.0` - LLM integration
- `langgraph>=0.3.0` - Agent orchestration
- `duckdb>=1.0.0` - Time-series database
- `kubernetes>=30.0.0` - Kubernetes client
- `prometheus-api-client>=0.5.3` - Prometheus queries
- `pydantic>=2.0.0` - Data validation
- `pandas>=2.2.0` - Data processing
- `pyyaml>=6.0.1` - Configuration parsing

### Step 4: Configure Environment

Create `.env` file (optional):

```bash
# OpenAI-compatible API configuration
OPENAI_API_KEY=your-api-key-here
BASE_URL=https://your-llm-api-endpoint

# OpenShift configuration
KUBECONFIG=/path/to/your/kubeconfig

# Optional: MCP Inspector
ENABLE_MCP_INSPECTOR=0
MCP_INSPECTOR_URL=http://127.0.0.1:8000/sse
```

### Step 5: Verify KUBECONFIG

```bash
export KUBECONFIG=/path/to/kubeconfig
kubectl get nodes
oc get clusterversion  # For OpenShift
```

## Quick Start

### ETCD Analyzer

```bash
cd mcp/etcd

# Start MCP server
./etcd_analyzer_command.sh start

# Or manually
python etcd_analyzer_mcp_server.py

# Start chat client (in another terminal)
python etcd_analyzer_client_chat.py

# Access web UI
open http://localhost:8080/ui
```

### Network Analyzer

```bash
cd mcp/net

# Start MCP server
./network_analyzer_mcp_command.sh start

# Or manually
python network_analyzer_mcp_server.py

# Start chat client
python network_analyzer_client_chat.py
```

### OVN-Kubernetes Analyzer

```bash
cd mcp/ovnk

# Start MCP server
./ovnk_analyzer_mcp_command.sh start

# Or manually
python ovnk_analyzer_mcp_server.py

# Start chat client
python ovnk_analyzer_mcp_client_chat.py
```

## Components

### 1. MCP Servers

Each analyzer exposes an MCP server with specialized tools:

#### ETCD MCP Server (`mcp/etcd/etcd_analyzer_mcp_server.py`)

**Tools:**
- `get_server_health` - Server health check
- `get_etcd_cluster_status` - Cluster health via etcdctl
- `get_ocp_cluster_info` - Cluster information
- `get_etcd_general_info` - General etcd metrics
- `get_etcd_node_usage` - Master node metrics
- `get_etcd_disk_wal_fsync` - WAL fsync performance
- `get_etcd_disk_backend_commit` - Backend commit performance
- `get_node_disk_io` - Disk I/O metrics
- `get_etcd_disk_compact_defrag` - Compaction/defrag metrics
- `get_etcd_network_io` - Network I/O metrics
- `get_etcd_performance_deep_drive` - Comprehensive analysis
- `get_etcd_bottleneck_analysis` - Bottleneck detection
- `generate_etcd_performance_report` - Executive report

#### Network MCP Server (`mcp/net/network_analyzer_mcp_server.py`)

**Tools:**
- `get_ocp_cluster_info` - Cluster information
- `query_network_l1_metrics` - Layer 1 network statistics
- `query_network_io_metrics` - Network I/O performance
- `query_network_socket_tcp_metrics` - TCP socket statistics
- `query_network_socket_udp_metrics` - UDP socket statistics
- `query_network_socket_ip_metrics` - IP socket statistics
- `query_network_socket_mem_metrics` - Socket memory statistics
- `query_network_socket_softnet_metrics` - Softnet statistics
- `query_network_netstat_tcp_metrics` - TCP netstat metrics
- `query_network_netstat_udp_metrics` - UDP netstat metrics

#### OVN-Kubernetes MCP Server (`mcp/ovnk/ovnk_analyzer_mcp_server.py`)

**Tools:**
- `get_ocp_cluster_info` - Cluster information
- `query_ovnk_pod_metrics` - OVN-Kubernetes pod metrics
- `query_multus_pod_metrics` - Multus CNI metrics
- `query_ovnk_container_metrics` - OVN container metrics
- `query_ovnk_sync_metrics` - OVN synchronization metrics
- `query_ovnk_ovs_metrics` - OVS daemon metrics
- `query_ovnk_latency_metrics` - Network latency metrics
- `query_kube_api_metrics` - Kubernetes API metrics

### 2. Tools/Collectors

Specialized collectors organized by category:

- **ETCD**: Cluster status, general info, WAL fsync, backend commit, compact/defrag
- **Network**: I/O, L1, sockets (TCP/UDP/IP/mem/softnet), netstat (TCP/UDP)
- **Node**: CPU, memory, cgroup usage
- **OCP**: Cluster info, API stats, alerts
- **OVNK**: OVN database, kubelet CNI, latency, OVS usage
- **Pods**: Pod and container metrics
- **Disk**: Disk I/O performance

### 3. Analysis Modules

Performance analysis and reporting:

- **Deep Drive Analysis**: Multi-subsystem comprehensive review
- **Bottleneck Detection**: Automated issue identification
- **Performance Reports**: Executive summaries with recommendations
- **Baseline Comparison**: Current vs. target performance
- **Root Cause Analysis**: Script-based + AI-powered RCA

### 4. ELT Pipeline

Extract-Load-Transform for data processing:

- **Generic Orchestrator**: Routes data to metric-specific handlers
- **Metric Handlers**: Specialized ELT modules per metric type
- **HTML Generation**: Formatted tables with highlighting
- **Data Transformation**: JSON to structured DataFrames

### 5. Storage Layer

DuckDB-based persistent storage:

- **Time-Series Data**: Efficient temporal data storage
- **Schema Management**: Automatic table creation and migration
- **Query Interface**: SQL-based data access
- **Historical Analysis**: Long-term performance tracking

### 6. AI Agents

LangGraph-based intelligent agents:

- **Chat Agent**: Conversational interface with tool execution
- **Report Agent**: Automated performance report generation
- **Storage Agent**: Data collection and persistence

## Configuration

### Metrics Configuration

Metrics are defined in YAML files under `config/`:

- `metrics-etcd.yml` - 51 ETCD metrics across 5 categories
- `metrics-net.yml` - 95 network metrics across 9 categories
- `metrics-api.yml` - 15 API server metrics
- `metrics-disk.yml` - 8 disk I/O metrics
- `metrics-node.yml` - 5 node metrics
- `metrics-ovn.yml` - 2 OVN metrics
- `metrics-ovs.yml` - 18 OVS metrics
- `metrics-pods.yml` - 6 pod metrics
- `metrics-cni.yml` - 18 CNI metrics
- `metrics-latency.yml` - 18 latency metrics
- `metrics-alert.yml` - Alert metrics

See `config/README.md` for detailed configuration documentation.

### Environment Variables

```bash
# Required
export KUBECONFIG=/path/to/kubeconfig

# Optional - automatically set to UTC
export TZ=UTC

# LLM Configuration
export OPENAI_API_KEY=your-api-key
export BASE_URL=https://api.openai.com/v1

# MCP Inspector (optional)
export ENABLE_MCP_INSPECTOR=1
export MCP_INSPECTOR_URL=http://127.0.0.1:8000/sse

# Logging
export LOG_LEVEL=INFO
export OVNK_LOG_LEVEL=INFO
```

### Performance Thresholds

Default thresholds (configurable in analysis modules):

```python
thresholds = {
    'wal_fsync_p99_ms': 10.0,              # Critical for write performance
    'backend_commit_p99_ms': 25.0,         # Critical for persistence
    'cpu_usage_warning': 70.0,             # Pod CPU warning
    'cpu_usage_critical': 85.0,            # Pod CPU critical
    'memory_usage_warning': 70.0,           # Pod memory warning
    'memory_usage_critical': 85.0,         # Pod memory critical
    'peer_latency_warning_ms': 50.0,       # Network warning
    'peer_latency_critical_ms': 100.0,     # Network critical
    'network_utilization_warning': 70.0,   # Network utilization warning
    'network_utilization_critical': 85.0,  # Network utilization critical
}
```

## Usage Examples

### Example 1: ETCD Performance Analysis

```bash
# Start ETCD analyzer
cd mcp/etcd
./etcd_analyzer_command.sh start

# In web UI, ask:
"Analyze etcd performance for the last hour"
"Show me WAL fsync performance"
"Generate a performance report for the last 24 hours"
```

### Example 2: Network Analysis

```bash
# Start network analyzer
cd mcp/net
python network_analyzer_mcp_server.py

# Query network metrics
curl -X POST http://localhost:8000/tools/query_network_io_metrics \
  -H "Content-Type: application/json" \
  -d '{"duration": "1h"}'
```

### Example 3: OVN-Kubernetes Analysis

```bash
# Start OVN-Kubernetes analyzer
cd mcp/ovnk
python ovnk_analyzer_mcp_server.py

# Query OVN metrics
curl -X POST http://localhost:8000/tools/query_ovnk_pod_metrics \
  -H "Content-Type: application/json" \
  -d '{"duration": "1h"}'
```

### Example 4: Performance Report Generation

```bash
# Using ETCD report agent
cd mcp/etcd
python etcd_analyzer_mcp_agent_report.py

# Follow prompts:
# 1. Select duration mode or time range mode
# 2. Enter duration (e.g., "1h") or time range
# 3. View streaming analysis and report
```

### Example 5: Data Storage

```bash
# Using ETCD storage agent
cd mcp/etcd
python etcd_analyzer_mcp_agent_stor2db.py

# Data stored in etcd_analyzer_cluster.duckdb
# Query stored data:
python -c "
import duckdb
conn = duckdb.connect('etcd_analyzer_cluster.duckdb')
result = conn.execute('SELECT * FROM wal_fsync_p99_latency LIMIT 10').fetchall()
print(result)
"
```

## API Reference

### MCP Server Endpoints

All MCP servers expose tools via HTTP/SSE:

- **Base URL**: `http://localhost:8000`
- **Health Check**: `GET /health`
- **Tools**: `POST /tools/{tool_name}`

### Chat Client Endpoints

AI chat clients expose REST APIs:

- **Base URL**: `http://localhost:8080`
- **Web UI**: `GET /ui` or `GET /`
- **Streaming Chat**: `POST /chat/stream`
- **Non-streaming Chat**: `POST /chat`
- **Health**: `GET /api/mcp/health`
- **Tools List**: `GET /api/tools`

### Tool Parameters

Common parameters across tools:

- `duration` (str): Time duration (e.g., "5m", "1h", "24h")
- `start_time` (str, optional): Start time in ISO format
- `end_time` (str, optional): End time in ISO format

See individual component READMEs for detailed API documentation:
- `mcp/etcd/README.md` - ETCD analyzer API
- `mcp/ovnk/README.md` - OVN-Kubernetes analyzer API
- `config/README.md` - Configuration API
- `elt/utils/README.md` - ELT pipeline API

## Troubleshooting

### Common Issues

#### 1. MCP Server Won't Start

**Solutions:**
```bash
# Check KUBECONFIG
echo $KUBECONFIG
kubectl get nodes

# Check if port 8000 is in use
lsof -i :8000

# Check logs
tail -f logs/mcp_server_*.log
```

#### 2. Authentication Failures

**Solutions:**
```bash
# Verify KUBECONFIG
export KUBECONFIG=/path/to/kubeconfig
kubectl auth can-i get pods -n openshift-etcd

# Check Prometheus access
kubectl get route -n openshift-monitoring
```

#### 3. Missing Metrics

**Solutions:**
```bash
# Verify Prometheus is accessible
oc get pods -n openshift-monitoring | grep prometheus

# Check metric availability
oc exec -n openshift-monitoring prometheus-k8s-0 -- \
  promtool query instant http://localhost:9090 \
  'etcd_disk_wal_fsync_duration_seconds_bucket'
```

#### 4. LLM API Errors

**Solutions:**
```bash
# Check .env file
cat .env | grep OPENAI_API_KEY

# Test API connection
curl -H "Authorization: Bearer $OPENAI_API_KEY" \
  $BASE_URL/models
```

### Debug Mode

Enable verbose logging:

```bash
export LOG_LEVEL=DEBUG
export OVNK_LOG_LEVEL=DEBUG
python mcp/etcd/etcd_analyzer_mcp_server.py
```

## Contributing

### Development Setup

```bash
# Clone repository
git clone https://github.com/liqcui/ocp-performance-analyzer-mcp.git
cd ocp-performance-analyzer-mcp

# Create development environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install pytest pytest-asyncio black flake8 mypy
```

### Code Style

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

### Adding New Metrics

1. Define metric in appropriate `config/metrics-*.yml` file
2. Add collector in `tools/{category}/` directory
3. Add ELT handler in `elt/{category}/` directory
4. Add storage module in `storage/{category}/` directory
5. Register tool in MCP server
6. Update documentation

### Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html
```

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:

1. Check the troubleshooting section
2. Review component-specific READMEs
3. Check logs in `logs/` directories
4. Open an issue with detailed logs and configuration

## Acknowledgments

- **MCP Protocol**: [Model Context Protocol](https://modelcontextprotocol.io)
- **LangChain**: [LangChain Framework](https://langchain.com)
- **LangGraph**: [LangGraph](https://langchain-ai.github.io/langgraph/)
- **FastMCP**: [FastMCP Library](https://github.com/jlowin/fastmcp)
- **DuckDB**: [DuckDB](https://duckdb.org)
- **OpenShift**: [Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)

## Roadmap

### Planned Features

- [ ] Multi-cluster support
- [ ] Historical trend analysis
- [ ] Anomaly detection with ML
- [ ] Custom alert rules
- [ ] Grafana integration
- [ ] Slack/Teams notifications
- [ ] Performance prediction
- [ ] Automated remediation suggestions
- [ ] Kubernetes native deployment (Helm charts)
- [ ] Real-time streaming metrics

---

**Built with ❤️ for the OpenShift and Kubernetes community**

