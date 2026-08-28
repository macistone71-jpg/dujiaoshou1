// ============================================================
//  网站基础配置
//  文章内容在 posts1.js ~ posts6.js，项目内容在 projects1.js ~ projects3.js
// ============================================================
window.SITE_CONFIG = {
  name: "何庆丰",
  slogan: "日拱一卒，功不唐捐",
  role: "产品经理 · 2 年经验",
  avatar: "https://avatars.githubusercontent.com/u/314186204?v=4", // 头像：GitHub 头像
  github: "macistone71-jpg",
  email: "macistone71@gmail.com",
  website: "https://macistone71-jpg.github.io/dujiaoshou1/",
  wechat: {
    name: "千秋少年创意园",
    // 微信公众号没有稳定的网页版主页，入口指向最新公开文章。
    url: "https://mp.weixin.qq.com/s/GpXb11O-Rpft1lFoCflEKQ",
  },

  // ---- 内容平台 ----
  // 在首页、侧边栏和页脚统一生成快捷入口。
  platforms: [
    {
      name: "小红书",
      handle: "千秋",
      desc: "产品、AI 与日常创作分享",
      action: "查看个人主页",
      mark: "红",
      tone: "xiaohongshu",
      url: "https://www.xiaohongshu.com/user/profile/5c5cd3d9000000001d03d04d",
    },
    {
      name: "人人都是产品经理",
      handle: "千秋折桂向轩辕",
      desc: "产品思考与 AI 实践文章",
      action: "查看作者主页",
      mark: "PM",
      tone: "woshipm",
      url: "https://www.woshipm.com/u/1685123",
    },
    {
      name: "少数派",
      handle: "@qrrzrkht",
      desc: "效率、创作与数字生活分享",
      action: "查看个人主页",
      mark: "少",
      tone: "sspai",
      url: "https://sspai.com/u/qrrzrkht/updates",
    },
  ],

  // ---- 关于我 ----
  about: [
    "何庆丰，做了两年产品经理。",
    "喜欢研究用户、拆解需求，把模糊的想法一步步做成能用的产品。",
    "这个网站是自己搭的，用来记录这两年的产品思考、踩过的坑和学到的东西。",
  ],

  // ---- 顶部高亮卡片 ----
  highlights: [
    { number: "11", title: "文章", desc: "个人网站 + 公众号内容", link: "#writing" },
    { number: "4", title: "项目", desc: "做过的产品与案例", link: "#projects" },
    { number: "→", title: "关于", desc: "关于我和这个网站", link: "#about" },
  ],

  // ---- 分类 ----
  categories: [
    { name: "公众号", count: 5 },
    { name: "思考", count: 4 },
    { name: "读书", count: 1 },
    { name: "项目", count: 1 },
  ],
};
