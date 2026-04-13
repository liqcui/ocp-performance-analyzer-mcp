# 🌐 Bilingual Support (双语支持)

## Overview / 概述

Both demo pages now support **English** and **Chinese** with instant language switching.

两个演示页面现在都支持**英文**和**中文**，可以即时切换语言。

---

## Features / 功能特性

### ✅ Supported Pages / 支持的页面

1. **index.html** - Interactive Demo / 交互式演示
   - URL: https://liqcui.github.io/ocp-performance-analyzer-mcp/

2. **demo.html** - Documentation Demo / 文档演示
   - URL: https://liqcui.github.io/ocp-performance-analyzer-mcp/demo.html

### ✅ What Gets Translated / 翻译内容

#### index.html
- **EN/ZH:**
  - Page title / 页面标题
  - Tab labels (AI Chat, Architecture, Demo) / 标签 (AI聊天、架构、演示)
  - Sidebar title and subtitle / 侧边栏标题和副标题
  - All 9 quick action buttons / 全部9个快速操作按钮
  - Status indicators / 状态指示器
  - Welcome message / 欢迎消息

#### demo.html
- **EN/ZH:**
  - Header title and subtitle / 页头标题和副标题
  - Navigation menu (6 items) / 导航菜单 (6项)
  - Section titles (6 sections) / 章节标题 (6个章节)

---

## Usage / 使用方法

### How to Switch Language / 如何切换语言

#### Method 1: Click Button / 方法1: 点击按钮

**index.html:**
```
Look for button in top-right corner of header area
在页头区域右上角查找按钮

Click: EN → Switches to English
点击: EN → 切换到英文

Click: 中文 → Switches to Chinese
点击: 中文 → 切换到中文
```

**demo.html:**
```
Look for floating button in top-right corner of page
在页面右上角查找浮动按钮

Click: EN → Switches to English
点击: EN → 切换到英文

Click: 中文 → Switches to Chinese
点击: 中文 → 切换到中文
```

#### Method 2: Automatic / 方法2: 自动

- **First Visit:** Defaults to Chinese / 首次访问：默认中文
- **After Toggle:** Preference saved to browser / 切换后：偏好保存到浏览器
- **Next Visit:** Automatically uses your last choice / 下次访问：自动使用上次选择

### Visual Guide / 视觉指南

```
Before / 切换前:
┌────────────────────────────────────┐
│  性能分析演示界面        [EN] ←   │  Click here / 点击这里
└────────────────────────────────────┘

After / 切换后:
┌────────────────────────────────────┐
│  Performance Analysis Demo  [中文] │
└────────────────────────────────────┘
```

---

## Technical Implementation / 技术实现

### Architecture / 架构

```javascript
// Language preference storage
localStorage.setItem('preferredLanguage', 'en'|'zh')

// Translation data structure
const translations = {
    zh: { 'key': '中文文本' },
    en: { 'key': 'English text' }
}

// HTML markup
<h2 data-i18n="key">中文文本</h2>

// JavaScript function
function applyLanguage() {
    document.querySelectorAll('[data-i18n]').forEach(...)
}
```

### Files Modified / 修改的文件

1. **docs/index.html**
   - Added CSS: `.lang-toggle` button styling
   - Added HTML: Language toggle button in header
   - Added JS: Translation system (145 lines)
   - Added: `data-i18n` attributes to elements

2. **docs/demo.html**
   - Added CSS: Floating `.lang-toggle` button
   - Added HTML: Language toggle button (fixed position)
   - Added JS: Translation system (114 lines)
   - Added: `data-i18n` attributes to navigation and sections

---

## Browser Compatibility / 浏览器兼容性

✅ **Supported / 支持:**
- Chrome 90+ / 谷歌浏览器 90+
- Firefox 88+ / 火狐浏览器 88+
- Safari 14+ / 苹果浏览器 14+
- Edge 90+ / 微软Edge 90+

✅ **Features / 功能:**
- `localStorage` for preference persistence / 偏好持久化
- `querySelectorAll` for element selection / 元素选择
- `forEach` for iteration / 迭代

---

## Customization / 自定义

### Adding New Translations / 添加新翻译

**Step 1: Add to translations object / 步骤1: 添加到翻译对象**
```javascript
const translations = {
    zh: {
        'new-key': '新的中文文本',
        // ... existing translations
    },
    en: {
        'new-key': 'New English text',
        // ... existing translations
    }
};
```

**Step 2: Add data-i18n attribute to HTML / 步骤2: 在HTML中添加data-i18n属性**
```html
<h3 data-i18n="new-key">新的中文文本</h3>
```

**Step 3: Test / 步骤3: 测试**
- Toggle language to see changes
- Check browser console for errors

### Extending to New Pages / 扩展到新页面

1. Copy CSS for `.lang-toggle` / 复制 `.lang-toggle` CSS
2. Copy HTML for button / 复制按钮HTML
3. Copy JavaScript translation system / 复制JavaScript翻译系统
4. Add `data-i18n` attributes / 添加 `data-i18n` 属性
5. Update `translations` object / 更新 `translations` 对象

---

## Testing Checklist / 测试清单

### ✅ Functionality Tests / 功能测试

- [x] Language toggle button visible / 语言切换按钮可见
- [x] Clicking button switches language / 点击按钮切换语言
- [x] All labeled elements update / 所有标记元素更新
- [x] Preference persists after page reload / 刷新页面后偏好保持
- [x] Works in both pages (index.html, demo.html) / 两个页面都工作

### ✅ Visual Tests / 视觉测试

- [x] Button styling correct / 按钮样式正确
- [x] Button hover effect works / 按钮悬停效果工作
- [x] Text doesn't overflow / 文字不溢出
- [x] Layout remains intact / 布局保持完整
- [x] Mobile responsive / 移动端响应式

### ✅ Content Tests / 内容测试

- [x] All Chinese text translates / 所有中文文本翻译
- [x] All English text correct / 所有英文文本正确
- [x] Emojis preserved / 表情符号保留
- [x] Technical terms accurate / 技术术语准确
- [x] Grammar correct in both languages / 两种语言语法正确

---

## Common Issues / 常见问题

### Issue 1: Preference Not Saving / 问题1: 偏好不保存

**Cause:** Browser blocking localStorage
**Solution:**
```javascript
// Check if localStorage is available
if (typeof(Storage) !== "undefined") {
    localStorage.setItem('preferredLanguage', lang);
}
```

### Issue 2: Some Text Not Translating / 问题2: 部分文字不翻译

**Cause:** Missing `data-i18n` attribute or translation key
**Solution:**
1. Add `data-i18n="key"` to HTML element
2. Add translation to `translations` object
3. Refresh page

### Issue 3: Button Not Visible / 问题3: 按钮不可见

**Cause:** CSS z-index or positioning issue
**Solution:**
```css
.lang-toggle {
    z-index: 1000; /* or higher */
    position: fixed; /* for demo.html */
}
```

---

## Statistics / 统计信息

### Translation Coverage / 翻译覆盖

**index.html:**
- UI Elements: 15+ / UI元素: 15+
- Quick Actions: 9 / 快速操作: 9
- Status Messages: 2 / 状态消息: 2
- **Total: 26+ translatable strings** / **总计: 26+可翻译字符串**

**demo.html:**
- Navigation Items: 6 / 导航项: 6
- Section Titles: 6 / 章节标题: 6
- Header Elements: 2 / 页头元素: 2
- **Total: 14+ translatable strings** / **总计: 14+可翻译字符串**

### Code Size / 代码大小

**index.html:**
- CSS: ~15 lines / CSS: ~15行
- JavaScript: ~145 lines / JavaScript: ~145行
- HTML attributes: ~26 additions / HTML属性: ~26处添加

**demo.html:**
- CSS: ~22 lines / CSS: ~22行
- JavaScript: ~114 lines / JavaScript: ~114行
- HTML attributes: ~14 additions / HTML属性: ~14处添加

---

## Future Enhancements / 未来增强

### Planned / 计划中

1. ⭐ **More Languages** / 更多语言
   - Japanese / 日语
   - Korean / 韩语
   - German / 德语
   - French / 法语

2. ⭐ **Auto-detect Browser Language** / 自动检测浏览器语言
   ```javascript
   const browserLang = navigator.language.split('-')[0];
   ```

3. ⭐ **Translate Demo Data** / 翻译演示数据
   - Analysis messages / 分析消息
   - AI insights / AI洞察
   - Table headers / 表头

4. ⭐ **URL Parameter** / URL参数
   - `?lang=en` or `?lang=zh`
   - Direct linking to specific language

### Nice to Have / 锦上添花

- Flag icons instead of text / 旗帜图标代替文字
- Keyboard shortcut (Alt+L) / 键盘快捷键 (Alt+L)
- Accessibility improvements / 无障碍改进
- Translation animation / 翻译动画

---

## Contributing / 贡献

### How to Improve Translations / 如何改进翻译

1. **Fork repository** / Fork 仓库
2. **Edit `translations` object** / 编辑 `translations` 对象
3. **Test changes** / 测试更改
4. **Submit pull request** / 提交 pull request

### Translation Guidelines / 翻译指南

**DO / 推荐:**
- Keep technical terms consistent / 保持技术术语一致
- Preserve emojis / 保留表情符号
- Use professional tone / 使用专业语气
- Test in real browsers / 在真实浏览器中测试

**DON'T / 避免:**
- Don't auto-translate / 不要机器翻译
- Don't break layouts / 不要破坏布局
- Don't remove context / 不要删除上下文
- Don't change meaning / 不要改变含义

---

## Credits / 致谢

- **Implementation:** Claude Code + liqcui
- **Testing:** Manual testing on Chrome, Firefox
- **Design:** Based on web demo UI patterns
- **Date:** 2026-04-14

---

## Support / 支持

**Issues:** https://github.com/liqcui/ocp-performance-analyzer-mcp/issues

**Questions:**
- English: Create GitHub issue with `[i18n]` tag
- 中文: 在GitHub上创建带`[i18n]`标签的issue

---

**Language Toggle Available On / 语言切换功能已在以下页面启用:**
- ✅ https://liqcui.github.io/ocp-performance-analyzer-mcp/
- ✅ https://liqcui.github.io/ocp-performance-analyzer-mcp/demo.html

**Try it now! / 现在就试试！** 🌍
