#!/usr/bin/env python3
"""
OCP Performance Analyzer - Enhanced CLI Tool
Interactive command-line interface for ETCD performance analysis
"""

import asyncio
import json
import sys
import os
from datetime import datetime
from typing import Optional, Dict, Any
import aiohttp

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt, Confirm
    from rich.markdown import Markdown
    from rich.layout import Layout
    from rich.live import Live
    from rich import box
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    print("Warning: 'rich' library not found. Install with: pip install rich")
    print("Falling back to basic output...")

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


class CLIAnalyzer:
    """Enhanced CLI for OCP Performance Analysis"""

    def __init__(self, mcp_server_url: str = "http://localhost:8001"):
        self.mcp_server_url = mcp_server_url
        self.console = Console() if HAS_RICH else None
        self.session = None
        self.tools_available = []

    def print(self, *args, **kwargs):
        """Print with rich if available, else standard print"""
        if self.console:
            self.console.print(*args, **kwargs)
        else:
            print(*args)

    async def connect(self) -> bool:
        """Connect to MCP server"""
        try:
            if self.console:
                with self.console.status("[bold green]Connecting to MCP server...", spinner="dots"):
                    await asyncio.sleep(0.5)  # Visual feedback

            url = f"{self.mcp_server_url}/mcp"
            async with streamablehttp_client(url) as (read_stream, write_stream, get_session_id):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    tools_result = await session.list_tools()
                    self.tools_available = [tool.name for tool in tools_result.tools]
                    self.session = session

                    if self.console:
                        self.console.print(f"[green]✓[/green] Connected to MCP server")
                        self.console.print(f"[cyan]{len(self.tools_available)} tools available[/cyan]")
                    else:
                        print(f"✓ Connected - {len(self.tools_available)} tools available")

                    return True
        except Exception as e:
            if self.console:
                self.console.print(f"[red]✗ Connection failed: {e}[/red]")
            else:
                print(f"✗ Connection failed: {e}")
            return False

    async def call_tool(self, tool_name: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Call an MCP tool"""
        try:
            url = f"{self.mcp_server_url}/mcp"
            async with streamablehttp_client(url) as (read_stream, write_stream, get_session_id):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()

                    # Wrap params in request object
                    call_params = {"request": params} if params else {}
                    result = await session.call_tool(tool_name, call_params)

                    # Extract content from result
                    if hasattr(result, 'content') and result.content:
                        content_item = result.content[0]
                        if hasattr(content_item, 'text'):
                            return json.loads(content_item.text)

                    return {"error": "No content in response"}
        except Exception as e:
            return {"error": str(e)}

    def display_header(self):
        """Display application header"""
        if self.console:
            self.console.print()
            panel = Panel(
                "[bold cyan]OCP Performance Analyzer[/bold cyan]\n"
                "[dim]AI-Powered ETCD Performance Analysis Tool[/dim]",
                box=box.DOUBLE,
                border_style="cyan"
            )
            self.console.print(panel)
        else:
            print("\n" + "="*60)
            print("   OCP Performance Analyzer")
            print("   AI-Powered ETCD Performance Analysis Tool")
            print("="*60)

    def display_menu(self):
        """Display main menu"""
        if self.console:
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
            menu.add_row("9", "📊 Generate Full Report")
            menu.add_row("", "")
            menu.add_row("s", "📡 Server Status")
            menu.add_row("h", "❓ Help")
            menu.add_row("q", "🚪 Quit")

            self.console.print("\n[bold]Quick Analysis Menu:[/bold]")
            self.console.print(menu)
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
            print("  9. 📊 Generate Full Report")
            print()
            print("  s. 📡 Server Status")
            print("  h. ❓ Help")
            print("  q. 🚪 Quit")
            print("-"*60)

    async def cluster_overview(self):
        """Display cluster overview"""
        self.print("\n[bold cyan]🏛️  Cluster Overview[/bold cyan]\n")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
            transient=True
        ) if self.console else self._null_context():
            if self.console:
                task = progress.add_task("Fetching cluster info...", total=None)

            result = await self.call_tool("get_ocp_cluster_info")

            if "error" in result:
                self.print(f"[red]Error: {result['error']}[/red]")
                return

            # Display results
            if self.console:
                table = Table(title="OpenShift Cluster Information", box=box.ROUNDED)
                table.add_column("Metric", style="cyan bold", width=25)
                table.add_column("Value", style="green")

                data = result.get("data", {})
                for key, value in data.items():
                    table.add_row(key, str(value))

                self.console.print(table)
            else:
                print("\nOpenShift Cluster Information:")
                print("-" * 60)
                data = result.get("data", {})
                for key, value in data.items():
                    print(f"  {key:25} {value}")

    async def etcd_general_info(self):
        """Display ETCD general information"""
        self.print("\n[bold cyan]🖥️  ETCD General Information[/bold cyan]\n")

        with self._progress_context("Fetching ETCD metrics..."):
            result = await self.call_tool("get_etcd_general_info", {"duration": "2m"})

            if "error" in result:
                self.print(f"[red]Error: {result['error']}[/red]")
                return

            # Display HTML table if available
            html_content = result.get("html_content", "")
            if html_content:
                # Parse and display table data
                self._display_html_as_table(html_content, "ETCD Performance Metrics")

            # Display AI analysis if available
            ai_analysis = result.get("ai_analysis", "")
            if ai_analysis:
                self.print("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
                if self.console:
                    md = Markdown(ai_analysis)
                    self.console.print(Panel(md, border_style="yellow"))
                else:
                    print(ai_analysis)

    async def wal_fsync_performance(self):
        """Analyze WAL Fsync performance"""
        self.print("\n[bold cyan]🔄 WAL Fsync Performance[/bold cyan]\n")

        with self._progress_context("Analyzing WAL fsync..."):
            result = await self.call_tool("get_etcd_disk_wal_fsync", {"duration": "2m"})

            if "error" in result:
                self.print(f"[red]Error: {result['error']}[/red]")
                return

            html_content = result.get("html_content", "")
            if html_content:
                self._display_html_as_table(html_content, "WAL Fsync Performance")

            ai_analysis = result.get("ai_analysis", "")
            if ai_analysis:
                self.print("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
                if self.console:
                    md = Markdown(ai_analysis)
                    self.console.print(Panel(md, border_style="yellow"))
                else:
                    print(ai_analysis)

    async def backend_commit_performance(self):
        """Analyze Backend Commit performance"""
        self.print("\n[bold cyan]🔗 Backend Commit Performance[/bold cyan]\n")

        with self._progress_context("Analyzing backend commit..."):
            result = await self.call_tool("get_etcd_disk_backend_commit", {"duration": "2m"})

            if "error" in result:
                self.print(f"[red]Error: {result['error']}[/red]")
                return

            html_content = result.get("html_content", "")
            if html_content:
                self._display_html_as_table(html_content, "Backend Commit Performance")

            ai_analysis = result.get("ai_analysis", "")
            if ai_analysis:
                self.print("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
                if self.console:
                    md = Markdown(ai_analysis)
                    self.console.print(Panel(md, border_style="yellow"))
                else:
                    print(ai_analysis)

    async def disk_io_analysis(self):
        """Analyze disk I/O performance"""
        self.print("\n[bold cyan]💾 Disk I/O Analysis[/bold cyan]\n")

        with self._progress_context("Analyzing disk I/O..."):
            result = await self.call_tool("get_node_disk_io", {"duration": "2m"})

            if "error" in result:
                self.print(f"[red]Error: {result['error']}[/red]")
                return

            html_content = result.get("html_content", "")
            if html_content:
                self._display_html_as_table(html_content, "Disk I/O Performance")

            ai_analysis = result.get("ai_analysis", "")
            if ai_analysis:
                self.print("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
                if self.console:
                    md = Markdown(ai_analysis)
                    self.console.print(Panel(md, border_style="yellow"))
                else:
                    print(ai_analysis)

    async def network_io_analysis(self):
        """Analyze network I/O performance"""
        self.print("\n[bold cyan]🌐 Network I/O Analysis[/bold cyan]\n")

        with self._progress_context("Analyzing network I/O..."):
            result = await self.call_tool("get_etcd_network_io", {"duration": "2m"})

            if "error" in result:
                self.print(f"[red]Error: {result['error']}[/red]")
                return

            html_content = result.get("html_content", "")
            if html_content:
                self._display_html_as_table(html_content, "Network I/O Performance")

            ai_analysis = result.get("ai_analysis", "")
            if ai_analysis:
                self.print("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
                if self.console:
                    md = Markdown(ai_analysis)
                    self.console.print(Panel(md, border_style="yellow"))
                else:
                    print(ai_analysis)

    async def deep_performance_analysis(self):
        """Perform deep performance analysis"""
        self.print("\n[bold cyan]🔍 Deep Performance Analysis[/bold cyan]\n")

        with self._progress_context("Performing deep analysis..."):
            result = await self.call_tool("get_etcd_performance_deep_drive", {"duration": "2m"})

            if "error" in result:
                self.print(f"[red]Error: {result['error']}[/red]")
                return

            html_content = result.get("html_content", "")
            if html_content:
                self._display_html_as_table(html_content, "Deep Performance Analysis")

            ai_analysis = result.get("ai_analysis", "")
            if ai_analysis:
                self.print("\n[bold yellow]🤖 AI Analysis:[/bold yellow]")
                if self.console:
                    md = Markdown(ai_analysis)
                    self.console.print(Panel(md, border_style="yellow"))
                else:
                    print(ai_analysis)

    async def generate_full_report(self):
        """Generate full performance report"""
        self.print("\n[bold cyan]📊 Generating Full Performance Report[/bold cyan]\n")

        with self._progress_context("Generating comprehensive report..."):
            result = await self.call_tool("generate_etcd_performance_report", {"duration": "2m"})

            if "error" in result:
                self.print(f"[red]Error: {result['error']}[/red]")
                return

            report_path = result.get("report_path", "")
            if report_path:
                self.print(f"\n[green]✓ Report generated successfully![/green]")
                self.print(f"[cyan]Location: {report_path}[/cyan]")

                if self.console and Confirm.ask("\nOpen report in browser?"):
                    import webbrowser
                    webbrowser.open(f"file://{os.path.abspath(report_path)}")

            html_content = result.get("html_content", "")
            if html_content:
                self._display_html_as_table(html_content, "Report Summary")

    def _progress_context(self, description: str):
        """Context manager for progress indicator"""
        if self.console:
            return Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=self.console,
                transient=True
            )
        else:
            return self._null_context()

    class _null_context:
        """Null context manager for when rich is not available"""
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass
        def add_task(self, *args, **kwargs):
            pass

    def _display_html_as_table(self, html_content: str, title: str):
        """Parse HTML and display as rich table"""
        # For now, just display raw HTML or extract text
        # TODO: Implement HTML parsing to extract table data
        if self.console:
            self.console.print(Panel(html_content[:500], title=title, border_style="cyan"))
        else:
            print(f"\n{title}:")
            print("-" * 60)
            print(html_content[:500])

    async def server_status(self):
        """Display server status"""
        self.print("\n[bold cyan]📡 Server Status[/bold cyan]\n")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.mcp_server_url}/health") as resp:
                    if resp.status == 200:
                        data = await resp.json()

                        if self.console:
                            table = Table(title="MCP Server Health", box=box.ROUNDED)
                            table.add_column("Metric", style="cyan bold")
                            table.add_column("Value", style="green")

                            table.add_row("Status", data.get("status", "unknown"))
                            table.add_row("Timestamp", data.get("timestamp", "N/A"))
                            table.add_row("Server URL", self.mcp_server_url)
                            table.add_row("Available Tools", str(len(self.tools_available)))

                            self.console.print(table)
                        else:
                            print(f"Status: {data.get('status', 'unknown')}")
                            print(f"Server: {self.mcp_server_url}")
                            print(f"Tools: {len(self.tools_available)}")
                    else:
                        self.print(f"[red]Server returned status {resp.status}[/red]")
        except Exception as e:
            self.print(f"[red]Error checking server: {e}[/red]")

    def display_help(self):
        """Display help information"""
        if self.console:
            help_text = """
# OCP Performance Analyzer CLI Help

## Quick Analysis Options

**1. Cluster Overview** - Display basic OpenShift cluster information
**2. ETCD General Info** - Show core ETCD performance metrics
**3. Node Resource Usage** - Analyze master node resource utilization
**4. WAL Fsync Performance** - Check ETCD write-ahead log performance
**5. Backend Commit** - Analyze database commit performance
**6. Disk I/O Analysis** - Deep dive into disk performance
**7. Network I/O Analysis** - Analyze network performance
**8. Deep Performance Analysis** - Comprehensive multi-dimensional analysis
**9. Generate Full Report** - Create complete HTML performance report

## Commands

- **s** - Check MCP server connection status
- **h** - Display this help message
- **q** - Quit the application

## Tips

- All analysis results include AI-powered insights
- Reports are saved to the `exports/` directory
- Use duration parameter to adjust analysis time window (default: 2m)
"""
            md = Markdown(help_text)
            self.console.print(Panel(md, title="Help", border_style="cyan"))
        else:
            print("\n" + "="*60)
            print("OCP Performance Analyzer CLI Help")
            print("="*60)
            print("\n1-9: Quick analysis options")
            print("s: Server status")
            print("h: Help")
            print("q: Quit")

    async def run(self):
        """Main CLI loop"""
        self.display_header()

        # Connect to server
        connected = await self.connect()
        if not connected:
            self.print("\n[red]Failed to connect to MCP server. Exiting.[/red]")
            return

        # Main loop
        while True:
            self.display_menu()

            if self.console:
                choice = Prompt.ask("\n[bold]Select an option[/bold]", default="h")
            else:
                choice = input("\nSelect an option (h for help): ").strip().lower()

            try:
                if choice == "1":
                    await self.cluster_overview()
                elif choice == "2":
                    await self.etcd_general_info()
                elif choice == "3":
                    self.print("\n[yellow]Node resource usage analysis - Coming soon![/yellow]")
                elif choice == "4":
                    await self.wal_fsync_performance()
                elif choice == "5":
                    await self.backend_commit_performance()
                elif choice == "6":
                    await self.disk_io_analysis()
                elif choice == "7":
                    await self.network_io_analysis()
                elif choice == "8":
                    await self.deep_performance_analysis()
                elif choice == "9":
                    await self.generate_full_report()
                elif choice == "s":
                    await self.server_status()
                elif choice == "h":
                    self.display_help()
                elif choice == "q":
                    self.print("\n[cyan]Thank you for using OCP Performance Analyzer![/cyan]")
                    break
                else:
                    self.print(f"\n[red]Invalid option: {choice}[/red]")

                # Pause before showing menu again
                if choice != "q" and choice != "h":
                    input("\nPress Enter to continue...")

            except KeyboardInterrupt:
                self.print("\n\n[yellow]Interrupted by user[/yellow]")
                break
            except Exception as e:
                self.print(f"\n[red]Error: {e}[/red]")
                if self.console:
                    import traceback
                    self.console.print_exception()


def main():
    """Entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="OCP Performance Analyzer CLI")
    parser.add_argument(
        "--server",
        default="http://localhost:8001",
        help="MCP server URL (default: http://localhost:8001)"
    )

    args = parser.parse_args()

    analyzer = CLIAnalyzer(mcp_server_url=args.server)

    try:
        asyncio.run(analyzer.run())
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
