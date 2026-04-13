# 📸 CLI Example Output

## Starting the CLI

```
$ ./cli.py

╔══════════════════════════════════════════════════════════════╗
║           OCP Performance Analyzer                           ║
║    AI-Powered ETCD Performance Analysis Tool                 ║
╚══════════════════════════════════════════════════════════════╝

⠋ Connecting to MCP server...
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

Select an option [h]:
```

## Example 1: Cluster Overview

```
Select an option [h]: 1

🏛️  Cluster Overview

⠋ Fetching cluster info...

                   OpenShift Cluster Information
┌─────────────────────────┬────────────────────────────────┐
│ Metric                  │ Value                          │
├─────────────────────────┼────────────────────────────────┤
│ Cluster Name            │ production-ocp-cluster         │
│ OpenShift Version       │ 4.14.3                         │
│ Kubernetes Version      │ v1.27.6                        │
│ Total Nodes             │ 15 (3 Master + 12 Worker)      │
│ ETCD Members            │ 3                              │
│ ETCD Health Status      │ Healthy ✓                      │
│ Cluster Uptime          │ 45 days                        │
└─────────────────────────┴────────────────────────────────┘

🤖 AI Analysis:
┌──────────────────────────────────────────────────────────┐
│ Cluster Status Summary                                   │
│                                                          │
│ Your OpenShift cluster is running in a healthy state:   │
│                                                          │
│ • Version: OpenShift 4.14.3 (latest stable)             │
│ • Scale: 15-node configuration suitable for medium      │
│   production environments                                │
│ • ETCD: 3-member cluster meets HA requirements           │
│ • Health: All components operational, no alerts         │
│                                                          │
│ Recommendation: Configuration is optimal. Continue       │
│ monitoring resource usage trends.                        │
└──────────────────────────────────────────────────────────┘

Press Enter to continue...
```

## Example 2: WAL Fsync Performance

```
Select an option [h]: 4

🔄 WAL Fsync Performance

⠋ Analyzing WAL fsync...

                    WAL Fsync Performance
┌──────────────────┬──────────┬──────────┬──────────┬──────────┬────────┐
│ Metric           │ etcd-0   │ etcd-1   │ etcd-2   │ Target   │ Status │
├──────────────────┼──────────┼──────────┼──────────┼──────────┼────────┤
│ P99 Latency      │ 8.2 ms   │ 7.9 ms   │ 8.5 ms   │ <10ms    │   ✓    │
│ P90 Latency      │ 5.1 ms   │ 4.8 ms   │ 5.3 ms   │ <7ms     │   ✓    │
│ P50 Latency      │ 2.3 ms   │ 2.1 ms   │ 2.4 ms   │ <3ms     │   ✓    │
│ Average Latency  │ 1.8 ms   │ 1.7 ms   │ 1.9 ms   │ <2ms     │   ✓    │
└──────────────────┴──────────┴──────────┴──────────┴──────────┴────────┘

🤖 AI Analysis:
┌──────────────────────────────────────────────────────────┐
│ WAL Fsync Performance Evaluation                         │
│                                                          │
│ 🎉 Performance: EXCELLENT                                │
│                                                          │
│ Key Findings:                                            │
│ • P99 latency: 8.2ms (target: <10ms) ✓ Excellent        │
│ • P90 latency: 5.1ms - Consistently fast                 │
│ • P50 latency: 2.3ms - Sub-millisecond typical case     │
│                                                          │
│ Performance Implications:                                │
│ WAL fsync is a critical component of ETCD's write path.  │
│ Current latency indicates:                               │
│ - Fast disk write performance                            │
│ - SSD is responding quickly                              │
│ - No I/O contention issues                               │
│                                                          │
│ Recommendation:                                          │
│ ✓ Performance is excellent, no optimization needed.      │
│ ✓ Continue monitoring to maintain current levels.        │
│ ✓ Disk subsystem is properly configured.                │
└──────────────────────────────────────────────────────────┘

Press Enter to continue...
```

## Example 3: Backend Commit Performance

```
Select an option [h]: 5

🔗 Backend Commit Performance

⠋ Analyzing backend commit...

                 Backend Commit Performance
┌──────────────────┬──────────┬──────────┬──────────┬──────────┬────────┐
│ Metric           │ etcd-0   │ etcd-1   │ etcd-2   │ Target   │ Status │
├──────────────────┼──────────┼──────────┼──────────┼──────────┼────────┤
│ P99 Latency      │ 32.5 ms  │ 31.8 ms  │ 33.2 ms  │ <25ms    │   ⚠    │
│ P90 Latency      │ 18.3 ms  │ 17.9 ms  │ 18.7 ms  │ <15ms    │   ⚠    │
│ P50 Latency      │ 8.1 ms   │ 7.8 ms   │ 8.3 ms   │ <10ms    │   ✓    │
└──────────────────┴──────────┴──────────┴──────────┴──────────┴────────┘

🤖 AI Analysis:
┌──────────────────────────────────────────────────────────┐
│ Backend Commit Performance Analysis                      │
│                                                          │
│ ⚠️  Status: NEEDS ATTENTION                              │
│                                                          │
│ Problem Identification:                                  │
│ • P99 latency: 32.5ms (target: <25ms) - 30% over limit  │
│ • P90 latency: 18.3ms (target: <15ms) - 22% over limit  │
│ • P50 latency: 8.1ms - Within acceptable range          │
│                                                          │
│ Root Cause Analysis:                                     │
│ 1. Disk I/O load is likely elevated                     │
│ 2. Backend database commit operations are frequent      │
│ 3. Potential disk performance insufficiency             │
│ 4. Possible I/O contention with other processes         │
│                                                          │
│ Optimization Recommendations:                            │
│                                                          │
│ Short-term (1-2 weeks):                                  │
│ 1. Check disk I/O Wait metrics                          │
│ 2. Verify no competing I/O processes                    │
│ 3. Review disk health and performance stats             │
│                                                          │
│ Mid-term (1-2 months):                                   │
│ 1. Consider upgrading to NVMe SSD                       │
│ 2. Adjust I/O scheduler to 'deadline' or 'noop'         │
│ 3. Separate WAL and data directories if possible        │
│                                                          │
│ Long-term (2-3 months):                                  │
│ 1. Implement RAID configuration for reliability         │
│ 2. Use enterprise-grade SSDs                            │
│ 3. Consider dedicated high-performance storage          │
│                                                          │
│ Impact Assessment:                                       │
│ Current performance won't severely impact operations,   │
│ but optimization will improve overall cluster           │
│ responsiveness and reduce latency spikes.               │
│                                                          │
│ Priority: MEDIUM - Schedule optimization during next    │
│ maintenance window                                       │
└──────────────────────────────────────────────────────────┘

Press Enter to continue...
```

## Example 4: Deep Performance Analysis

```
Select an option [h]: 8

🔍 Deep Performance Analysis

⠋ Performing deep analysis...

              Multi-Dimensional Performance Scan
┌──────────────────────┬──────────────────┬──────────────┬────────┐
│ Subsystem            │ Key Metric       │ Current      │ Status │
├──────────────────────┼──────────────────┼──────────────┼────────┤
│ WAL Fsync            │ P99 Latency      │ 8.2 ms       │   ✓    │
│ Backend Commit       │ P99 Latency      │ 32.5 ms      │   ⚠    │
│ Disk I/O             │ I/O Wait         │ 15%          │   ✗    │
│ Network I/O          │ Peer Latency     │ 3.2 ms       │   ✓    │
│ CPU Usage            │ Average Usage    │ 43%          │   ✓    │
│ Memory Usage         │ Average Usage    │ 58%          │   ✓    │
└──────────────────────┴──────────────────┴──────────────┴────────┘

🤖 AI Analysis:
┌──────────────────────────────────────────────────────────┐
│ Deep Performance Analysis Results                        │
│                                                          │
│ 🔴 BOTTLENECK IDENTIFIED: Disk I/O                       │
│                                                          │
│ Evidence Chain:                                          │
│                                                          │
│ 1. WAL Fsync: 8.2ms ✓                                    │
│    → Sequential writes are fast                          │
│                                                          │
│ 2. Backend Commit: 32.5ms ⚠                              │
│    → Random writes are slow                              │
│                                                          │
│ 3. Disk I/O Wait: 15% ✗                                  │
│    → CPU spending too much time waiting for disk         │
│                                                          │
│ 4. Network I/O: 3.2ms ✓                                  │
│    → Network is not the problem                          │
│                                                          │
│ 5. CPU/Memory: Normal                                    │
│    → Not a compute resource issue                        │
│                                                          │
│                        ↓                                 │
│         CONCLUSION: Disk I/O Bottleneck                  │
│                                                          │
│ Root Cause:                                              │
│ Disk I/O Wait at 15% (threshold: <10%) indicates the    │
│ storage subsystem cannot keep up with ETCD's write       │
│ demands. This is causing Backend Commit delays.          │
│                                                          │
│ Optimization Roadmap:                                    │
│                                                          │
│ Immediate Actions (0-1 week):                            │
│ 1. Run: iostat -x 1                                      │
│    Check disk utilization and await times                │
│                                                          │
│ 2. Verify disk type:                                     │
│    lsblk -d -o name,rota,disc-gran                       │
│                                                          │
│ 3. Check for competing I/O:                              │
│    iotop -aoP                                            │
│                                                          │
│ Short-term (1-2 weeks):                                  │
│ 1. Adjust I/O scheduler:                                 │
│    echo deadline > /sys/block/sda/queue/scheduler        │
│                                                          │
│ 2. Optimize mount options:                               │
│    mount -o remount,noatime /etcd                        │
│                                                          │
│ 3. Increase disk cache if available                      │
│                                                          │
│ Mid-term (1-2 months):                                   │
│ 1. Upgrade to NVMe SSD                                   │
│    Expected improvement:                                 │
│    • I/O Wait: 15% → <5%                                 │
│    • Backend Commit: 32ms → <20ms                        │
│                                                          │
│ 2. Implement RAID 10 configuration                       │
│                                                          │
│ Long-term (2-3 months):                                  │
│ 1. Deploy dedicated storage array                        │
│ 2. Implement monitoring and alerting                     │
│ 3. Establish performance baselines                       │
│                                                          │
│ Expected ROI:                                            │
│ • 40% reduction in write latency                         │
│ • 66% improvement in I/O Wait                            │
│ • 25% faster API operations                              │
│ • Better cluster responsiveness                          │
│                                                          │
│ Cost-Benefit:                                            │
│ NVMe SSD upgrade: $500-800/disk                          │
│ Performance gain: 3-4x improvement                       │
│ Payback period: 2-3 months in reduced downtime          │
└──────────────────────────────────────────────────────────┘

Press Enter to continue...
```

## Example 5: Server Status

```
Select an option [h]: s

📡 Server Status

                    MCP Server Health
┌──────────────────────┬──────────────────────────────────┐
│ Metric               │ Value                            │
├──────────────────────┼──────────────────────────────────┤
│ Status               │ healthy                          │
│ Timestamp            │ 2026-04-13T10:30:45Z             │
│ Server URL           │ http://localhost:8001            │
│ Available Tools      │ 15                               │
└──────────────────────┴──────────────────────────────────┘

Press Enter to continue...
```

## Example 6: Generate Full Report

```
Select an option [h]: 9

📊 Generating Full Performance Report

⠋ Generating comprehensive report...

✓ Report generated successfully!
Location: exports/etcd_performance_report_20260413_103052.html

                     Report Summary
┌──────────────────────────────────────────────────────────┐
│ ETCD Performance Analysis Report                         │
│                                                          │
│ Generated: 2026-04-13 10:30:52 UTC                       │
│ Analysis Window: 2m                                      │
│ Cluster: production-ocp-cluster                         │
│                                                          │
│ Executive Summary:                                       │
│ • Cluster Health: Healthy ✓                             │
│ • Issues Found: 1 warning (Backend Commit)               │
│ • Identified Bottleneck: Disk I/O                        │
│ • Priority: Medium                                       │
│                                                          │
│ Key Metrics:                                             │
│ • WAL Fsync P99: 8.2ms ✓                                 │
│ • Backend Commit P99: 32.5ms ⚠                           │
│ • CPU Usage: 43% ✓                                       │
│ • Memory Usage: 58% ✓                                    │
│ • Disk I/O Wait: 15% ✗                                   │
│ • Network Latency: 3.2ms ✓                               │
│                                                          │
│ Recommendations:                                         │
│ 1. Check disk I/O statistics (iostat)                    │
│ 2. Adjust I/O scheduler to deadline                      │
│ 3. Plan NVMe upgrade within 1-2 months                   │
│ 4. Set up Backend Commit latency alerts                  │
└──────────────────────────────────────────────────────────┘

Open report in browser? (y/n):
```

## Example 7: Help

```
Select an option [h]: h

┌──────────────────────────────────────────────────────────┐
│ Help                                                     │
├──────────────────────────────────────────────────────────┤
│ OCP Performance Analyzer CLI Help                       │
│                                                          │
│ Quick Analysis Options                                   │
│                                                          │
│ 1. Cluster Overview - Display basic OpenShift cluster   │
│    information                                           │
│ 2. ETCD General Info - Show core ETCD performance       │
│    metrics                                               │
│ 3. Node Resource Usage - Analyze master node resource   │
│    utilization                                           │
│ 4. WAL Fsync Performance - Check ETCD write-ahead log   │
│    performance                                           │
│ 5. Backend Commit - Analyze database commit performance │
│ 6. Disk I/O Analysis - Deep dive into disk performance  │
│ 7. Network I/O Analysis - Analyze network performance   │
│ 8. Deep Performance Analysis - Comprehensive multi-      │
│    dimensional analysis                                  │
│ 9. Generate Full Report - Create complete HTML          │
│    performance report                                    │
│                                                          │
│ Commands                                                 │
│                                                          │
│ • s - Check MCP server connection status                │
│ • h - Display this help message                         │
│ • q - Quit the application                              │
│                                                          │
│ Tips                                                     │
│                                                          │
│ • All analysis results include AI-powered insights      │
│ • Reports are saved to the exports/ directory           │
│ • Use duration parameter to adjust analysis time window │
│   (default: 2m)                                          │
└──────────────────────────────────────────────────────────┘

Press Enter to continue...
```

## Example 8: Graceful Exit

```
Select an option [h]: q

Thank you for using OCP Performance Analyzer!

$
```

## Fallback Mode (Without Rich Library)

```
$ ./cli.py

Warning: 'rich' library not found. Install with: pip install rich
Falling back to basic output...

============================================================
   OCP Performance Analyzer
   AI-Powered ETCD Performance Analysis Tool
============================================================

✓ Connected - 15 tools available

------------------------------------------------------------
Quick Analysis Menu:
------------------------------------------------------------
  1. 🏛️  Cluster Overview
  2. 🖥️  ETCD General Info
  3. 📈 Node Resource Usage
  4. 🔄 WAL Fsync Performance
  5. 🔗 Backend Commit Performance
  6. 💾 Disk I/O Analysis
  7. 🌐 Network I/O Analysis
  8. 🔍 Deep Performance Analysis
  9. 📊 Generate Full Report

  s. 📡 Server Status
  h. ❓ Help
  q. 🚪 Quit
------------------------------------------------------------

Select an option (h for help): 4

WAL Fsync Performance

OpenShift Cluster Information:
------------------------------------------------------------
  Metric                    Value
  P99 Latency              8.2 ms ✓
  P90 Latency              5.1 ms
  P50 Latency              2.3 ms
  Average Latency          1.8 ms

🤖 AI Analysis:
WAL fsync performance is excellent. P99 latency of 8.2ms
is well below the 10ms threshold...

Press Enter to continue...
```

---

**Note:** These examples show the rich terminal UI output. Actual output will vary based on:
- Your cluster's real metrics
- Whether the 'rich' library is installed
- Terminal width and capabilities
- MCP server availability
