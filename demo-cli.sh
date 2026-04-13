#!/bin/bash

# OCP Performance Analyzer - CLI Demo Script
# This script demonstrates the CLI functionality

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  OCP Performance Analyzer - Enhanced CLI Demo               ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if rich is installed
echo "🔍 Checking dependencies..."
if python3 -c "import rich" 2>/dev/null; then
    echo "✓ Rich library installed"
else
    echo "⚠️  Rich library not found. Installing..."
    pip install rich
fi

# Check if MCP server is running
echo ""
echo "🔍 Checking MCP server status..."
if curl -s http://localhost:8001/health > /dev/null 2>&1; then
    echo "✓ MCP server is running on http://localhost:8001"
else
    echo "⚠️  MCP server is not running!"
    echo ""
    echo "To start the MCP server, run in another terminal:"
    echo "  python3 mcp/etcd/etcd_analyzer_mcp_server.py"
    echo ""
    read -p "Press Enter to continue anyway (demo mode)..."
fi

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  Starting Enhanced CLI                                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Available commands:"
echo "  1-9  : Quick analysis scenarios"
echo "  s    : Server status"
echo "  h    : Help"
echo "  q    : Quit"
echo ""
echo "Demo tips:"
echo "  • Try option '4' for WAL Fsync Performance"
echo "  • Try option '8' for Deep Performance Analysis"
echo "  • Try option '9' to Generate Full Report"
echo ""
read -p "Press Enter to launch the CLI..."

# Launch the CLI
./cli.py

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  Demo Complete                                               ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo "  • Check generated reports in exports/ directory"
echo "  • Review CLI_GUIDE.md for detailed documentation"
echo "  • Try the web demo: https://liqcui.github.io/ocp-performance-analyzer-mcp/"
echo ""
