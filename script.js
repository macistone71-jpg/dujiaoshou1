// ============================================================
//  网站逻辑 —— 通用模板
//  读取 config.js 中的 SITE_CONFIG 自动渲染页面，无需改动本文件。
// ============================================================
const cfg = window.SITE_CONFIG || {};

// 简单的 HTML 转义，防止内容中的特殊字符破坏结构
function escapeHtml(str) {
  return String(str ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

// 按 id 填充文本
function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value ?? "";
}

// ---- 基础信息 ----
document.title = cfg.siteTitle || "我的个人网站";
setText("logo", cfg.logo);
setText("hero-greeting", cfg.greeting);
setText("hero-name", cfg.name);
setText("hero-role", cfg.role);
setText("hero-desc", cfg.intro);
setText("about-story", cfg.about?.story);
setText("about-philosophy", cfg.about?.philosophy);
setText("about-hobby", cfg.about?.hobby);
setText("footer-name", cfg.siteTitle || cfg.name);

// ---- 头像（支持 emoji 或图片地址）----
const avatarEl = document.getElementById("hero-avatar");
if (avatarEl) {
  const avatar = cfg.avatar || "👋";
  if (/^(https?:\/\/|data:image\/)/i.test(avatar) || /\.(png|jpe?g|gif|webp|svg)$/i.test(avatar)) {
    avatarEl.innerHTML = `<img src="${escapeHtml(avatar)}" alt="${escapeHtml(cfg.name || "")}" class="avatar-img" />`;
  } else {
    avatarEl.textContent = avatar;
  }
}

// ---- GitHub 链接（全站统一跳转到你的主页）----
const githubUrl = cfg.github
  ? `https://github.com/${encodeURIComponent(cfg.github)}`
  : "https://github.com/";

document.querySelectorAll(".github-link").forEach((a) => {
  a.href = githubUrl;
  if (cfg.github) a.title = `访问 ${cfg.github} 的 GitHub`;
});
document.querySelectorAll(".github-username").forEach((el) => {
  el.textContent = cfg.github ? `@${cfg.github}` : "GitHub";
});

// ---- 技能 ----
function renderSkills() {
  const grid = document.getElementById("skills-grid");
  if (!grid || !Array.isArray(cfg.skills)) return;
  grid.innerHTML = cfg.skills
    .map(
      (s) => `
      <div class="skill-item">
        <div class="skill-label"><span>${escapeHtml(s.name)}</span><span>${Number(s.level) || 0}%</span></div>
        <div class="skill-bar"><div class="skill-fill" data-level="${Number(s.level) || 0}"></div></div>
      </div>`
    )
    .join("");
}
renderSkills();

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
        ? `<a ${linkAttr} class="project-link">了解更多 →</a>`
        : "";
      const tagsHtml = (p.tags || [])
        .map((t) => `<span class="tag">${escapeHtml(t)}</span>`)
        .join("");
      return `
      <article class="project-card">
        <div class="project-thumb">${escapeHtml(p.icon || "📁")}</div>
        <div class="project-body">
          <h3>${escapeHtml(p.title)}</h3>
          <p>${escapeHtml(p.desc)}</p>
          <div class="project-tags">${tagsHtml}</div>
          ${linkHtml}
        </div>
      </article>`;
    })
    .join("");
}
renderProjects();

// ---- 联系 ----
setText(
  "contact-email",
  cfg.email ? cfg.email : ""
);
document.getElementById("contact-email")?.setAttribute(
  "href",
  cfg.email ? `mailto:${cfg.email}` : "#"
);

function renderExtraContact() {
  const box = document.getElementById("contact-links");
  if (!box || !Array.isArray(cfg.extraContact)) return;
  cfg.extraContact.forEach((c) => {
    if (!c.label) return;
    const a = document.createElement("a");
    a.className = "contact-card";
    a.href = c.href || "#";
    if (/^https?:\/\//i.test(c.href || "")) {
      a.target = "_blank";
      a.rel = "noopener";
    }
    a.innerHTML = `<span class="contact-icon">${escapeHtml(c.icon || "🔗")}</span><span>${escapeHtml(c.label)}</span>`;
    box.appendChild(a);
  });
}
renderExtraContact();

// 若填写了 website，提示 GitHub 主页可回链到这里
if (cfg.website) {
  const note = document.getElementById("back-note");
  if (note) {
    note.style.display = "block";
    note.textContent = `💡 提示：你可以在 GitHub 个人主页的 Website 栏填上 ${cfg.website}，实现网站与 GitHub 双向跳转。`;
  }
}

// ---- 页脚年份 ----
document.getElementById("year").textContent = new Date().getFullYear();

// ============================================================
//  交互逻辑
// ============================================================
// 移动端菜单开关
const menuToggle = document.getElementById("menu-toggle");
const navLinks = document.getElementById("nav-links");
menuToggle?.addEventListener("click", () => navLinks.classList.toggle("open"));
navLinks.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => navLinks.classList.remove("open"));
});

// 滚动时高亮当前导航项
const sections = document.querySelectorAll("section[id]");
const navAnchors = document.querySelectorAll(".nav-links a");

function highlightNav() {
  const scrollPos = window.scrollY + 120;
  let currentId = "home";
  sections.forEach((section) => {
    if (scrollPos >= section.offsetTop) currentId = section.id;
  });
  navAnchors.forEach((a) => {
    a.classList.toggle("active", a.getAttribute("href") === `#${currentId}`);
  });
}
window.addEventListener("scroll", highlightNav);
highlightNav();

// 技能条进入视口时动画展开
const skillObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const fill = entry.target;
        fill.style.width = `${fill.dataset.level}%`;
        skillObserver.unobserve(fill);
      }
    });
  },
  { threshold: 0.4 }
);

document.querySelectorAll(".skill-fill").forEach((fill) => skillObserver.observe(fill));
