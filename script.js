// ============================================================
//  网站逻辑 —— 风格参考 rui.juzi.bot，数据来自 config.js
// ============================================================
const cfg = window.SITE_CONFIG || {};
const POSTS = window.POSTS || [];
const PROJECTS = window.PROJECTS || [];
const ARTICLE_VISUALS = window.ARTICLE_VISUALS || [];

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
    avatarEl.classList.remove("avatar-placeholder");
  } else {
    avatarEl.textContent = avatar;
    avatarEl.classList.add("avatar-placeholder");
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
function readingMinutes(post) {
  const chars = (post.content || []).reduce((sum, block) => {
    const text = block.p || block.h2 || block.quote || (block.list || []).join("");
    return sum + String(text || "").length;
  }, 0);
  return Math.max(1, Math.ceil(chars / 450));
}

function renderPosts() {
  const list = document.getElementById("posts-list");
  if (!list || !Array.isArray(POSTS)) return;
  list.innerHTML = POSTS
    .map((p, i) => {
      const cover = ARTICLE_VISUALS[i]?.[0];
      return `
      <article class="post-item" data-search="${escapeHtml((p.title + " " + p.excerpt).toLowerCase())}">
        ${cover ? `<a class="post-cover-link" href="#post-${i + 1}" data-post="${i}" aria-label="阅读：${escapeHtml(p.title)}"><img class="post-cover" src="${escapeHtml(cover.src)}" alt="" loading="lazy" /></a>` : ""}
        <div class="post-summary">
          <h3 class="post-title"><a href="#post-${i + 1}" data-post="${i}">${escapeHtml(p.title)}</a></h3>
          <div class="post-meta">
            <span>${escapeHtml(p.date)}</span> · <span class="post-cat">${escapeHtml(p.category)}</span> · <span>约 ${readingMinutes(p)} 分钟</span>
          </div>
          <p class="post-excerpt">${escapeHtml(p.excerpt)}</p>
          <a class="post-more" href="#post-${i + 1}" data-post="${i}">继续读 →</a>
        </div>
      </article>`;
    })
    .join("");
}
renderPosts();

// ---- 项目 ----
function renderProjects() {
  const grid = document.getElementById("projects-grid");
  if (!grid || !Array.isArray(PROJECTS)) return;
  grid.innerHTML = PROJECTS
    .map((p, i) => {
      const isExternal = /^https?:\/\//i.test(p.link || "");
      const linkHtml = p.link
        ? `<a href="${escapeHtml(p.link)}"${isExternal ? ' target="_blank" rel="noopener"' : ""} class="project-link">查看 →</a>`
        : `<span class="project-link" data-project="${i}">查看详情 →</span>`;
      const tagsHtml = (p.tags || [])
        .map((t) => `<span class="tag">${escapeHtml(t)}</span>`)
        .join("");
      return `
      <div class="project-card" data-project="${i}">
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

// ---- 重点项目 ----
function renderFeatured() {
  const grid = document.getElementById("featured-grid");
  const featured = window.FEATURED || [];
  if (!grid || !Array.isArray(featured)) return;
  grid.innerHTML = featured
    .map((p) => {
      const tagsHtml = (p.tags || [])
        .map((t) => `<span class="tag">${escapeHtml(t)}</span>`)
        .join("");
      return `
      <a class="project-card" href="${escapeHtml(p.link)}" target="_blank" rel="noopener">
        <div class="project-icon">${escapeHtml(p.icon || "⭐")}</div>
        <h3>${escapeHtml(p.title)}</h3>
        <p>${escapeHtml(p.desc)}</p>
        <div class="project-tags">${tagsHtml}</div>
        <span class="project-link">查看 →</span>
      </a>`;
    })
    .join("");
}
renderFeatured();

// ---- Skills ----
function renderSkills() {
  const grid = document.getElementById("skills-grid");
  const skills = window.SKILLS || [];
  if (!grid || !Array.isArray(skills)) return;
  grid.innerHTML = skills
    .map(
      (s) => `
      <a class="skill-card" href="${escapeHtml(s.repo)}" target="_blank" rel="noopener">
        <div class="skill-icon">${escapeHtml(s.icon)}</div>
        <div class="skill-info">
          <div class="skill-name">${escapeHtml(s.name)} <span class="skill-en">${escapeHtml(s.en)}</span></div>
          <div class="skill-desc">${escapeHtml(s.desc)}</div>
          <div class="skill-tags"><span class="tag">${escapeHtml(s.type)}</span></div>
        </div>
      </a>`
    )
    .join("");
}
renderSkills();

// ---- 近期文章（侧边栏）----
function renderRecent() {
  const ul = document.getElementById("recent-posts");
  if (!ul || !Array.isArray(POSTS)) return;
  ul.innerHTML = POSTS
    .slice(0, 6)
    .map(
      (p, i) => `<li><a href="#post-${i + 1}" data-post="${i}">${escapeHtml(p.title)}</a></li>`
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

// ============================================================
//  阅读弹窗（文章 / 项目详情）
// ============================================================
function renderBlocks(blocks) {
  return (blocks || [])
    .map((b) => {
      if (b.h2) return `<h2 class="article-h2">${escapeHtml(b.h2)}</h2>`;
      if (b.p) return `<p>${escapeHtml(b.p)}</p>`;
      if (b.quote) return `<blockquote class="article-quote">${escapeHtml(b.quote)}</blockquote>`;
      if (Array.isArray(b.list))
        return `<ul class="article-list">${b.list.map((i) => `<li>${escapeHtml(i)}</li>`).join("")}</ul>`;
      return "";
    })
    .join("");
}

function renderFigure(visual, extraClass = "") {
  if (!visual) return "";
  return `<figure class="article-figure ${extraClass}">
    <img src="${escapeHtml(visual.src)}" alt="${escapeHtml(visual.alt)}" loading="lazy" />
    <figcaption>${escapeHtml(visual.caption)}</figcaption>
  </figure>`;
}

function renderArticleBlocks(blocks, visuals) {
  const inlineVisuals = (visuals || []).slice(1);
  const slots = new Map();
  inlineVisuals.forEach((visual, index) => {
    let slot = Math.max(1, Math.round(((index + 1) / (inlineVisuals.length + 1)) * blocks.length));
    while (slots.has(slot) && slot < blocks.length - 1) slot += 1;
    slots.set(slot, visual);
  });
  return (blocks || []).map((block, index) => {
    const figure = slots.has(index + 1) ? renderFigure(slots.get(index + 1)) : "";
    return renderBlocks([block]) + figure;
  }).join("");
}

const modal = document.getElementById("modal");
const modalBody = document.getElementById("modal-body");
const modalPanel = modal?.querySelector(".modal-panel");
const readingProgress = document.getElementById("reading-progress");
let modalReturnHash = "#writing";
let activePostIndex = null;

function updateReadingProgress() {
  if (!modalPanel || !readingProgress) return;
  const available = modalPanel.scrollHeight - modalPanel.clientHeight;
  const progress = available > 0 ? (modalPanel.scrollTop / available) * 100 : 100;
  readingProgress.style.width = `${Math.min(100, Math.max(0, progress))}%`;
}
modalPanel?.addEventListener("scroll", updateReadingProgress, { passive: true });

function openModal(html) {
  modalBody.innerHTML = html;
  modal.classList.add("open");
  modal.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";
  if (modalPanel) {
    modalPanel.scrollTop = 0;
    modalPanel.focus();
  }
  updateReadingProgress();
}

function closeModal({ restoreHash = true } = {}) {
  modal.classList.remove("open");
  modal.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
  activePostIndex = null;
  document.title = `${cfg.name || "个人网站"} · ${cfg.slogan || ""}`.trim();
  if (restoreHash && location.hash.startsWith("#post-")) {
    history.replaceState(null, "", modalReturnHash || "#writing");
  }
}

function openPost(i, { updateUrl = true } = {}) {
  const p = POSTS[i];
  if (!p) return;
  if (!location.hash.startsWith("#post-")) modalReturnHash = location.hash || "#writing";
  activePostIndex = i;
  const visuals = ARTICLE_VISUALS[i] || [];
  document.title = `${p.title} · ${cfg.name || ""}`;
  if (updateUrl && location.hash !== `#post-${i + 1}`) {
    history.pushState({ post: i }, "", `#post-${i + 1}`);
  }
  openModal(`
    <article class="wechat-article">
      <header class="article-head">
        <div class="article-label">${escapeHtml(p.category)} · 产品思考</div>
        <h1 class="article-title" id="article-dialog-title">${escapeHtml(p.title)}</h1>
        <div class="article-byline">
          <span class="article-author">${escapeHtml(cfg.name || "何庆丰")}</span>
          <span>${escapeHtml(p.date)}</span>
          <span>约 ${readingMinutes(p)} 分钟阅读</span>
        </div>
      </header>
      ${renderFigure(visuals[0], "article-hero")}
      <div class="article-lead">${escapeHtml(p.excerpt)}</div>
      <div class="article-content">${renderArticleBlocks(p.content, visuals)}</div>
      <footer class="article-end">
        <span>END</span>
        <strong>${escapeHtml(cfg.name || "何庆丰")}</strong>
        <p>${escapeHtml(cfg.slogan || "日拱一卒，功不唐捐")}</p>
      </footer>
    </article>
  `);
}

function openProject(i) {
  const p = PROJECTS[i];
  if (!p) return;
  const linkHtml = p.link
    ? `<a class="article-cta" href="${escapeHtml(p.link)}" target="_blank" rel="noopener">查看仓库 →</a>`
    : "";
  openModal(`
    <div class="article-head">
      <div class="article-meta"><span class="post-cat">项目</span></div>
      <h1 class="article-title">${escapeHtml(p.icon || "")} ${escapeHtml(p.title)}</h1>
    </div>
    <div class="article-content">${renderBlocks(p.detail)}</div>
    ${linkHtml}
  `);
}

// 事件委托：打开文章 / 项目详情 / 关闭弹窗
document.addEventListener("click", (e) => {
  const post = e.target.closest("[data-post]");
  if (post) {
    e.preventDefault();
    openPost(Number(post.dataset.post));
    return;
  }
  const proj = e.target.closest("[data-project]");
  if (proj && !e.target.closest("a")) {
    openProject(Number(proj.dataset.project));
    return;
  }
  if (e.target.closest("[data-close]")) closeModal();
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeModal();
});

function openPostFromHash() {
  const match = location.hash.match(/^#post-(\d+)$/);
  if (match) {
    openPost(Number(match[1]) - 1, { updateUrl: false });
  } else if (modal?.classList.contains("open") && activePostIndex !== null) {
    closeModal({ restoreHash: false });
  }
}
window.addEventListener("popstate", openPostFromHash);
openPostFromHash();

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
