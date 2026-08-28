# 个人网站 · 通用模板

一个简洁现代的个人网站模板，所有内容都集中在一个配置文件里，改一处全站生效，并且内置了 **GitHub 双向跳转**。

首页的“内容平台”区域会从 `config.js` 的 `platforms` 配置自动生成，并同步显示在侧边栏和页脚，方便集中维护小红书、人人都是产品经理、少数派等个人入口。

## 文件说明

| 文件 | 作用 |
|------|------|
| `index.html` | 页面结构（一般不用改） |
| `style.css` | 样式（一般不用改） |
| `script.js` | 渲染与交互逻辑（一般不用改） |
| `config.js` | ✅ **你唯一需要修改的文件**，所有个人信息都在这里 |

## 快速开始

### 1. 修改配置

打开 `config.js`，把里面的占位内容改成你自己的：

```js
window.SITE_CONFIG = {
  name: "你的名字",              // 改成你的名字
  role: "前端开发者",            // 你的身份
  avatar: "👋",                 // 头像：emoji 或图片地址
  github: "your-username",      // ⭐ 改成你的 GitHub 用户名（关键！）
  email: "you@example.com",     // 你的邮箱
  website: "",                  // 网站上线后的地址（实现双向跳转用）
  // ...技能、项目、关于我等，按需修改
};
```

### 2. 本地预览

直接双击 `index.html` 即可在浏览器中打开。

### 3. 部署到 GitHub Pages（实现双向跳转）

1. 在 GitHub 新建一个仓库，例如 `my-website`。
2. 把本文件夹里的文件上传到该仓库。
3. 进入仓库 **Settings → Pages**，把 Source 设为 `main` 分支（根目录）。
4. 稍等片刻，GitHub 会给你一个网址，形如 `https://你的用户名.github.io/my-website/`。
5. 把这个网址填回 `config.js` 的 `website` 字段，重新上传。

### 4. 设置 GitHub 主页回链（双向跳转）

1. 打开你的 GitHub 个人主页 → **Edit profile**。
2. 在 **Website** 一栏填入上面的网址并保存。

这样：
- **网站 → GitHub**：网站导航栏、首页按钮、联系区、页脚都有 GitHub 入口，自动指向你的主页。
- **GitHub → 网站**：你的 GitHub 主页会显示网站链接，点击即可回到本网站。

## 常见自定义

- **加项目**：在 `config.js` 的 `projects` 数组里新增一项，包含 `icon / title / desc / tags / link`。
- **改技能**：修改 `skills` 数组，`level` 为 0–100 的熟练度。
- **换颜色**：打开 `style.css`，修改顶部 `:root` 里的 `--primary` 等变量。
- **加联系方式**：在 `extraContact` 数组里添加 `{ icon, label, href }`。
