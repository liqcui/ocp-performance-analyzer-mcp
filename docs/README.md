# OCP Performance Analyzer MCP - 在线演示

欢迎体验 **OCP Performance Analyzer MCP** 的在线演示！

## 🎬 演示页面

### 1. [交互式演示 (推荐)](./index.html)
**完整功能演示** - 模拟真实的AI对话分析界面

**特点**:
- 🤖 真实的AI聊天界面
- 📊 9个性能分析场景
- 🏗️ 完整的系统架构图
- 🎯 实际的数据展示

**使用方法**: 点击左侧快速操作按钮，体验不同的性能分析场景

---

### 2. [完整文档演示](./demo.html)
**项目概览与文档** - 全面的项目介绍和技术说明

**包含内容**:
- 📖 项目概览和统计
- 🏗️ 系统架构设计
- ⚡ 核心功能特性
- 🧩 组件详细说明
- 🎬 性能分析演示
- 📖 使用示例

---

## 🚀 快速开始

想在自己的环境中运行？

```bash
# 克隆仓库
git clone https://github.com/liqcui/ocp-performance-analyzer-mcp.git
cd ocp-performance-analyzer-mcp

# 安装依赖
python3 -m venv venv
source venv/bin/activate
pip install -e .

# 配置环境
export KUBECONFIG=/path/to/kubeconfig
export OPENAI_API_KEY=your-api-key

# 启动服务
cd mcp/etcd
./etcd_analyzer_command.sh start

# 访问 Web UI
open http://localhost:8080/ui
```

---

## 📚 相关资源

- **GitHub仓库**: [liqcui/ocp-performance-analyzer-mcp](https://github.com/liqcui/ocp-performance-analyzer-mcp)
- **详细文档**: [README.md](https://github.com/liqcui/ocp-performance-analyzer-mcp/blob/main/README.md)
- **演示文稿**: [Demo Script](https://github.com/liqcui/ocp-performance-analyzer-mcp/blob/main/docs/demo-script.md)

---

## 🎯 项目特点

- 🤖 **AI驱动** - 基于LangGraph和OpenAI的智能分析
- 🔍 **自动瓶颈检测** - 智能识别性能问题
- 📊 **一键生成报告** - 专业的性能分析报告
- 💾 **历史趋势分析** - DuckDB时序数据分析
- 🌐 **MCP协议** - 标准化的工具集成

---

**Built with ❤️ for the OpenShift and Kubernetes community**

© 2026 OCP Performance Analyzer MCP | MIT License
