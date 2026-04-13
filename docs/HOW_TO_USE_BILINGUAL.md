# 🌐 How to Use Bilingual Feature | 如何使用双语功能

## Quick Start | 快速开始

**English Users:**
1. Visit: https://liqcui.github.io/ocp-performance-analyzer-mcp/
2. Click the **"EN"** button in the top-right corner
3. Enjoy the demo in English!

**中文用户:**
1. 访问: https://liqcui.github.io/ocp-performance-analyzer-mcp/
2. 页面默认显示中文
3. 开始使用演示!

---

## Visual Guide | 视觉指南

### index.html (Interactive Demo | 交互式演示)

#### Step 1: Default View (Chinese) | 步骤1: 默认视图（中文）
```
┌──────────────────────────────────────────────────────┐
│  性能分析演示界面                          [EN] ←    │  Click here!
│                                                      │
│  💬 AI聊天  🏗️ 架构  🎬 演示                        │
└──────────────────────────────────────────────────────┘
│                                                      │
│  Sidebar (Left):                                     │
│  🚀 OCP ETCD Analyzer                                │
│  AI驱动的性能分析平台                                │
│                                                      │
│  📊 快速操作                                         │
│  🏛️ 集群概览                                         │
│  🖥️ ETCD常规信息                                     │
│  📈 节点资源使用                                     │
│  ...                                                 │
└──────────────────────────────────────────────────────┘
```

#### Step 2: After Clicking "EN" | 步骤2: 点击"EN"后
```
┌──────────────────────────────────────────────────────┐
│  Performance Analysis Demo                  [中文] ← │  Click to switch back
│                                                      │
│  💬 AI Chat  🏗️ Architecture  🎬 Demo               │
└──────────────────────────────────────────────────────┘
│                                                      │
│  Sidebar (Left):                                     │
│  🚀 OCP ETCD Analyzer                                │
│  AI-Powered Performance Analysis Platform            │
│                                                      │
│  📊 Quick Actions                                    │
│  🏛️ Cluster Overview                                │
│  🖥️ ETCD General Info                               │
│  📈 Node Resource Usage                              │
│  ...                                                 │
└──────────────────────────────────────────────────────┘
```

---

### demo.html (Documentation Demo | 文档演示)

#### Step 1: Find the Button | 步骤1: 找到按钮
```
                                          ┌──────┐
                                          │  EN  │ ← Floating button
                                          └──────┘    (top-right corner)

┌────────────────────────────────────────────────────────┐
│                                                        │
│  🚀 OCP Performance Analyzer MCP                       │
│  AI驱动的OpenShift/Kubernetes集群性能分析平台          │
│                                                        │
│  [概览] [架构设计] [核心功能] [组件说明] [演示] [使用] │
│                                                        │
└────────────────────────────────────────────────────────┘
```

#### Step 2: After Toggle | 步骤2: 切换后
```
                                          ┌──────┐
                                          │ 中文  │ ← Click to go back
                                          └──────┘

┌────────────────────────────────────────────────────────┐
│                                                        │
│  🚀 OCP Performance Analyzer MCP                       │
│  AI-Powered Performance Analysis Platform for...      │
│                                                        │
│  [Overview] [Architecture] [Features] [Components]... │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## What Changes | 什么会改变

### index.html

**When you toggle to English:**

| Element | Chinese (中文) | English (EN) |
|---------|---------------|--------------|
| Page Title | 性能分析演示界面 | Performance Analysis Demo |
| Tab 1 | 💬 AI聊天 | 💬 AI Chat |
| Tab 2 | 🏗️ 架构 | 🏗️ Architecture |
| Tab 3 | 🎬 演示 | 🎬 Demo |
| Sidebar Title | 🚀 OCP ETCD Analyzer | (same) |
| Sidebar Subtitle | AI驱动的性能分析平台 | AI-Powered Performance Analysis Platform |
| Quick Actions | 📊 快速操作 | 📊 Quick Actions |
| Action 1 | 🏛️ 集群概览 | 🏛️ Cluster Overview |
| Action 2 | 🖥️ ETCD常规信息 | 🖥️ ETCD General Info |
| Action 3 | 📈 节点资源使用 | 📈 Node Resource Usage |
| Action 4 | 🔄 WAL Fsync性能 | 🔄 WAL Fsync Performance |
| Action 5 | 🔗 Backend Commit | (same) |
| Action 6 | 💾 磁盘I/O分析 | 💾 Disk I/O Analysis |
| Action 7 | 🌐 网络I/O分析 | 🌐 Network I/O Analysis |
| Action 8 | 🔍 深度性能分析 | 🔍 Deep Performance Analysis |
| Action 9 | 📊 完整性能报告 | 📊 Full Performance Report |
| Status 1 | MCP服务器已连接 (演示模式) | MCP Server Connected (Demo Mode) |
| Status 2 | 集群健康 (15个工具可用) | Cluster Healthy (15 Tools Available) |
| Welcome | 👋 欢迎使用... | 👋 Welcome to... |

**Total: 22+ elements change instantly**

### demo.html

**When you toggle to English:**

| Element | Chinese (中文) | English (EN) |
|---------|---------------|--------------|
| Header Title | 🚀 OCP Performance Analyzer MCP | (same) |
| Header Subtitle | AI驱动的OpenShift/Kubernetes集群性能分析平台 | AI-Powered Performance Analysis Platform for OpenShift/Kubernetes Clusters |
| Nav: Overview | 概览 | Overview |
| Nav: Architecture | 架构设计 | Architecture |
| Nav: Features | 核心功能 | Core Features |
| Nav: Components | 组件说明 | Components |
| Nav: Demo | 性能分析演示 | Performance Demo |
| Nav: Usage | 使用示例 | Usage Examples |
| Section 1 Title | 📊 项目概览 | 📊 Project Overview |
| Section 2 Title | 🏗️ 系统架构 | 🏗️ System Architecture |
| Section 3 Title | ⚡ 核心功能特性 | ⚡ Core Features |
| Section 4 Title | 🧩 组件详细说明 | 🧩 Components |
| Section 5 Title | 🎬 性能分析演示 | 🎬 Performance Analysis Demo |
| Section 6 Title | 📖 使用示例 | 📖 Usage Examples |

**Total: 14+ elements change instantly**

---

## Features | 功能特性

### ✨ Instant Switching | 即时切换
- No page reload needed | 无需刷新页面
- Changes apply in <10ms | 切换耗时<10毫秒
- Smooth transition | 平滑过渡

### 💾 Persistent Preference | 偏好持久化
- Your choice is saved | 您的选择会被保存
- Remembered on next visit | 下次访问时记住
- Works across both demo pages | 在两个演示页面都有效

### 🎯 Smart Default | 智能默认
- First visit: Chinese | 首次访问：中文
- After toggle: Your last choice | 切换后：您的上次选择
- Easy to change anytime | 随时可以更改

---

## Technical Details | 技术细节

### How It Works | 工作原理

**Step 1: Page Load | 页面加载**
```javascript
// Check for saved preference
let currentLang = localStorage.getItem('preferredLanguage') || 'zh';

// Apply language on load
document.addEventListener('DOMContentLoaded', function() {
    applyLanguage();
});
```

**Step 2: User Clicks Button | 用户点击按钮**
```javascript
function toggleLanguage() {
    // Toggle between zh and en
    currentLang = currentLang === 'zh' ? 'en' : 'zh';

    // Save preference
    localStorage.setItem('preferredLanguage', currentLang);

    // Apply changes
    applyLanguage();
}
```

**Step 3: Update UI | 更新界面**
```javascript
function applyLanguage() {
    // Update button text
    document.getElementById('lang-text').textContent =
        currentLang === 'zh' ? 'EN' : '中文';

    // Update all translated elements
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        element.textContent = translations[currentLang][key];
    });
}
```

### Browser Storage | 浏览器存储

**What Gets Saved:**
```
Key: 'preferredLanguage'
Value: 'en' or 'zh'
Location: localStorage (persistent)
```

**Check Your Preference:**
```javascript
// Open browser console (F12)
localStorage.getItem('preferredLanguage')
// Returns: 'en' or 'zh' or null
```

**Clear Your Preference:**
```javascript
// Open browser console (F12)
localStorage.removeItem('preferredLanguage')
// Next visit will default to Chinese
```

---

## Troubleshooting | 故障排除

### Problem: Button Not Visible | 问题：按钮不可见

**index.html:**
- Look in the top-right area of the header
- It's next to the tab buttons (AI Chat, Architecture, Demo)
- Should show "EN" if page is in Chinese

**demo.html:**
- Look at the very top-right corner of the page
- It's a floating button, always visible
- Should show "EN" if page is in Chinese

### Problem: Language Doesn't Change | 问题：语言不改变

**Possible Causes:**
1. JavaScript disabled in browser
2. localStorage blocked by privacy settings
3. Old cached version loaded

**Solutions:**
```
1. Enable JavaScript:
   - Chrome: Settings → Privacy → Site Settings → JavaScript
   - Firefox: about:config → javascript.enabled → true

2. Allow localStorage:
   - Chrome: Settings → Privacy → Cookies → Allow all cookies
   - Firefox: Options → Privacy → Custom → Cookies → Accept

3. Clear cache:
   - Chrome: Ctrl+Shift+Delete → Clear browsing data
   - Firefox: Ctrl+Shift+Delete → Clear Recent History
   - Or: Hard refresh with Ctrl+F5
```

### Problem: Preference Not Saved | 问题：偏好未保存

**Check:**
```javascript
// Open browser console (F12)
console.log(typeof(Storage)); // Should return "object" not "undefined"
console.log(localStorage.getItem('preferredLanguage')); // Should return 'en' or 'zh'
```

**If undefined:**
- Browser is blocking localStorage
- Try different browser
- Check privacy/incognito mode settings

---

## Tips & Tricks | 提示与技巧

### 1. Keyboard Shortcut (Future)
Currently not implemented, but you can suggest:
```
Alt+L → Toggle language
```

### 2. Share Link in Specific Language
Currently, the preference is stored locally. To share:
```
English speakers: Ask them to click "EN" on first visit
Chinese speakers: Default is Chinese, no action needed
```

### 3. Test Both Languages
```
1. Visit page (loads in Chinese)
2. Click "EN" (switches to English)
3. Refresh page (stays in English)
4. Click "中文" (switches back to Chinese)
5. Refresh page (stays in Chinese)
```

### 4. Mobile Experience
- Button is responsive
- Works on phones and tablets
- Touch-friendly size
- Same functionality as desktop

---

## FAQs | 常见问题

### Q: Will my preference sync across devices?
**A:** No, preferences are stored locally in each browser.

### 问：我的偏好会在设备间同步吗？
**答：** 不会，偏好存储在每个浏览器本地。

---

### Q: Can I bookmark a specific language?
**A:** Currently no, but the page will remember your last choice.

### 问：我可以收藏特定语言的页面吗？
**答：** 目前不行，但页面会记住您的上次选择。

---

### Q: Why doesn't the demo data translate?
**A:** Currently, only UI elements translate. Demo data (AI responses, tables) remain in original language.

### 问：为什么演示数据不翻译？
**答：** 目前只翻译UI元素。演示数据（AI回复、表格）保持原始语言。

---

### Q: Can I add more languages?
**A:** Yes! Check the developer documentation for how to extend translations.

### 问：可以添加更多语言吗？
**答：** 可以！查看开发者文档了解如何扩展翻译。

---

## Developer Info | 开发者信息

**Want to customize or extend?**

See detailed documentation:
- [BILINGUAL_SUPPORT.md](BILINGUAL_SUPPORT.md) - Full technical guide
- [BILINGUAL_SUMMARY.md](../BILINGUAL_SUMMARY.md) - Implementation summary
- [BILINGUAL_TEST_REPORT.md](../BILINGUAL_TEST_REPORT.md) - Test results

**想要自定义或扩展？**

查看详细文档：
- [BILINGUAL_SUPPORT.md](BILINGUAL_SUPPORT.md) - 完整技术指南
- [BILINGUAL_SUMMARY.md](../BILINGUAL_SUMMARY.md) - 实现总结
- [BILINGUAL_TEST_REPORT.md](../BILINGUAL_TEST_REPORT.md) - 测试结果

---

## Feedback | 反馈

**Found an issue or have a suggestion?**

Create an issue: https://github.com/liqcui/ocp-performance-analyzer-mcp/issues

Please include:
- Which page (index.html or demo.html)
- Browser and version
- What you expected vs what happened
- Screenshots if possible

**发现问题或有建议？**

创建issue: https://github.com/liqcui/ocp-performance-analyzer-mcp/issues

请包含：
- 哪个页面 (index.html 或 demo.html)
- 浏览器和版本
- 期望结果 vs 实际结果
- 如果可能，提供截图

---

**Enjoy the bilingual demo! | 享受双语演示！** 🌍

**Live Demo:**
- 🌐 https://liqcui.github.io/ocp-performance-analyzer-mcp/
- 📖 https://liqcui.github.io/ocp-performance-analyzer-mcp/demo.html
