# 🖥️ Enhanced CLI Guide

## Overview

The enhanced CLI (`cli.py`) provides an interactive, menu-driven interface for analyzing OpenShift ETCD performance, inspired by the web demo interface.

## Features

### ✨ Interactive Menu
- 9 quick analysis scenarios accessible via simple number keys
- Rich terminal UI with colors, tables, and progress indicators
- Real-time server status checking
- Built-in help system

### 📊 Analysis Scenarios

1. **Cluster Overview** 🏛️
   - OpenShift cluster basic information
   - ETCD cluster status
   - Node configuration

2. **ETCD General Info** 🖥️
   - CPU and memory usage
   - Database size metrics
   - Proposal failure rates

3. **Node Resource Usage** 📈
   - Master node resource utilization
   - Detailed resource allocation
   - Network statistics

4. **WAL Fsync Performance** 🔄
   - Write-ahead log performance
   - P50/P90/P99 latency metrics
   - Performance threshold comparison

5. **Backend Commit Performance** 🔗
   - Database commit latency
   - Bottleneck identification
   - Optimization recommendations

6. **Disk I/O Analysis** 💾
   - IOPS and throughput
   - Read/write latency
   - Queue depth analysis

7. **Network I/O Analysis** 🌐
   - Peer communication latency
   - Bandwidth utilization
   - Network reliability metrics

8. **Deep Performance Analysis** 🔍
   - Multi-dimensional performance scan
   - Cross-system correlation
   - Root cause identification

9. **Generate Full Report** 📊
   - Comprehensive HTML report
   - Executive summary
   - Actionable recommendations

## Installation

### Prerequisites

```bash
# Python 3.8 or higher required
python3 --version
```

### Install Dependencies

```bash
# Install rich library for enhanced terminal UI
pip install rich

# Or install all project dependencies
pip install -r requirements.txt
```

### Verify Installation

```bash
# Check if rich is installed
python3 -c "import rich; print(rich.__version__)"
```

## Usage

### Basic Usage

```bash
# Start the CLI (assumes MCP server running on localhost:8001)
./cli.py

# Or with explicit server URL
./cli.py --server http://localhost:8001
```

### Quick Start

1. **Start the MCP Server** (in another terminal):
   ```bash
   python3 mcp/etcd/etcd_analyzer_mcp_server.py
   ```

2. **Run the CLI**:
   ```bash
   ./cli.py
   ```

3. **Navigate the Menu**:
   - Press `1-9` for quick analysis
   - Press `s` for server status
   - Press `h` for help
   - Press `q` to quit

### Command-Line Options

```bash
./cli.py --help

Options:
  --server SERVER  MCP server URL (default: http://localhost:8001)
```

## UI Features

### With Rich Library (Recommended)

When the `rich` library is installed, you get:

- ✅ **Colored output** - Syntax-highlighted tables and panels
- ✅ **Progress indicators** - Spinners for long-running operations
- ✅ **Formatted tables** - Clean, bordered data displays
- ✅ **Markdown rendering** - Beautiful AI analysis formatting
- ✅ **Interactive prompts** - Enhanced user input experience

### Without Rich Library (Fallback)

If `rich` is not installed, the CLI falls back to:

- Basic text output
- Plain tables
- Standard Python input/output
- All functionality still works, just less visually appealing

## Example Session

```
┌─────────────────────────────────────────────────────────┐
│           OCP Performance Analyzer                      │
│    AI-Powered ETCD Performance Analysis Tool            │
└─────────────────────────────────────────────────────────┘

✓ Connected to MCP server
15 tools available

Quick Analysis Menu:
┌───────┬──────────────────────────────────────┐
│ 1     │ 🏛️  Cluster Overview                 │
│ 2     │ 🖥️  ETCD General Info                │
│ 3     │ 📈 Node Resource Usage               │
│ 4     │ 🔄 WAL Fsync Performance             │
│ 5     │ 🔗 Backend Commit Performance        │
│ 6     │ 💾 Disk I/O Analysis                 │
│ 7     │ 🌐 Network I/O Analysis              │
│ 8     │ 🔍 Deep Performance Analysis         │
│ 9     │ 📊 Generate Full Report              │
│       │                                      │
│ s     │ 📡 Server Status                     │
│ h     │ ❓ Help                              │
│ q     │ 🚪 Quit                              │
└───────┴──────────────────────────────────────┘

Select an option [h]: 4

🔄 WAL Fsync Performance

⠋ Analyzing WAL fsync...

┌─────────────────────────────────────────────────┐
│         WAL Fsync Performance                   │
├──────────────────┬──────────────────────────────┤
│ Metric           │ Value                        │
├──────────────────┼──────────────────────────────┤
│ P99 Latency      │ 8.2 ms ✓                     │
│ P90 Latency      │ 5.1 ms                       │
│ P50 Latency      │ 2.3 ms                       │
│ Status           │ Excellent                    │
└──────────────────┴──────────────────────────────┘

🤖 AI Analysis:
┌─────────────────────────────────────────────────┐
│ WAL fsync performance is excellent. P99         │
│ latency of 8.2ms is well below the 10ms         │
│ threshold, indicating fast disk write           │
│ performance and no I/O contention.              │
│                                                 │
│ Recommendation: No action needed. Continue      │
│ monitoring to maintain current performance.     │
└─────────────────────────────────────────────────┘

Press Enter to continue...
```

## Tips and Best Practices

### 1. Run Analysis During Different Times

```bash
# Run during peak hours
./cli.py  # Select option 8 for deep analysis

# Run during off-hours for comparison
./cli.py  # Select option 8 again
```

### 2. Generate Reports Regularly

```bash
# Weekly report generation
./cli.py  # Select option 9
# Reports are saved to exports/ directory
```

### 3. Monitor Specific Metrics

```bash
# Check WAL fsync regularly if using spinning disks
./cli.py  # Select option 4

# Monitor network during cluster scaling
./cli.py  # Select option 7
```

### 4. Use Server Status Check

```bash
# Verify MCP server is healthy before analysis
./cli.py  # Select option 's'
```

## Troubleshooting

### Connection Issues

```bash
# Check if MCP server is running
curl http://localhost:8001/health

# Start MCP server if not running
python3 mcp/etcd/etcd_analyzer_mcp_server.py
```

### Missing Dependencies

```bash
# Install rich for better UI
pip install rich

# Verify installation
python3 -c "import rich; print('✓ Rich installed')"
```

### Permission Denied

```bash
# Make CLI executable
chmod +x cli.py

# Or run with python explicitly
python3 cli.py
```

### Import Errors

```bash
# Ensure you're in the project root directory
cd /path/to/ocp-performance-analyzer-mcp
./cli.py

# Or set PYTHONPATH
export PYTHONPATH=/path/to/ocp-performance-analyzer-mcp
./cli.py
```

## Advanced Usage

### Custom Duration

While the CLI uses default 2-minute windows, you can modify the code to accept custom durations:

```python
# In cli.py, modify tool calls:
result = await self.call_tool("get_etcd_disk_wal_fsync", {"duration": "5m"})
```

### Automated Reporting

```bash
# Create a cron job for daily reports
0 2 * * * cd /path/to/project && echo "9\nq\n" | ./cli.py --server http://localhost:8001
```

### Integration with Scripts

```python
# Use as a module in your own scripts
from cli import CLIAnalyzer

async def custom_analysis():
    analyzer = CLIAnalyzer()
    await analyzer.connect()
    await analyzer.deep_performance_analysis()
```

## Comparison: CLI vs Web Demo

| Feature | Web Demo | CLI |
|---------|----------|-----|
| Interactive UI | ✅ Rich HTML/CSS | ✅ Rich Terminal |
| 9 Analysis Scenarios | ✅ | ✅ |
| AI Analysis | ✅ | ✅ |
| Progress Indicators | ✅ | ✅ |
| Export Reports | ✅ | ✅ |
| Keyboard Navigation | ❌ | ✅ |
| Remote Access | ✅ | ❌ (SSH required) |
| No Browser Required | ❌ | ✅ |
| Works Offline | ✅ | ✅ (if MCP server local) |

## Future Enhancements

Planned features for future versions:

- [ ] Custom duration selection via prompt
- [ ] Save analysis history
- [ ] Compare reports side-by-side
- [ ] Export to JSON/CSV formats
- [ ] Scheduling and automation
- [ ] Alert configuration
- [ ] Multi-cluster support
- [ ] Real-time monitoring mode

## Contributing

To enhance the CLI:

1. Fork the repository
2. Add your feature to `cli.py`
3. Test thoroughly
4. Submit a pull request

## Support

- **GitHub Issues**: https://github.com/liqcui/ocp-performance-analyzer-mcp/issues
- **Documentation**: See `docs/` directory
- **Web Demo**: https://liqcui.github.io/ocp-performance-analyzer-mcp/

## License

Same as main project - see LICENSE file.

---

**Happy Analyzing!** 🚀
