#!/usr/bin/env python3
"""
OCP Performance Analyzer - Offline Demo Mode
Demonstrates CLI functionality with simulated data (no MCP server required)
"""

import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.prompt import Prompt
    from rich.markdown import Markdown
    from rich import box
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    print("Installing rich library for better UI...")
    os.system("pip install rich")
    try:
        from rich.console import Console
        from rich.table import Table
        from rich.panel import Panel
        from rich.prompt import Prompt
        from rich.markdown import Markdown
        from rich import box
        HAS_RICH = True
    except:
        HAS_RICH = False

console = Console() if HAS_RICH else None


def print_msg(*args, **kwargs):
    """Print with rich if available"""
    if console:
        console.print(*args, **kwargs)
    else:
        print(*args)


def display_header():
    """Display application header"""
    if console:
        console.print()
        panel = Panel(
            "[bold cyan]OCP Performance Analyzer - DEMO MODE[/bold cyan]\n"
            "[dim]AI-Powered ETCD Performance Analysis (Simulated Data)[/dim]",
            box=box.DOUBLE,
            border_style="cyan"
        )
        console.print(panel)
    else:
        print("\n" + "="*60)
        print("   OCP Performance Analyzer - DEMO MODE")
        print("   (Simulated Data - No Server Required)")
        print("="*60)


def display_menu():
    """Display main menu"""
    if console:
        menu = Table(show_header=False, box=box.SIMPLE, padding=(0, 2))
        menu.add_column("Option", style="cyan bold", width=4)
        menu.add_column("Description", style="white")

        menu.add_row("1", "🏛️  Cluster Overview")
        menu.add_row("2", "🖥️  ETCD General Info")
        menu.add_row("3", "📈 Node Resource Usage")
        menu.add_row("4", "🔄 WAL Fsync Performance")
        menu.add_row("5", "🔗 Backend Commit Performance")
        menu.add_row("6", "💾 Disk I/O Analysis")
        menu.add_row("7", "🌐 Network I/O Analysis")
        menu.add_row("8", "🔍 Deep Performance Analysis")
        menu.add_row("", "")
        menu.add_row("h", "❓ Help")
        menu.add_row("q", "🚪 Quit")

        console.print("\n[bold]Quick Analysis Menu:[/bold]")
        console.print(menu)
    else:
        print("\n" + "-"*60)
        print("Quick Analysis Menu:")
        print("-"*60)
        print("  1. 🏛️  Cluster Overview")
        print("  2. 🖥️  ETCD General Info")
        print("  3. 📈 Node Resource Usage")
        print("  4. 🔄 WAL Fsync Performance")
        print("  5. 🔗 Backend Commit Performance")
        print("  6. 💾 Disk I/O Analysis")
        print("  7. 🌐 Network I/O Analysis")
        print("  8. 🔍 Deep Performance Analysis")
        print()
        print("  h. ❓ Help")
        print("  q. 🚪 Quit")
        print("-"*60)


def demo_cluster_overview():
    """Demo cluster overview"""
    print_msg("\n[bold cyan]🏛️  Cluster Overview[/bold cyan]\n")

    import time
    if console:
        with console.status("[bold green]Fetching cluster info...", spinner="dots"):
            time.sleep(1.5)

    if console:
        table = Table(title="OpenShift Cluster Information", box=box.ROUNDED)
        table.add_column("Metric", style="cyan bold", width=25)
        table.add_column("Value", style="green")

        table.add_row("Cluster Name", "production-ocp-cluster")
        table.add_row("OpenShift Version", "4.14.3")
        table.add_row("Kubernetes Version", "v1.27.6")
        table.add_row("Total Nodes", "15 (3 Master + 12 Worker)")
        table.add_row("ETCD Members", "3")
        table.add_row("ETCD Health", "✓ Healthy")
        table.add_row("Cluster Uptime", "45 days")

        console.print(table)

        ai_analysis = """**Cluster Status Summary**

Your OpenShift cluster is running in a healthy state:

• **Version**: OpenShift 4.14.3 (latest stable)
• **Scale**: 15-node configuration suitable for medium production
• **ETCD**: 3-member cluster meets HA requirements
• **Health**: All components operational, no alerts

**Recommendation**: Configuration is optimal. Continue monitoring resource trends."""

        print_msg("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
        md = Markdown(ai_analysis)
        console.print(Panel(md, border_style="yellow"))
    else:
        print("\nOpenShift Cluster Information:")
        print("-" * 60)
        print(f"  {'Cluster Name':25} production-ocp-cluster")
        print(f"  {'OpenShift Version':25} 4.14.3")
        print(f"  {'Kubernetes Version':25} v1.27.6")
        print(f"  {'Total Nodes':25} 15 (3 Master + 12 Worker)")
        print(f"  {'ETCD Members':25} 3")
        print(f"  {'ETCD Health':25} ✓ Healthy")


def demo_wal_fsync():
    """Demo WAL Fsync performance"""
    print_msg("\n[bold cyan]🔄 WAL Fsync Performance[/bold cyan]\n")

    import time
    if console:
        with console.status("[bold green]Analyzing WAL fsync...", spinner="dots"):
            time.sleep(1.5)

    if console:
        table = Table(title="WAL Fsync Performance", box=box.ROUNDED)
        table.add_column("Metric", style="cyan bold")
        table.add_column("etcd-0", style="white")
        table.add_column("etcd-1", style="white")
        table.add_column("etcd-2", style="white")
        table.add_column("Target", style="yellow")
        table.add_column("Status", style="green")

        table.add_row("P99 Latency", "8.2 ms", "7.9 ms", "8.5 ms", "<10ms", "✓")
        table.add_row("P90 Latency", "5.1 ms", "4.8 ms", "5.3 ms", "<7ms", "✓")
        table.add_row("P50 Latency", "2.3 ms", "2.1 ms", "2.4 ms", "<3ms", "✓")
        table.add_row("Average", "1.8 ms", "1.7 ms", "1.9 ms", "<2ms", "✓")

        console.print(table)

        ai_analysis = """**WAL Fsync Performance Evaluation**

🎉 **Performance: EXCELLENT**

**Key Findings:**
• P99 latency: 8.2ms (target: <10ms) ✓ Excellent
• P90 latency: 5.1ms - Consistently fast
• P50 latency: 2.3ms - Sub-millisecond typical case

**Performance Implications:**
WAL fsync is critical to ETCD's write path. Current latency indicates:
- Fast disk write performance
- SSD responding quickly
- No I/O contention issues

**Recommendation:**
✓ Performance excellent, no optimization needed
✓ Continue monitoring to maintain current levels
✓ Disk subsystem properly configured"""

        print_msg("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
        md = Markdown(ai_analysis)
        console.print(Panel(md, border_style="yellow"))
    else:
        print("\nWAL Fsync Performance:")
        print("-" * 60)
        print("  P99 Latency: 8.2ms (target: <10ms) ✓")
        print("  P90 Latency: 5.1ms")
        print("  P50 Latency: 2.3ms")


def demo_backend_commit():
    """Demo backend commit performance"""
    print_msg("\n[bold cyan]🔗 Backend Commit Performance[/bold cyan]\n")

    import time
    if console:
        with console.status("[bold yellow]Analyzing backend commit...", spinner="dots"):
            time.sleep(1.5)

    if console:
        table = Table(title="Backend Commit Performance", box=box.ROUNDED)
        table.add_column("Metric", style="cyan bold")
        table.add_column("etcd-0", style="white")
        table.add_column("etcd-1", style="white")
        table.add_column("etcd-2", style="white")
        table.add_column("Target", style="yellow")
        table.add_column("Status", style="yellow")

        table.add_row("P99 Latency", "32.5 ms", "31.8 ms", "33.2 ms", "<25ms", "⚠")
        table.add_row("P90 Latency", "18.3 ms", "17.9 ms", "18.7 ms", "<15ms", "⚠")
        table.add_row("P50 Latency", "8.1 ms", "7.8 ms", "8.3 ms", "<10ms", "✓")

        console.print(table)

        ai_analysis = """**Backend Commit Performance Analysis**

⚠️ **Status: NEEDS ATTENTION**

**Problem Identification:**
• P99 latency: 32.5ms (target: <25ms) - 30% over limit
• P90 latency: 18.3ms (target: <15ms) - 22% over limit
• P50 latency: 8.1ms - Within acceptable range

**Root Cause Analysis:**
1. Disk I/O load likely elevated
2. Backend database commits are frequent
3. Potential disk performance insufficiency
4. Possible I/O contention

**Optimization Recommendations:**

**Short-term (1-2 weeks):**
1. Check disk I/O Wait metrics
2. Verify no competing I/O processes
3. Review disk health and performance

**Mid-term (1-2 months):**
1. Consider upgrading to NVMe SSD
2. Adjust I/O scheduler to 'deadline' or 'noop'
3. Separate WAL and data directories

**Priority:** MEDIUM - Schedule during next maintenance window"""

        print_msg("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
        md = Markdown(ai_analysis)
        console.print(Panel(md, border_style="yellow"))
    else:
        print("\nBackend Commit Performance:")
        print("-" * 60)
        print("  P99 Latency: 32.5ms (target: <25ms) ⚠")
        print("  P90 Latency: 18.3ms")
        print("  Status: Needs attention")


def demo_deep_analysis():
    """Demo deep performance analysis"""
    print_msg("\n[bold cyan]🔍 Deep Performance Analysis[/bold cyan]\n")

    import time
    if console:
        with console.status("[bold green]Performing deep analysis...", spinner="dots"):
            time.sleep(2)

    if console:
        table = Table(title="Multi-Dimensional Performance Scan", box=box.ROUNDED)
        table.add_column("Subsystem", style="cyan bold")
        table.add_column("Key Metric", style="white")
        table.add_column("Current", style="white")
        table.add_column("Status", style="white")

        table.add_row("WAL Fsync", "P99 Latency", "8.2 ms", "[green]✓[/green]")
        table.add_row("Backend Commit", "P99 Latency", "32.5 ms", "[yellow]⚠[/yellow]")
        table.add_row("Disk I/O", "I/O Wait", "15%", "[red]✗[/red]")
        table.add_row("Network I/O", "Peer Latency", "3.2 ms", "[green]✓[/green]")
        table.add_row("CPU Usage", "Average", "43%", "[green]✓[/green]")
        table.add_row("Memory", "Average", "58%", "[green]✓[/green]")

        console.print(table)

        ai_analysis = """**Deep Performance Analysis Results**

🔴 **BOTTLENECK IDENTIFIED: Disk I/O**

**Evidence Chain:**

1. WAL Fsync: 8.2ms ✓ → Sequential writes are fast
2. Backend Commit: 32.5ms ⚠ → Random writes are slow
3. Disk I/O Wait: 15% ✗ → CPU waiting for disk
4. Network I/O: 3.2ms ✓ → Network is NOT the problem
5. CPU/Memory: Normal → Not a compute issue

                    ↓
        **CONCLUSION: Disk I/O Bottleneck**

**Root Cause:**
Disk I/O Wait at 15% (threshold: <10%) indicates storage cannot keep up with ETCD's write demands.

**Optimization Roadmap:**

**Immediate (0-1 week):**
1. Run: `iostat -x 1` - Check disk utilization
2. Verify disk type: `lsblk -d -o name,rota`
3. Check competing I/O: `iotop -aoP`

**Short-term (1-2 weeks):**
1. Adjust scheduler: `echo deadline > /sys/block/sda/queue/scheduler`
2. Optimize mounts: `mount -o remount,noatime /etcd`

**Mid-term (1-2 months):**
1. Upgrade to NVMe SSD
   - Expected: I/O Wait 15% → <5%
   - Backend Commit: 32ms → <20ms

**Expected ROI:**
• 40% reduction in write latency
• 66% improvement in I/O Wait
• 25% faster API operations
• Better cluster responsiveness"""

        print_msg("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
        md = Markdown(ai_analysis)
        console.print(Panel(md, border_style="yellow"))
    else:
        print("\nMulti-Dimensional Performance Scan:")
        print("-" * 60)
        print("  WAL Fsync: 8.2ms ✓")
        print("  Backend Commit: 32.5ms ⚠")
        print("  Disk I/O Wait: 15% ✗ BOTTLENECK")
        print("  Network: 3.2ms ✓")


def display_help():
    """Display help"""
    if console:
        help_text = """# OCP Performance Analyzer CLI Help

## Demo Mode

This is a **demonstration mode** with simulated data. No MCP server required!

## Quick Analysis Options

**1. Cluster Overview** - OpenShift cluster information
**2. ETCD General Info** - Core ETCD metrics
**3. Node Resource Usage** - Master node utilization
**4. WAL Fsync Performance** - Write-ahead log performance ⭐ Try this!
**5. Backend Commit** - Database commit analysis ⭐ Try this!
**6. Disk I/O Analysis** - Deep disk performance
**7. Network I/O Analysis** - Network performance
**8. Deep Performance Analysis** - Comprehensive scan ⭐ Try this!

## Commands

- **h** - Display this help
- **q** - Quit

## Real Usage

To use with real data:
1. Start MCP server: `python3 mcp/etcd/etcd_analyzer_mcp_server.py`
2. Run: `./cli.py`"""

        md = Markdown(help_text)
        console.print(Panel(md, title="Help", border_style="cyan"))
    else:
        print("\n" + "="*60)
        print("Help")
        print("="*60)
        print("\nThis is DEMO MODE with simulated data.")
        print("\nOptions 1-8: Quick analysis scenarios")
        print("Try option 4, 5, or 8 for best examples!")


def main():
    """Main demo loop"""
    display_header()

    print_msg("\n[bold green]✓[/bold green] Demo mode active (no server required)")
    print_msg("[dim]Using simulated data for demonstration[/dim]")

    while True:
        display_menu()

        if console:
            choice = Prompt.ask("\n[bold]Select an option[/bold]", default="h")
        else:
            choice = input("\nSelect an option (h for help): ").strip().lower()

        try:
            if choice == "1":
                demo_cluster_overview()
            elif choice == "2":
                print_msg("\n[yellow]Demo: ETCD General Info - Try option 4 or 8 instead![/yellow]")
            elif choice == "3":
                print_msg("\n[yellow]Demo: Node Resource Usage - Try option 4 or 8 instead![/yellow]")
            elif choice == "4":
                demo_wal_fsync()
            elif choice == "5":
                demo_backend_commit()
            elif choice == "6":
                print_msg("\n[yellow]Demo: Disk I/O - Try option 8 for comprehensive analysis![/yellow]")
            elif choice == "7":
                print_msg("\n[yellow]Demo: Network I/O - Try option 8 for comprehensive analysis![/yellow]")
            elif choice == "8":
                demo_deep_analysis()
            elif choice == "h":
                display_help()
            elif choice == "q":
                print_msg("\n[cyan]Thank you for trying the OCP Performance Analyzer demo![/cyan]")
                print_msg("[dim]To use with real data, start the MCP server and run ./cli.py[/dim]\n")
                break
            else:
                print_msg(f"\n[red]Invalid option: {choice}[/red]")

            if choice != "q" and choice != "h":
                input("\nPress Enter to continue...")

        except KeyboardInterrupt:
            print_msg("\n\n[yellow]Demo interrupted[/yellow]")
            break
        except Exception as e:
            print_msg(f"\n[red]Error: {e}[/red]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting demo...")
    except Exception as e:
        print(f"Fatal error: {e}")
