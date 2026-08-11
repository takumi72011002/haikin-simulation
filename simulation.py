import streamlit as st
import streamlit.components.v1 as components


# ==========================================================
# ページ設定
# ==========================================================

st.set_page_config(
    page_title="配筋シミュレーション",
    page_icon="🌸",
    layout="centered"
)

st.title("配筋シミュレーション")


# ==========================================================
# 配筋条件
# ==========================================================

# ------------------------------
# 柱
# ------------------------------

COLUMN_WIDTH = 1200
COLUMN_HEIGHT = 1200

COLUMN_BAR_D = 38
TIE_BAR_D = 13

COLUMN_BARS = [
    85,
    226,
    384,
    522,
    677,
    874,
    995,
    1115
]


# ------------------------------
# 梁
# ------------------------------

BEAM_WIDTH = 750

BEAM_BAR_D = 19
STIRRUP_D = 13

BEAM_BARS = [
    259,
    351,
    453,
    554,
    644,
    744,
    842
]


# ==========================================================
# 梁の長さ
# ==========================================================
#
# ここを変更すれば上下方向の梁の長さを変更できる
#
# ==========================================================

BEAM_LENGTH_TOP = 250
BEAM_LENGTH_BOTTOM = 250


# ==========================================================
# 座標
# ==========================================================

# 梁幅750を柱1200の中央に配置

BEAM_LEFT = (COLUMN_WIDTH - BEAM_WIDTH) / 2-50
BEAM_RIGHT = BEAM_LEFT + BEAM_WIDTH


# 柱の上下端

COLUMN_TOP = 0
COLUMN_BOTTOM = COLUMN_HEIGHT


# 梁の範囲

TOP_BEAM_TOP = -BEAM_LENGTH_TOP
TOP_BEAM_BOTTOM = 0

BOTTOM_BEAM_TOP = COLUMN_HEIGHT
BOTTOM_BEAM_BOTTOM = COLUMN_HEIGHT + BEAM_LENGTH_BOTTOM


# ==========================================================
# 柱筋のY座標
# ==========================================================
#
# X方向と同じ85mmを採用
#
# ==========================================================

COLUMN_BAR_Y_TOP = 85
COLUMN_BAR_Y_BOTTOM = COLUMN_HEIGHT - 85


# ==========================================================
# SVG
# ==========================================================

svg = f"""
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="100%"
    viewBox="-150 -500 1500 2200"
>


<!-- ======================================================
     コンクリート外形
     ====================================================== -->

<path
    d="
        M {BEAM_LEFT} {TOP_BEAM_TOP}

        H {BEAM_RIGHT}
        V 0

        H {COLUMN_WIDTH}
        V {COLUMN_HEIGHT}

        H {BEAM_RIGHT}
        V {BOTTOM_BEAM_BOTTOM}

        H {BEAM_LEFT}
        V {COLUMN_HEIGHT}

        H 0
        V 0

        H {BEAM_LEFT}
        Z
    "
    fill="#eeeeee"
    stroke="black"
    stroke-width="2"
/>
"""


# ==========================================================
# 帯筋
# ==========================================================
#
# 正方形の柱の中に配置
#
# ==========================================================

TIE_LEFT = 70
TIE_RIGHT = COLUMN_WIDTH - 70

TIE_TOP = 70
TIE_BOTTOM = COLUMN_HEIGHT - 70

svg += f"""
<rect
    x="{TIE_LEFT}"
    y="{TIE_TOP}"
    width="{TIE_RIGHT - TIE_LEFT}"
    height="{TIE_BOTTOM - TIE_TOP}"
    fill="none"
    stroke="#333333"
    stroke-width="{TIE_BAR_D}"
    rx="10"
/>
"""


# ==========================================================
# 帯筋フック
# ==========================================================

svg += f"""
<line
    x1="{TIE_LEFT}"
    y1="{TIE_TOP + 35}"
    x2="{TIE_LEFT + 65}"
    y2="{TIE_TOP + 90}"
    stroke="#333333"
    stroke-width="{TIE_BAR_D}"
    stroke-linecap="round"
/>
"""


# ==========================================================
# 梁筋
# ==========================================================
#
# ★重要
#
# 梁筋は
#
# 上梁
#   ↓
# 柱の中
#   ↓
# 下梁
#
# まで連続して描く
#
# ==========================================================

for x in BEAM_BARS:

    svg += f"""
    <rect
        x="{x - BEAM_BAR_D / 2}"
        y="{TOP_BEAM_TOP}"
        width="{BEAM_BAR_D}"
        height="{BOTTOM_BEAM_BOTTOM - TOP_BEAM_TOP}"
        fill="#222222"
    />
    """


# ==========================================================
# 柱筋
# ==========================================================
#
# ExcelのX座標をそのまま使用
#
# 上側：Y=85
# 下側：Y=1115
#
# ==========================================================

COLUMN_BAR_RADIUS = COLUMN_BAR_D / 2


for x in COLUMN_BARS:

    # 上側

    svg += f"""
    <circle
        cx="{x}"
        cy="{COLUMN_BAR_Y_TOP}"
        r="{COLUMN_BAR_RADIUS}"
        fill="#666666"
        stroke="black"
        stroke-width="1"
    />
    """


    # 下側

    svg += f"""
    <circle
        cx="{x}"
        cy="{COLUMN_BAR_Y_BOTTOM}"
        r="{COLUMN_BAR_RADIUS}"
        fill="#666666"
        stroke="black"
        stroke-width="1"
    />
    """

# ==========================================================
# 梁と柱の境界線をグレーで消す
# ==========================================================

svg += f"""
<line
    x1="{BEAM_LEFT}"
    y1="0"
    x2="{BEAM_RIGHT}"
    y2="0"
    stroke="#eeeeee"
    stroke-width="8"
/>

<line
    x1="{BEAM_LEFT}"
    y1="{COLUMN_HEIGHT}"
    x2="{BEAM_RIGHT}"
    y2="{COLUMN_HEIGHT}"
    stroke="#eeeeee"
    stroke-width="8"
/>
"""











# ==========================================================
# 上側：柱幅
# ==========================================================

COLUMN_DIM_Y = -410

svg += f"""
<line
    x1="0"
    y1="{COLUMN_DIM_Y}"
    x2="{COLUMN_WIDTH}"
    y2="{COLUMN_DIM_Y}"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="0"
    y1="{COLUMN_DIM_Y}"
    x2="0"
    y2="-340"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{COLUMN_WIDTH}"
    y1="{COLUMN_DIM_Y}"
    x2="{COLUMN_WIDTH}"
    y2="-340"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{COLUMN_WIDTH / 2}"
    y="{COLUMN_DIM_Y - 15}"
    text-anchor="middle"
    font-size="20">
    {COLUMN_WIDTH}
</text>
"""


# ==========================================================
# 上側：柱筋寸法
# ==========================================================

CHAIN_Y = -340

previous = 0

for x in COLUMN_BARS:

    distance = x - previous
    center = (previous + x) / 2

    svg += f"""
    <line
        x1="{x}"
        y1="{CHAIN_Y}"
        x2="{x}"
        y2="-300"
        stroke="black"
        stroke-width="1"
    />

    <text
        x="{center}"
        y="{CHAIN_Y - 12}"
        text-anchor="middle"
        font-size="15">
        {distance}
    </text>
    """

    previous = x


# 最後

last = COLUMN_WIDTH - COLUMN_BARS[-1]

svg += f"""
<line
    x1="{COLUMN_BARS[-1]}"
    y1="{CHAIN_Y}"
    x2="{COLUMN_BARS[-1]}"
    y2="-300"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{COLUMN_BARS[-1] + last / 2}"
    y="{CHAIN_Y - 12}"
    text-anchor="middle"
    font-size="15">
    {last}
</text>
"""


# ==========================================================
# 下側：梁筋寸法
# ==========================================================

BEAM_CHAIN_Y = BOTTOM_BEAM_BOTTOM + 70

previous = 0

for x in BEAM_BARS:

    distance = x - previous
    center = (previous + x) / 2

    svg += f"""
    <line
        x1="{x}"
        y1="{BOTTOM_BEAM_BOTTOM}"
        x2="{x}"
        y2="{BEAM_CHAIN_Y}"
        stroke="black"
        stroke-width="1"
    />

    <text
        x="{center}"
        y="{BEAM_CHAIN_Y + 20}"
        text-anchor="middle"
        font-size="15">
        {distance}
    </text>
    """

    previous = x


# 最後

last = COLUMN_WIDTH - BEAM_BARS[-1]

svg += f"""
<line
    x1="{BEAM_BARS[-1]}"
    y1="{BOTTOM_BEAM_BOTTOM}"
    x2="{BEAM_BARS[-1]}"
    y2="{BEAM_CHAIN_Y}"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{BEAM_BARS[-1] + last / 2}"
    y="{BEAM_CHAIN_Y + 20}"
    text-anchor="middle"
    font-size="15">
    {last}
</text>
"""


# ==========================================================
# 下側：梁幅
# ==========================================================

BEAM_DIM_Y = BEAM_CHAIN_Y + 60

svg += f"""
<line
    x1="{BEAM_LEFT}"
    y1="{BEAM_DIM_Y}"
    x2="{BEAM_RIGHT}"
    y2="{BEAM_DIM_Y}"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{BEAM_LEFT}"
    y1="{BOTTOM_BEAM_BOTTOM}"
    x2="{BEAM_LEFT}"
    y2="{BEAM_DIM_Y}"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{BEAM_RIGHT}"
    y1="{BOTTOM_BEAM_BOTTOM}"
    x2="{BEAM_RIGHT}"
    y2="{BEAM_DIM_Y}"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{(BEAM_LEFT + BEAM_RIGHT) / 2}"
    y="{BEAM_DIM_Y + 25}"
    text-anchor="middle"
    font-size="20">
    {BEAM_WIDTH}
</text>


</svg>
"""


# ==========================================================
# 表示
# ==========================================================

components.html(
    svg,
    height=1200,
    scrolling=False
)