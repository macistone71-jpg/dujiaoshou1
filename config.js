// ============================================================
//  网站配置文件 —— 通用模板
//  只需修改这个文件，全站内容（包括所有 GitHub 跳转）会自动更新。
// ============================================================
window.SITE_CONFIG = {
  // ---- 基本信息 ----
  siteTitle: "我的个人网站",          // 浏览器标签标题
  logo: "我的网站",                   // 导航栏左上角文字
  name: "你的名字",                   // 你的名字 / 昵称
  greeting: "你好，我是",             // 首页问候语
  role: "前端开发者 · 创作者 · 终身学习者", // 身份/一句话介绍
  intro:
    "欢迎来到我的个人网站。这里记录了我的项目、技能与思考，也希望能与你产生一些有趣的连接。",
  avatar: "👋", // 头像：填 emoji 或图片地址（如 https://.../avatar.png）

  // ---- GitHub（改成你的用户名，全站 GitHub 按钮会自动指向你的主页）----
  github: "macistone71-jpg",          // 你的 GitHub 用户名
  email: "you@example.com",           // 你的邮箱
  website: "https://macistone71-jpg.github.io/dujiaoshou1/", // 本网站上线后的地址（部署后填，GitHub 主页可回链到这里）

  // ---- 关于我 ----
  about: {
    story:
      "我热爱把想法变成现实，喜欢用代码解决问题，也享受设计带来的美感。在工作与学习中，我始终保持好奇心，不断探索新的技术与可能性。",
    philosophy:
      "简单、清晰、有用。我相信好的产品应该让人感到自然，好的代码应该易于阅读和维护。持续迭代，比一次做到完美更重要。",
    hobby:
      "除了写代码，我还喜欢阅读、旅行、摄影和音乐。这些爱好让我保持对世界的敏感，也常常给我的创作带来灵感。",
  },

  // ---- 技能（name 名称 / level 熟练度 0-100）----
  skills: [
    { name: "HTML / CSS", level: 90 },
    { name: "JavaScript", level: 85 },
    { name: "Vue / React", level: 75 },
    { name: "Node.js", level: 70 },
    { name: "UI / 设计", level: 65 },
  ],

  // ---- 项目（icon emoji / title / desc / tags / link）----
  projects: [
    {
      icon: "🚀",
      title: "个人项目 1",
      desc: "这是我的第一个项目，简单介绍一下它做了什么、解决了什么问题。",
      tags: ["HTML", "CSS", "JS"],
      link: "", // 填仓库或演示地址，留空则不显示链接
    },
    {
      icon: "📱",
      title: "项目名称 2",
      desc: "这是一个还未完成的项目，用来展示你将来会添加的内容。",
      tags: ["Vue", "Node.js"],
      link: "",
    },
    {
      icon: "🎨",
      title: "项目名称 3",
      desc: "这里也可以放一个设计或创意类的项目，展示你的多元化能力。",
      tags: ["设计", "创意"],
      link: "",
    },
  ],

  // ---- 额外联系方式（可自行增删）----
  extraContact: [
    { icon: "💬", label: "微信 / 其他", href: "" },
  ],
};
