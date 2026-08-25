#!/usr/bin/env python3
"""Generate the 30 original SVG editorial illustrations used by the six articles."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / "assets" / "illustrations"
OUT.mkdir(parents=True, exist_ok=True)

PALETTES = [
    ("#B85C38", "#FFF4EC", "#F2C7AE", "#4A2418"),
    ("#276B64", "#ECF8F4", "#A9D9CC", "#163D39"),
    ("#6A5AA3", "#F4F0FF", "#CFC4F3", "#342A59"),
    ("#9A6B1F", "#FFF8E8", "#E7C77E", "#4D350F"),
    ("#3568A8", "#EEF5FF", "#B6D1F3", "#183B68"),
    ("#A3475B", "#FFF0F3", "#EDBAC5", "#552331"),
]

DATA = [
    [
        ("用户价值", "产品经理真正的判断原点", ["新体验", "旧体验", "替换成本"]),
        ("价值公式", "新体验 − 旧体验 − 替换成本", ["感知提升", "真实替代", "切换阻力"]),
        ("价值三层", "从能用，到好用，再到认同", ["功能价值", "体验价值", "情感价值"]),
        ("价值三问", "增量、阻力与投入产出", ["好了多少？", "代价多大？", "值得做吗？"]),
        ("价值闭环", "定义 → 验证 → 复盘 → 迭代", ["看行为", "追结果", "持续改"]),
    ],
    [
        ("需求分析五步法", "把模糊诉求变成可交付方案", ["用户场景", "价值判断", "交付验证"]),
        ("先定义问题", "谁，在什么场景，遇到什么问题", ["用户", "场景", "问题"]),
        ("问题不是方案", "先追问为什么，再讨论怎么做", ["表层诉求", "真实问题", "多种解法"]),
        ("先定义成功", "过程指标与结果指标要同时看", ["使用率", "完成率", "结果改善"]),
        ("可交付需求", "正常流程、异常流程、不做清单", ["讲清背景", "写全边界", "对齐指标"]),
    ],
    [
        ("产品经典阅读月", "从大师思想回到真实实践", ["用户价值", "克制聚焦", "长期主义"]),
        ("思想坐标", "理性计算与用户情绪彼此补全", ["俞军", "张小龙", "梁宁"]),
        ("共同的答案", "理解用户、保持克制、长期主义", ["用户", "聚焦", "耐心"]),
        ("读书方法", "带着问题读，读完就写，写完去用", ["读", "写", "用"]),
        ("行动清单", "让读到的思想进入每一次决策", ["算价值", "做减法", "勤复盘"]),
    ],
    [
        ("做减法", "好产品不是少，而是没有多余", ["清晰", "简单", "自然"]),
        ("功能越多", "认知负担与维护成本同步上升", ["入口拥挤", "选择困难", "体验稀释"]),
        ("减法三步", "盘点 → 诊断 → 验证", ["看数据", "找原因", "小步灰度"]),
        ("一进一出", "每加一个功能，也审视一个旧功能", ["控制总量", "保护核心", "持续体检"]),
        ("克制检查", "砍掉不重要的，让重要的更突出", ["低使用", "低价值", "可替代"]),
    ],
    [
        ("AI 做产品", "把执行交给 AI，把判断留给自己", ["效率", "判断", "责任"]),
        ("四个场景", "竞品、访谈、文档与数据整理", ["竞品分析", "访谈纪要", "文档初稿"]),
        ("人机工作流", "喂足上下文 → AI 草稿 → 人工把关", ["结构输入", "快速初稿", "逐项核对"]),
        ("AI 的边界", "判断、品味、同理心与责任", ["不能外包", "必须共情", "最终负责"]),
        ("安全使用", "不迷信、不泄密、不跳过核对", ["事实核验", "数据脱敏", "保留判断"]),
    ],
    [
        ("从执行到负责", "一个小功能的完整上线闭环", ["需求", "上线", "复盘"]),
        ("先确认痛点", "访谈与数据互相印证", ["找用户", "看现场", "翻数据"]),
        ("异常流程", "正常流程之外，才是真正的产品功力", ["断网", "并发", "误删"]),
        ("上线验证", "使用、完成与结果数据缺一不可", ["使用率", "完成率", "投诉变化"]),
        ("负责的闭环", "调研 → 交付 → 验收 → 数据 → 复盘", ["敢拍板", "盯结果", "持续迭代"]),
    ],
]


def svg(article_no, visual_no, title, subtitle, labels):
    accent, pale, soft, ink = PALETTES[article_no - 1]
    subtitle_lines = [subtitle[i:i + 18] for i in range(0, len(subtitle), 18)]
    subtitle_svg = "".join(
        f'<text x="116" y="{326 + i * 39}" class="subtitle" fill="{ink}" opacity=".72">{escape(line)}</text>'
        for i, line in enumerate(subtitle_lines)
    )
    label_svg = []
    for i, label in enumerate(labels):
        y = 246 + i * 92
        num = f"0{i + 1}"
        label_svg.append(f'''<g>
          <rect x="705" y="{y}" width="355" height="70" rx="20" fill="#FFFFFF" fill-opacity=".82"/>
          <circle cx="748" cy="{y + 35}" r="23" fill="{accent}"/>
          <text x="748" y="{y + 42}" text-anchor="middle" class="num">{num}</text>
          <text x="788" y="{y + 43}" class="label">{escape(label)}</text>
        </g>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(subtitle)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{pale}"/><stop offset="1" stop-color="#FFFFFF"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="{ink}" flood-opacity=".10"/></filter>
  </defs>
  <style>
    .kicker,.num{{font:700 18px -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;letter-spacing:2px}}
    .title{{font:800 54px -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}}
    .subtitle{{font:400 24px -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}}
    .label{{font:700 25px -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}}
    .foot{{font:500 17px -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;letter-spacing:1px}}
  </style>
  <rect width="1200" height="675" rx="36" fill="url(#bg)"/>
  <circle cx="1070" cy="76" r="170" fill="{soft}" fill-opacity=".45"/>
  <circle cx="1130" cy="620" r="245" fill="{accent}" fill-opacity=".07"/>
  <path d="M0 550 C220 475 320 655 560 575 C770 505 870 595 1200 485 V675 H0Z" fill="{soft}" fill-opacity=".22"/>
  <g filter="url(#shadow)"><rect x="72" y="72" width="1056" height="531" rx="32" fill="#FFFFFF" fill-opacity=".48"/></g>
  <text x="116" y="142" class="kicker" fill="{accent}">何庆丰 · 产品思考  /  A{article_no:02d}—{visual_no:02d}</text>
  <text x="116" y="252" class="title" fill="{ink}">{escape(title)}</text>
  {subtitle_svg}
  <rect x="116" y="428" width="92" height="8" rx="4" fill="{accent}"/>
  <text x="116" y="500" class="foot" fill="{ink}" opacity=".65">日拱一卒 · 功不唐捐</text>
  <g>{''.join(label_svg)}</g>
  <path d="M640 190 V500" stroke="{accent}" stroke-width="2" stroke-dasharray="6 10" opacity=".25"/>
</svg>'''


for a_idx, visuals in enumerate(DATA, 1):
    for v_idx, item in enumerate(visuals, 1):
        name = f"article-{a_idx}-{v_idx}.svg"
        (OUT / name).write_text(svg(a_idx, v_idx, *item), encoding="utf-8")

print(f"Generated {sum(map(len, DATA))} SVG files in {OUT}")
