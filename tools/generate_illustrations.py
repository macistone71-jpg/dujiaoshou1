#!/usr/bin/env python3
"""Generate 30 original hand-drawn, story-led SVG illustrations."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / "assets" / "illustrations"
OUT.mkdir(parents=True, exist_ok=True)

PALETTES = [
    ("#C65D3B", "#FFF7EE", "#F4C9AA", "#315B55", "#302A26"),
    ("#2F7A70", "#F3FBF7", "#B9DED3", "#D8913D", "#28332F"),
    ("#725FA8", "#F8F5FF", "#D8CEF4", "#D58B57", "#322E3D"),
    ("#A87725", "#FFFAEF", "#E9D29C", "#64806A", "#393125"),
    ("#3D72B4", "#F3F8FF", "#C8DCF5", "#D97857", "#293747"),
    ("#B34E68", "#FFF5F7", "#F0C5CF", "#507A70", "#3D2D32"),
]

# title, subtitle, scene, three story beats
DATA = [
  [
    ("用户价值", "深夜复盘时，小何终于问对了问题", "desk", ["功能做了很多", "用户真的变好了吗？", "判断从这里开始"]),
    ("价值公式", "用户从旧办法走向新体验，中间隔着一条河", "bridge", ["旧体验", "替换成本", "新体验"]),
    ("价值三层", "产品价值不是电梯，而是一阶阶爬上去的楼梯", "stairs", ["能完成", "更舒服", "愿认同"]),
    ("价值三问", "先别画原型，坐到用户身边问清楚", "interview", ["好了多少？", "代价多大？", "值得做吗？"]),
    ("价值闭环", "上线不是句号，数据会带你回到下一次迭代", "cycle", ["定义", "验证", "复盘"]),
  ],
  [
    ("需求分析五步法", "需求像一团毛线，要耐心找到线头", "storm", ["谁在用？", "哪里卡住？", "怎样算成功？"]),
    ("先定义问题", "客服说要导出按钮，小何先去看他怎么工作", "observe", ["用户", "场景", "问题"]),
    ("问题不是方案", "同一个问题前，永远不只一条路", "fork", ["别急着做按钮", "追问为什么", "再比较解法"]),
    ("先定义成功", "上线前，先把终点线画在白板上", "dashboard", ["使用率", "完成率", "结果改善"]),
    ("可交付需求", "评审桌上，正常流程和意外都要摊开讲", "review", ["正常流程", "异常流程", "不做清单"]),
  ],
  [
    ("产品经典阅读月", "踩过坑再读经典，书里的话突然有了温度", "books", ["带着问题读", "对照真实经历", "写下自己的答案"]),
    ("思想坐标", "理性和感性坐在同一张桌上讨论产品", "roundtable", ["算清价值", "理解情绪", "做出取舍"]),
    ("共同的答案", "不同的书，最后都指向同一座山", "flags", ["理解用户", "保持克制", "相信长期"]),
    ("从读到用", "读书、写作、实践，三块石头才能过河", "stepping", ["读进去", "写明白", "用起来"]),
    ("行动清单", "合上书后，小何把六件小事贴到了工位上", "checklist", ["每周算价值", "每月写复盘", "每天做少一点"]),
  ],
  [
    ("做减法", "按钮塞满屏幕时，用户反而找不到出口", "clutter", ["功能越来越多", "核心越来越小", "该清一清了"]),
    ("功能越多", "每多一件行李，产品就走得更慢一点", "baggage", ["认知负担", "维护成本", "体验被稀释"]),
    ("减法三步", "团队把僵尸功能搬到桌上，一件件检查", "cleanup", ["盘点", "诊断", "灰度验证"]),
    ("一进一出", "新功能上船前，先问旧功能是否还该占位", "seesaw", ["新增一个", "审视一个", "保护核心"]),
    ("克制检查", "清空杂物后，用户终于一眼看见最重要的按钮", "door", ["少一点打扰", "多一点清晰", "把核心做深"]),
  ],
  [
    ("AI 做产品", "小何多了一位速度很快、但需要带教的实习生", "robot", ["AI 先打草稿", "人来做判断", "结果共同变好"]),
    ("四个高频场景", "机器人搬走资料堆，小何终于抬头思考", "piles", ["竞品资料", "访谈纪要", "数据归类"]),
    ("人机工作流", "AI 交上初稿，小何拿起红笔逐项核对", "redpen", ["喂足上下文", "生成初稿", "人工把关"]),
    ("AI 的边界", "线的这边是效率，线的那边是人的责任", "boundary", ["判断", "共情", "负责"]),
    ("安全使用 AI", "敏感数据进门前，先经过脱敏和核验两道锁", "lock", ["事实核验", "数据脱敏", "不外包判断"]),
  ],
  [
    ("从执行到负责", "这一次，小何接过的不只是任务，还有结果", "baton", ["以前：把活做完", "现在：把结果做好", "责任开始生长"]),
    ("先确认痛点", "他坐到客服旁边，看见便签如何让交接断线", "support", ["访谈五个人", "观察真实操作", "再用数据印证"]),
    ("异常流程", "评审会上，三个问题把“小功能”问出了深水区", "questions", ["保存多久？", "同时编辑呢？", "误删怎么办？"]),
    ("上线验证", "发布那晚，小何盯着三块数据屏不敢眨眼", "launch", ["使用率", "完成率", "投诉变化"]),
    ("负责的闭环", "每踩一个坑，就把它垫成下一步台阶", "retro", ["调研", "交付", "复盘再出发"]),
  ],
]


def txt(x, y, text, cls="note", anchor=None, rotate=None):
    attrs = f' class="{cls}"'
    if anchor: attrs += f' text-anchor="{anchor}"'
    if rotate: attrs += f' transform="rotate({rotate} {x} {y})"'
    return f'<text x="{x}" y="{y}"{attrs}>{escape(text)}</text>'


def path(d, stroke="#302A26", width=4, fill="none", dash=""):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{width}" fill="{fill}" stroke-linecap="round" stroke-linejoin="round"{ds}/>'


def person(x, y, shirt, facing=1, mood="smile", scale=1.0, prop=""):
    # y is floor level
    sx = facing
    eye = ":)" if mood == "smile" else ":|"
    prop_svg = ""
    if prop == "paper":
        prop_svg = f'<rect x="{x+sx*45-22}" y="{y-118}" width="54" height="68" rx="5" fill="#fff" stroke="#302A26" stroke-width="3" transform="rotate({sx*7} {x+sx*45} {y-84})"/>'
    elif prop == "book":
        prop_svg = f'<path d="M{x-2} {y-92} q{sx*38} -18 {sx*70} 0 v42 q{-sx*34} -18 {-sx*70} 0z" fill="#fff" stroke="#302A26" stroke-width="3"/>'
    elif prop == "pen":
        prop_svg = path(f"M{x+sx*25} {y-90} L{x+sx*72} {y-128}", shirt, 6)
    return f'''<g class="sketch" transform="translate({x} {y}) scale({scale}) translate({-x} {-y})">
      <circle cx="{x}" cy="{y-184}" r="34" fill="#FFD9BC" stroke="#302A26" stroke-width="4"/>
      <path d="M{x-31} {y-193} q30 -45 62 0 q-13 -10 -20 -26 q-20 18 -42 20" fill="#43352F" stroke="#302A26" stroke-width="3"/>
      <text x="{x}" y="{y-174}" text-anchor="middle" class="face">{eye}</text>
      <path d="M{x} {y-148} C{x-sx*8} {y-110} {x+sx*6} {y-66} {x} {y-36}" stroke="#302A26" stroke-width="5" fill="{shirt}"/>
      <path d="M{x-34} {y-139} Q{x-58} {y-92} {x-74} {y-75}" stroke="#302A26" stroke-width="5" fill="none"/>
      <path d="M{x+34} {y-139} Q{x+sx*55} {y-106} {x+sx*64} {y-80}" stroke="#302A26" stroke-width="5" fill="none"/>
      <path d="M{x-4} {y-38} L{x-34} {y}" stroke="#302A26" stroke-width="6"/>
      <path d="M{x+4} {y-38} L{x+34} {y}" stroke="#302A26" stroke-width="6"/>
      <path d="M{x-48} {y} h30 M{x+18} {y} h30" stroke="#302A26" stroke-width="6" stroke-linecap="round"/>
      {prop_svg}
    </g>'''


def robot(x, y, accent):
    return f'''<g class="sketch">
      <rect x="{x-54}" y="{y-192}" width="108" height="92" rx="24" fill="#EAF3FF" stroke="#302A26" stroke-width="4"/>
      <path d="M{x} {y-192} v-30 m-10 0 h20" stroke="#302A26" stroke-width="4"/>
      <circle cx="{x-24}" cy="{y-151}" r="8" fill="{accent}"/><circle cx="{x+24}" cy="{y-151}" r="8" fill="{accent}"/>
      <path d="M{x-22} {y-126} q22 18 44 0" stroke="#302A26" stroke-width="3" fill="none"/>
      <rect x="{x-42}" y="{y-96}" width="84" height="74" rx="15" fill="{accent}" opacity=".82" stroke="#302A26" stroke-width="4"/>
      <path d="M{x-42} {y-76} l-42 -25 m126 25 l42 -25 M{x-20} {y-20} l-18 24 m58 -24 18 24" stroke="#302A26" stroke-width="5"/>
    </g>'''


def bubble(x, y, w, text, accent, flip=False):
    tail = f'M{x+w-36} {y+68} l22 28 l-42 -20' if flip else f'M{x+36} {y+68} l-22 28 l42 -20'
    return f'''<g class="sketch"><rect x="{x}" y="{y}" width="{w}" height="76" rx="25" fill="#fff" stroke="{accent}" stroke-width="3"/>{path(tail, accent, 3, '#fff')}{txt(x+w/2,y+47,text,'bubble', 'middle')}</g>'''


def sticky(x, y, text, fill, rot=0, w=150, h=88):
    return f'''<g transform="rotate({rot} {x+w/2} {y+h/2})" class="sketch"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="#302A26" stroke-width="3"/><path d="M{x+w-28} {y} l28 28 h-28z" fill="#fff" opacity=".6"/>{txt(x+w/2,y+h/2+8,text,'sticky','middle')}</g>'''


def arrow(x1,y1,x2,y2,color):
    return path(f'M{x1} {y1} Q{(x1+x2)/2} {min(y1,y2)-30} {x2} {y2} m-18 -12 l18 12 l-17 14',color,4)


def scene_svg(scene, beats, accent, soft, alt, ink):
    a,b,c = beats
    ground = path('M90 535 Q260 522 430 536 T770 534 T1110 538', ink, 3, 'none', '8 10')
    if scene == 'desk':
        return f'''{ground}{person(305,530,accent,1,'neutral','1','paper')}<rect x="475" y="350" width="390" height="150" rx="12" fill="#fff" stroke="{ink}" stroke-width="4" class="sketch"/>{sticky(505,375,a,soft,-4,105,72)}{sticky(625,365,b,'#FFE4A8',4,180,82)}{sticky(735,448,c,'#D7EFE5',-3,110,65)}{bubble(175,145,330,'做了这么多，用户变好了吗？',accent)}{path('M450 505 h450',ink,8)}'''
    if scene == 'bridge':
        return f'''{ground}{person(230,520,alt,1,'neutral','.85')}<path d="M350 500 Q585 340 820 500" stroke="{ink}" stroke-width="14" fill="none" stroke-dasharray="22 13" class="sketch"/><path d="M420 510 Q585 650 750 510" fill="{soft}" opacity=".55"/><circle cx="585" cy="470" r="55" fill="#fff" stroke="{accent}" stroke-width="4" class="sketch"/>{txt(585,462,'切换', 'sticky','middle')}{txt(585,490,'成本', 'sticky','middle')}{person(935,520,accent,-1,'smile','.85')}{sticky(125,205,a,soft,-5)}{sticky(505,175,b,'#FFE4A8',3)}{sticky(905,205,c,'#D7EFE5',5)}{arrow(325,300,845,300,accent)}'''
    if scene == 'stairs':
        return f'''{ground}<path d="M280 520 h210 v-105 h200 v-105 h215 v210" fill="{soft}" stroke="{ink}" stroke-width="4" class="sketch"/>{txt(385,478,a,'sticky','middle')}{txt(590,375,b,'sticky','middle')}{txt(797,270,c,'sticky','middle')}{person(350,405,accent,1,'smile','.72')}<path d="M465 392 q32 -65 66 -12" stroke="{accent}" stroke-width="4" fill="none"/><path d="M522 369 l12 14 l-18 8" stroke="{accent}" stroke-width="4" fill="none"/>{bubble(760,130,250,'一步一步，价值才站得稳',accent,True)}'''
    if scene in ('interview','observe','support'):
        left_prop='paper' if scene!='observe' else 'pen'
        return f'''{ground}{person(285,530,accent,1,'smile','.9',left_prop)}{person(875,530,alt,-1,'neutral','.9','paper')}<rect x="420" y="425" width="315" height="92" rx="10" fill="#fff" stroke="{ink}" stroke-width="4" class="sketch"/>{sticky(445,332,a,soft,-5,120,72)}{sticky(575,315,b,'#FFE4A8',3,145,78)}{sticky(710,365,c,'#D7EFE5',5,130,72)}{bubble(170,150,320,'别告诉我你想要什么，先演示现在怎么做',accent)}'''
    if scene == 'cycle':
        return f'''{ground}<circle cx="610" cy="345" r="165" fill="{soft}" opacity=".55" stroke="{ink}" stroke-width="4" stroke-dasharray="14 10" class="sketch"/>{sticky(535,150,a,'#fff',-3)}{sticky(775,300,b,'#fff',4)}{sticky(455,440,c,'#fff',3)}{arrow(690,190,790,300,accent)}{arrow(760,400,560,495,accent)}{arrow(460,410,500,225,accent)}{person(230,530,accent,1,'smile','.78','paper')}{bubble(120,175,270,'数据不是终点，是下一圈的起点',accent)}'''
    if scene == 'storm':
        knots=''.join(path(f'M{420+i*36} {260+(i%2)*40} q80 {-95+i*8} 150 10 q-60 100 -140 35',accent if i%2==0 else alt,4) for i in range(5))
        return f'''{ground}{person(260,530,accent,1,'neutral','.9','paper')}{knots}{sticky(785,205,a,soft,4)}{sticky(845,330,b,'#FFE4A8',-5)}{sticky(765,445,c,'#D7EFE5',3)}{bubble(140,135,315,'先找线头，再动手画原型',accent)}'''
    if scene == 'fork':
        return f'''{ground}{person(300,530,accent,1,'neutral','.88','paper')}<path d="M390 490 Q560 450 610 300 M610 300 Q730 190 920 205 M610 300 Q760 330 930 360 M610 300 Q720 470 900 500" stroke="{ink}" stroke-width="8" fill="none" class="sketch"/>{sticky(810,145,a,soft,-3)}{sticky(850,300,b,'#FFE4A8',4)}{sticky(810,445,c,'#D7EFE5',-4)}{bubble(150,145,300,'问题只有一个，解法可以有很多',accent)}'''
    if scene == 'dashboard':
        return f'''{ground}{person(250,530,accent,1,'smile','.8','pen')}<rect x="410" y="190" width="540" height="300" rx="18" fill="#fff" stroke="{ink}" stroke-width="4" class="sketch"/><path d="M470 430 v-70 h65 v70 m35 0 v-125 h65 v125 m35 0 v-190 h65 v190" stroke="{accent}" stroke-width="16"/><path d="M465 270 q110 65 220 -5 t205 -20" stroke="{alt}" stroke-width="5" fill="none"/>{txt(505,465,a,'sticky','middle')}{txt(605,465,b,'sticky','middle')}{txt(760,465,c,'sticky','middle')}{bubble(120,150,300,'上线前，先说清哪里算赢',accent)}'''
    if scene == 'review':
        return f'''{ground}<rect x="250" y="400" width="700" height="110" rx="18" fill="#fff" stroke="{ink}" stroke-width="5" class="sketch"/>{person(285,445,accent,1,'smile','.7','paper')}{person(895,445,alt,-1,'neutral','.7','paper')}{sticky(430,260,a,soft,-4)}{sticky(595,245,b,'#FFE4A8',4)}{sticky(760,270,c,'#D7EFE5',-3)}{bubble(405,135,390,'把晴天和下雨天都讲清楚',accent)}'''
    if scene == 'books':
        books=''.join(f'<rect x="{430+i*75}" y="{410-i%2*22}" width="62" height="{105+i%2*22}" rx="5" fill="{[soft,"#FFE4A8","#D7EFE5"][i%3]}" stroke="{ink}" stroke-width="4" transform="rotate({-5+i*3} {460+i*75} 470)" class="sketch"/>' for i in range(5))
        return f'''{ground}{person(260,530,accent,1,'smile','.9','book')}{books}{sticky(450,205,a,soft,-4)}{sticky(655,170,b,'#FFE4A8',3)}{sticky(830,235,c,'#D7EFE5',-3)}{bubble(120,145,300,'原来那些坑，书里早就写过',accent)}'''
    if scene == 'roundtable':
        return f'''{ground}<ellipse cx="610" cy="420" rx="290" ry="105" fill="#fff" stroke="{ink}" stroke-width="5" class="sketch"/>{person(360,500,accent,1,'smile','.65','paper')}{person(860,500,alt,-1,'smile','.65','book')}{sticky(475,315,a,soft,-4)}{sticky(600,290,b,'#FFE4A8',3)}{sticky(725,325,c,'#D7EFE5',-3)}{bubble(370,145,480,'理性的尺子，也要量得到人的情绪',accent)}'''
    if scene == 'flags':
        return f'''{ground}<path d="M250 520 Q500 160 930 195" stroke="{ink}" stroke-width="7" fill="none" stroke-dasharray="15 12"/><path d="M900 120 v130 m0 -125 l140 45 l-140 45" fill="{accent}" stroke="{ink}" stroke-width="4" class="sketch"/>{person(300,500,accent,1,'smile','.65')}{person(510,390,alt,1,'smile','.62')}{person(720,275,accent,1,'smile','.58')}{sticky(170,205,a,soft,-5)}{sticky(460,145,b,'#FFE4A8',3)}{sticky(750,355,c,'#D7EFE5',-3)}'''
    if scene == 'stepping':
        return f'''{ground}<path d="M180 500 Q600 610 1030 500" fill="#CDE7F0" opacity=".7"/><ellipse cx="400" cy="450" rx="95" ry="40" fill="{soft}" stroke="{ink}" stroke-width="4"/><ellipse cx="610" cy="365" rx="95" ry="40" fill="#FFE4A8" stroke="{ink}" stroke-width="4"/><ellipse cx="820" cy="280" rx="95" ry="40" fill="#D7EFE5" stroke="{ink}" stroke-width="4"/>{txt(400,458,a,'sticky','middle')}{txt(610,373,b,'sticky','middle')}{txt(820,288,c,'sticky','middle')}{person(300,420,accent,1,'smile','.62','book')}{arrow(450,400,770,260,accent)}'''
    if scene == 'checklist':
        return f'''{ground}{person(270,530,accent,1,'smile','.85','pen')}<rect x="430" y="165" width="465" height="335" rx="14" fill="#fff" stroke="{ink}" stroke-width="4" class="sketch"/>{sticky(475,210,a,soft,-3,330,65)}{sticky(500,305,b,'#FFE4A8',2,330,65)}{sticky(470,400,c,'#D7EFE5',-2,330,65)}<path d="M455 244 l12 13 l25 -30 M480 340 l12 13 l25 -30 M450 435 l12 13 l25 -30" stroke="{accent}" stroke-width="5" fill="none"/>{bubble(130,145,280,'合上书，真正的阅读才开始',accent)}'''
    if scene == 'clutter':
        buttons=''.join(f'<rect x="{450+(i%4)*115}" y="{220+(i//4)*90}" width="90" height="58" rx="10" fill="{[soft,"#FFE4A8","#D7EFE5"][i%3]}" stroke="{ink}" stroke-width="3" transform="rotate({(-4+i)%7-3} {495+(i%4)*115} {249+(i//4)*90})"/>' for i in range(12))
        return f'''{ground}{person(260,530,accent,1,'neutral','.9','paper')}<rect x="420" y="175" width="520" height="330" rx="25" fill="#fff" stroke="{ink}" stroke-width="5" class="sketch"/>{buttons}{bubble(120,145,290,'入口这么多，我该点哪一个？',accent)}{sticky(845,420,c,'#fff',5,150,65)}'''
    if scene == 'baggage':
        bags=''.join(f'<rect x="{430+i*95}" y="{420-(i%2)*45}" width="80" height="70" rx="10" fill="{[soft,"#FFE4A8","#D7EFE5"][i%3]}" stroke="{ink}" stroke-width="4" class="sketch"/>' for i in range(5))
        return f'''{ground}{person(300,530,accent,1,'neutral','.85')}{bags}<path d="M380 480 h520" stroke="{ink}" stroke-width="6"/>{sticky(430,260,a,soft,-4)}{sticky(620,220,b,'#FFE4A8',3)}{sticky(805,280,c,'#D7EFE5',-2)}{bubble(135,145,300,'每加一件，产品都要多背一段路',accent)}'''
    if scene == 'cleanup':
        return f'''{ground}{person(250,530,accent,1,'smile','.82','paper')}{person(940,530,alt,-1,'smile','.82')}<rect x="390" y="395" width="430" height="110" rx="15" fill="#fff" stroke="{ink}" stroke-width="4"/>{sticky(410,275,a,soft,-5)}{sticky(555,240,b,'#FFE4A8',3)}{sticky(700,285,c,'#D7EFE5',-3)}<path d="M430 440 l45 35 l55 -70 M575 440 q30 40 60 0 M725 420 l50 55" stroke="{accent}" stroke-width="5" fill="none"/>{bubble(375,135,430,'不是看见数据低就砍，要先问为什么',accent)}'''
    if scene == 'seesaw':
        return f'''{ground}<path d="M300 440 L900 350" stroke="{ink}" stroke-width="12"/><path d="M600 400 l-70 130 h140z" fill="{soft}" stroke="{ink}" stroke-width="4"/>{sticky(285,320,a,soft,-6,170,80)}{sticky(750,255,b,'#FFE4A8',4,170,80)}{sticky(510,160,c,'#D7EFE5',-2,180,80)}{person(245,515,accent,1,'smile','.65')}{person(940,440,alt,-1,'neutral','.65')}{bubble(390,105,420,'新增不是免费，它会挤占旧的空间',accent)}'''
    if scene == 'door':
        return f'''{ground}{person(270,530,accent,1,'smile','.85')}<rect x="500" y="175" width="300" height="340" rx="12" fill="#fff" stroke="{ink}" stroke-width="5" class="sketch"/><rect x="555" y="235" width="190" height="95" rx="18" fill="{accent}"/><circle cx="710" cy="440" r="12" fill="{ink}"/>{txt(650,292,'核心功能','bubble','middle')}{sticky(390,205,a,soft,-5)}{sticky(780,300,b,'#FFE4A8',4)}{sticky(390,430,c,'#D7EFE5',-3)}{bubble(130,135,290,'清空之后，重要的终于被看见',accent)}'''
    if scene == 'robot':
        return f'''{ground}{person(300,530,accent,1,'smile','.9','paper')}{robot(780,530,alt)}{bubble(135,145,300,'你先整理，我来判断',accent)}{bubble(720,125,280,'收到！但请记得核对我',alt,True)}{sticky(435,365,a,soft,-4)}{sticky(545,300,b,'#FFE4A8',3)}{sticky(655,390,c,'#D7EFE5',-3)}'''
    if scene == 'piles':
        piles=''.join(f'<rect x="{380+i*125}" y="{460-(i%3)*45}" width="105" height="{55+(i%3)*45}" fill="{[soft,"#FFE4A8","#D7EFE5"][i%3]}" stroke="{ink}" stroke-width="4" class="sketch"/>' for i in range(4))
        return f'''{ground}{robot(270,530,alt)}{piles}{person(935,530,accent,-1,'smile','.8','paper')}{txt(435,445,a,'sticky','middle')}{txt(575,400,b,'sticky','middle')}{txt(700,355,c,'sticky','middle')}{bubble(735,130,300,'脏活搬走后，我终于能抬头想方向',accent,True)}'''
    if scene == 'redpen':
        return f'''{ground}{robot(270,530,alt)}<rect x="410" y="180" width="390" height="320" rx="12" fill="#fff" stroke="{ink}" stroke-width="4" class="sketch"/><path d="M455 245 h260 M455 310 h220 M455 375 h270 M455 440 h180" stroke="{soft}" stroke-width="12"/><path d="M720 230 l28 26 l50 -65 M680 355 l28 26 l50 -65" stroke="{accent}" stroke-width="6" fill="none"/>{person(945,530,accent,-1,'smile','.82','pen')}{sticky(430,125,a,soft,-3)}{sticky(620,115,b,'#FFE4A8',2)}{sticky(790,210,c,'#D7EFE5',4)}'''
    if scene == 'boundary':
        return f'''{ground}<path d="M590 150 C540 250 650 360 590 530" stroke="{accent}" stroke-width="5" stroke-dasharray="12 10"/><text x="590" y="120" class="tiny" text-anchor="middle">边界线</text>{robot(330,530,alt)}{person(850,530,accent,-1,'neutral','.9','paper')}{sticky(170,250,'效率',soft,-4)}{sticky(675,190,a,'#FFE4A8',3)}{sticky(820,290,b,'#D7EFE5',-3)}{sticky(690,415,c,'#fff',4)}{bubble(135,130,300,'我可以建议，但不能替你负责',alt)}'''
    if scene == 'lock':
        return f'''{ground}{robot(270,530,alt)}<rect x="465" y="300" width="300" height="205" rx="22" fill="{soft}" stroke="{ink}" stroke-width="5" class="sketch"/><path d="M535 305 v-65 q0 -90 80 -90 q80 0 80 90 v65" stroke="{ink}" stroke-width="16" fill="none"/><circle cx="615" cy="390" r="25" fill="{accent}"/><path d="M615 415 v38" stroke="{accent}" stroke-width="12"/>{person(945,530,accent,-1,'smile','.78','paper')}{sticky(400,155,a,soft,-4)}{sticky(705,145,b,'#FFE4A8',3)}{sticky(800,300,c,'#D7EFE5',-2)}'''
    if scene == 'baton':
        return f'''{ground}{person(300,530,alt,1,'smile','.9')}<path d="M395 330 l210 85" stroke="{accent}" stroke-width="18"/><path d="M390 325 l35 -20 m165 105 l35 -20" stroke="{ink}" stroke-width="6"/>{person(860,530,accent,-1,'neutral','.9','paper')}{sticky(180,205,a,soft,-5)}{sticky(500,175,b,'#FFE4A8',3)}{sticky(840,235,c,'#D7EFE5',-3)}{bubble(650,120,320,'接住的不只是任务，还有结果',accent,True)}'''
    if scene == 'questions':
        return f'''{ground}{person(260,530,accent,1,'neutral','.85','paper')}<rect x="420" y="395" width="430" height="110" rx="14" fill="#fff" stroke="{ink}" stroke-width="4"/>{person(930,530,alt,-1,'neutral','.75','pen')}{bubble(380,130,230,a,accent)}{bubble(620,205,230,b,alt,True)}{bubble(430,290,250,c,accent)}{txt(635,450,'订单备注功能','sticky','middle')}<text x="775" y="470" class="bigq">?</text>'''
    if scene == 'launch':
        return f'''{ground}{person(250,530,accent,1,'neutral','.8','paper')}<rect x="405" y="180" width="540" height="320" rx="18" fill="#202A35" stroke="{ink}" stroke-width="5" class="sketch"/><path d="M455 405 q80 -120 160 -20 t170 -95 t110 50" stroke="#7FE0C0" stroke-width="5" fill="none"/><rect x="465" y="250" width="80" height="80" fill="{accent}"/><rect x="570" y="220" width="80" height="110" fill="#FFE4A8"/><rect x="675" y="270" width="80" height="60" fill="{alt}"/>{txt(505,455,a,'tiny','middle')}{txt(610,455,b,'tiny','middle')}{txt(715,455,c,'tiny','middle')}{bubble(120,135,300,'上线不是结束，数据才刚开口',accent)}'''
    if scene == 'retro':
        return f'''{ground}<path d="M280 520 h200 v-100 h190 v-100 h190 v-100 h170" fill="none" stroke="{ink}" stroke-width="8" class="sketch"/>{person(340,410,accent,1,'smile','.63','paper')}{person(545,315,alt,1,'smile','.6')}{person(735,215,accent,1,'smile','.58')}{sticky(260,255,a,soft,-5)}{sticky(490,180,b,'#FFE4A8',3)}{sticky(760,115,c,'#D7EFE5',-3)}{bubble(170,125,300,'每个坑，都能垫成下一步',accent)}'''
    return f'''{ground}{person(300,530,accent,1,'smile','.9','paper')}{person(900,530,alt,-1,'smile','.9')}{sticky(420,230,a,soft,-4)}{sticky(610,200,b,'#FFE4A8',3)}{sticky(780,300,c,'#D7EFE5',-3)}'''


def svg(article_no, visual_no, title, subtitle, scene, beats):
    accent, bg, soft, alt, ink = PALETTES[article_no - 1]
    scene_content = scene_svg(scene, beats, accent, soft, alt, ink)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle)}</desc>
  <defs>
    <filter id="rough"><feTurbulence type="fractalNoise" baseFrequency="0.015" numOctaves="2" seed="{visual_no}" result="noise"/><feDisplacementMap in="SourceGraphic" in2="noise" scale="1.6"/></filter>
    <pattern id="grain" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="4" cy="7" r="1" fill="{ink}" opacity=".12"/><circle cx="20" cy="18" r=".8" fill="{accent}" opacity=".12"/><path d="M10 24 l3 -1" stroke="{ink}" stroke-width=".7" opacity=".1"/></pattern>
  </defs>
  <style>
    .sketch{{filter:url(#rough)}}
    .kicker{{font:700 16px -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;letter-spacing:3px}}
    .title{{font:700 42px "Kaiti SC",STKaiti,"KaiTi","PingFang SC",sans-serif}}
    .subtitle{{font:400 19px "Kaiti SC",STKaiti,"KaiTi","PingFang SC",sans-serif}}
    .note{{font:500 20px "Kaiti SC",STKaiti,"KaiTi","PingFang SC",sans-serif;fill:{ink}}}
    .sticky{{font:700 18px "Kaiti SC",STKaiti,"KaiTi","PingFang SC",sans-serif;fill:{ink}}}
    .bubble{{font:600 18px "Kaiti SC",STKaiti,"KaiTi","PingFang SC",sans-serif;fill:{ink}}}
    .tiny{{font:600 15px "Kaiti SC",STKaiti,"KaiTi","PingFang SC",sans-serif;fill:#fff}}
    .face{{font:700 18px "Kaiti SC",STKaiti,"KaiTi",sans-serif;fill:{ink}}}
    .bigq{{font:800 82px "Kaiti SC",STKaiti,"KaiTi",sans-serif;fill:{accent}}}
  </style>
  <rect width="1200" height="675" rx="28" fill="{bg}"/>
  <g opacity=".5"><path d="M30 115 Q260 90 500 112 T1170 100" stroke="{soft}" stroke-width="3" fill="none"/><path d="M45 585 Q350 610 650 585 T1160 595" stroke="{soft}" stroke-width="3" fill="none"/></g>
  <path d="M24 30 Q310 20 590 28 T1174 25 L1180 640 Q910 654 610 646 T25 650Z" fill="none" stroke="{ink}" stroke-width="3" stroke-dasharray="9 7" opacity=".45" class="sketch"/>
  <text x="68" y="70" class="kicker" fill="{accent}">小何的产品手记  ·  {article_no:02d}/{visual_no:02d}</text>
  <text x="68" y="123" class="title" fill="{ink}">{escape(title)}</text>
  <text x="68" y="156" class="subtitle" fill="{ink}" opacity=".72">{escape(subtitle)}</text>
  <g transform="translate(0 32)">{scene_content}</g>
  <text x="1120" y="625" text-anchor="end" class="subtitle" fill="{accent}">日拱一卒 · 功不唐捐</text>
  <rect width="1200" height="675" rx="28" fill="url(#grain)" pointer-events="none"/>
</svg>'''


for a_idx, visuals in enumerate(DATA, 1):
    for v_idx, item in enumerate(visuals, 1):
        (OUT / f"article-{a_idx}-{v_idx}.svg").write_text(svg(a_idx, v_idx, *item), encoding="utf-8")
print(f"Generated {sum(map(len, DATA))} hand-drawn story illustrations in {OUT}")
