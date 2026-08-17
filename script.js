// ============================================================
//  网站逻辑 —— 风格参考 rui.juzi.bot，数据来自 config.js
// ============================================================
const cfg = window.SITE_CONFIG || {};

function escapeHtml(str) {
  return String(str ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value ?? "";
}

// ---- 基础信息 ----
document.title = `${cfg.name || "个人网站"} · ${cfg.slogan || ""}`.trim();
setText("site-name", cfg.name);
setText("site-slogan", cfg.slogan);
setText("sidebar-name", cfg.name);
setText("footer-name", cfg.name);
setText("footer-slogan", cfg.slogan);
setText("about-meta", cfg.role);

// ---- 头像（文字 / emoji / 图片）----
const avatarEl = document.getElementById("sidebar-avatar");
if (avatarEl) {
  const avatar = cfg.avatar || cfg.name?.slice(0, 1) || "何";
  if (/^(https?:\/\/|data:image\/)/i.test(avatar) || /\.(png|jpe?g|gif|webp|svg)$/i.test(avatar)) {
    avatarEl.innerHTML = `<img src="${escapeHtml(avatar)}" alt="${escapeHtml(cfg.name || "")}" />`;
  } else {
    avatarEl.textContent = avatar;
  }
}

// ---- 关于我 ----
const aboutBox = document.getElementById("sidebar-about");
if (aboutBox) {
  aboutBox.innerHTML = (cfg.about || [])
    .map((p) => `<p>${escapeHtml(p)}</p>`)
    .join("");
}

// ---- 高亮卡片 ----
function renderHighlights() {
  const grid = document.getElementById("highlights-grid");
  if (!grid || !Array.isArray(cfg.highlights)) return;
  grid.innerHTML = cfg.highlights
    .map(
      (h) => `
      <a class="highlight-card" href="${escapeHtml(h.link || "#")}">
        <span class="highlight-arrow">→</span>
        <div class="highlight-num">${escapeHtml(h.number)}</div>
        <h3>${escapeHtml(h.title)}</h3>
        <p>${escapeHtml(h.desc)}</p>
      </a>`
    )
    .join("");
}
renderHighlights();

// ---- 文章列表 ----
function renderPosts() {
  const list = document.getElementById("posts-list");
  if (!list || !Array.isArray(cfg.posts)) return;
  list.innerHTML = cfg.posts
    .map(
      (p) => `
      <article class="post-item" data-search="${escapeHtml((p.title + " " + p.excerpt).toLowerCase())}">
        <h3 class="post-title"><a href="${escapeHtml(p.link || "#")}">${escapeHtml(p.title)}</a></h3>
        <div class="post-meta">
          <span>${escapeHtml(p.date)}</span> · <span class="post-cat">${escapeHtml(p.category)}</span>
        </div>
        <p class="post-excerpt">${escapeHtml(p.excerpt)}</p>
        <a class="post-more" href="${escapeHtml(p.link || "#")}">继续读 →</a>
      </article>`
    )
    .join("");
}
renderPosts();

// ---- 项目 ----
function renderProjects() {
  const grid = document.getElementById("projects-grid");
  if (!grid || !Array.isArray(cfg.projects)) return;
  grid.innerHTML = cfg.projects
    .map((p) => {
      const isExternal = /^https?:\/\//i.test(p.link || "");
      const linkAttr = p.link
        ? `href="${escapeHtml(p.link)}"${isExternal ? ' target="_blank" rel="noopener"' : ""}`
        : "";
      const linkHtml = p.link
        ? `<a ${linkAttr} class="project-link">查看 →</a>`
        : "";
      const tagsHtml = (p.tags || [])
        .map((t) => `<span class="tag">${escapeHtml(t)}</span>`)
        .join("");
      return `
      <div class="project-card">
        <div class="project-icon">${escapeHtml(p.icon || "📁")}</div>
        <h3>${escapeHtml(p.title)}</h3>
        <p>${escapeHtml(p.desc)}</p>
        <div class="project-tags">${tagsHtml}</div>
        ${linkHtml}
      </div>`;
    })
    .join("");
}
renderProjects();

// ---- 近期文章（侧边栏）----
function renderRecent() {
  const ul = document.getElementById("recent-posts");
  if (!ul || !Array.isArray(cfg.posts)) return;
  ul.innerHTML = cfg.posts
    .slice(0, 6)
    .map(
      (p) => `<li><a href="${escapeHtml(p.link || "#")}">${escapeHtml(p.title)}</a></li>`
    )
    .join("");
}
renderRecent();

// ---- 分类 ----
function renderCategories() {
  const ul = document.getElementById("categories");
  if (!ul || !Array.isArray(cfg.categories)) return;
  ul.innerHTML = cfg.categories
    .map(
      (c) =>
        `<li><a href="#writing"><span>${escapeHtml(c.name)}</span><span class="count">${escapeHtml(c.count)}</span></a></li>`
    )
    .join("");
}
renderCategories();

// ---- GitHub 链接 ----
const githubUrl = cfg.github
  ? `https://github.com/${encodeURIComponent(cfg.github)}`
  : "https://github.com/";
document.querySelectorAll(".github-link").forEach((a) => {
  a.href = githubUrl;
  if (cfg.github) a.title = `访问 ${cfg.github} 的 GitHub`;
});

// ---- 邮箱 ----
const emailEl = document.getElementById("contact-email");
if (emailEl) {
  if (cfg.email && cfg.email !== "you@example.com") {
    emailEl.href = `mailto:${cfg.email}`;
    emailEl.textContent = cfg.email;
  } else {
    emailEl.href = "mailto:";
    emailEl.textContent = "邮箱";
  }
}

// ---- 搜索过滤 ----
const searchInput = document.getElementById("search-input");
searchInput?.addEventListener("input", () => {
  const q = searchInput.value.trim().toLowerCase();
  document.querySelectorAll(".post-item").forEach((item) => {
    const hay = item.getAttribute("data-search") || "";
    item.style.display = q && !hay.includes(q) ? "none" : "";
  });
});

// ---- 页脚年份 ----
document.getElementById("year").textContent = new Date().getFullYear();

// ---- 移动端菜单 ----
const menuToggle = document.getElementById("menu-toggle");
const nav = document.getElementById("nav");
menuToggle?.addEventListener("click", () => nav.classList.toggle("open"));
nav.querySelectorAll("a").forEach((a) =>
  a.addEventListener("click", () => nav.classList.remove("open"))
);

// ---- 滚动高亮导航 ----
const sections = document.querySelectorAll("section[id], div[id='home']");
const navAnchors = document.querySelectorAll(".nav a");
function highlightNav() {
  const pos = window.scrollY + 100;
  let current = "home";
  sections.forEach((s) => {
    if (pos >= s.offsetTop) current = s.id;
  });
  navAnchors.forEach((a) => {
    const href = a.getAttribute("href") || "";
    a.classList.toggle("active", href === `#${current}`);
  });
}
window.addEventListener("scroll", highlightNav);
highlightNav();
