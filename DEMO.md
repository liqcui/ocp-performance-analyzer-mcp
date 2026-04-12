# 🎬 在线演示指南

## 📍 GitHub Pages 在线访问

演示页面已部署到GitHub Pages，可以直接在浏览器中访问：

### 🔗 访问地址

**主演示页面**: https://liqcui.github.io/ocp-performance-analyzer-mcp/

**完整文档演示**: https://liqcui.github.io/ocp-performance-analyzer-mcp/demo.html

**演示文稿**: https://liqcui.github.io/ocp-performance-analyzer-mcp/demo-script.html

---

## 🚀 如何启用 GitHub Pages

如果页面还未激活，请按以下步骤操作：

### 步骤1: 进入仓库设置
访问: https://github.com/liqcui/ocp-performance-analyzer-mcp/settings/pages

### 步骤2: 配置GitHub Pages
- **Source**: Deploy from a branch
- **Branch**: main
- **Folder**: /docs
- 点击 **Save**

### 步骤3: 等待部署
通常需要1-2分钟，刷新页面会看到访问链接

### 步骤4: 访问演示
访问: https://liqcui.github.io/ocp-performance-analyzer-mcp/

---

## 📱 演示页面功能

### 主演示页面 (index.html)

**特点**:
- ✅ 真实的AI聊天界面
- ✅ 三个视图：AI聊天、架构、演示
- ✅ 9个性能分析场景可点击体验

**演示场景**:
1. 🏛️ 集群概览
2. 🖥️ ETCD常规信息
3. 📈 节点资源使用
4. 🔄 WAL Fsync性能
5. 🔗 Backend Commit
6. 💾 磁盘I/O分析
7. 🌐 网络I/O分析
8. 🔍 深度性能分析
9. 📊 完整性能报告

**操作方法**:
点击左侧快速操作按钮 → 查看模拟的分析结果 → 查看AI解读

---

### 文档演示页面 (demo.html)

**包含内容**:
- 📊 项目概览（统计数据、核心价值）
- 🏗️ 系统架构（6层架构图）
- ⚡ 核心功能（实时监控、AI分析、瓶颈检测）
- 🧩 组件说明（ETCD、网络、OVN-K三个分析器）
- 🎬 性能分析演示（3个实际案例）
- 📖 使用示例（代码、命令、配置）

**适用场景**:
- 项目介绍
- 技术分享
- 团队培训
- 文档参考

---

## 📖 演示文稿 (demo-script.md)

**内容**:
- 完整的15-20分钟演示大纲
- 详细的演示话术
- 18个常见问题详细解答
- 演示技巧和注意事项

**使用方法**:
作为演讲提纲和Q&A速查手册

---

## 🔗 快速链接

| 资源 | 链接 | 说明 |
|------|------|------|
| 交互式演示 | [index.html](https://liqcui.github.io/ocp-performance-analyzer-mcp/) | 主演示页面 |
| 文档演示 | [demo.html](https://liqcui.github.io/ocp-performance-analyzer-mcp/demo.html) | 完整文档 |
| 演示文稿 | [demo-script.md](https://github.com/liqcui/ocp-performance-analyzer-mcp/blob/main/docs/demo-script.md) | 演讲指南 |
| GitHub仓库 | [Repository](https://github.com/liqcui/ocp-performance-analyzer-mcp) | 源代码 |
| 项目README | [README.md](https://github.com/liqcui/ocp-performance-analyzer-mcp/blob/main/README.md) | 项目文档 |

---

## 📤 分享演示

### 方法1: 直接分享链接
```
https://liqcui.github.io/ocp-performance-analyzer-mcp/
```

### 方法2: 二维码分享
可以使用在线工具生成二维码：
- https://qr-code-generator.com/
- 输入演示链接
- 下载二维码图片

### 方法3: 嵌入到文档
```markdown
[查看在线演示](https://liqcui.github.io/ocp-performance-analyzer-mcp/)
```

### 方法4: 在README中添加徽章
```markdown
[![Demo](https://img.shields.io/badge/Demo-在线演示-blue)](https://liqcui.github.io/ocp-performance-analyzer-mcp/)
```

---

## 💡 使用建议

### 用于演讲/展示
1. 打开主演示页面
2. 全屏显示 (F11)
3. 按顺序点击左侧场景
4. 配合演示文稿讲解

### 用于培训
1. 先展示架构视图（点击"🏗️ 架构"）
2. 再展示实际演示（点击"🎬 演示"）
3. 最后互动体验（点击"💬 AI聊天"）

### 用于技术分享
1. 使用文档演示页面
2. 滚动浏览各个章节
3. 重点讲解架构和案例

---

## 🛠️ 本地测试

如果想在本地测试演示页面：

```bash
# 方法1: 直接打开HTML文件
open docs/index.html

# 方法2: 使用Python启动本地服务器
cd docs
python3 -m http.server 8000
# 访问 http://localhost:8000

# 方法3: 使用Live Server (VSCode插件)
# 右键index.html → Open with Live Server
```

---

## 🔄 更新演示页面

如果需要更新演示内容：

```bash
# 1. 修改 docs/ 目录下的HTML文件
vim docs/index.html

# 2. 提交更改
git add docs/
git commit -m "Update demo pages"
git push origin main

# 3. 等待GitHub Pages自动部署（约1-2分钟）

# 4. 清除浏览器缓存后访问新版本
```

---

## 📊 访问统计

可以添加Google Analytics追踪访问：

```html
<!-- 在 docs/index.html 和 docs/demo.html 的 <head> 中添加 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
```

---

## 🎯 演示最佳实践

### ✅ 推荐做法
- 提前测试所有链接和功能
- 准备好网络备份方案
- 使用大屏幕/投影仪展示
- 配合演示文稿讲解

### ❌ 避免
- 不要在演示中修改代码
- 不要依赖实时网络（可提前打开页面）
- 不要跳过架构讲解（很重要）

---

## 📞 支持

遇到问题？
- GitHub Issues: https://github.com/liqcui/ocp-performance-analyzer-mcp/issues
- Email: liqcui@redhat.com

---

**祝演示成功！** 🎉
