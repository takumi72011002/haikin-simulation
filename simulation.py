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

COLUMN_BARS = [85,226,384,522,677,874,995,1115]

# ------------------------------
# 梁
# ------------------------------

BEAM_WIDTH = 750

BEAM_BAR_D = 19
STIRRUP_D = 13

BEAM_BARS = [259,351,453,554,644,744,842]


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
# 梁と柱の境界線をグレーで消す
# ==========================================================

svg += f"""
<line
    x1="{BEAM_LEFT}"
    y1="{TOP_BEAM_TOP}"
    x2="{BEAM_RIGHT}"
    y2="{TOP_BEAM_TOP}"
    stroke="#eeeeee"
    stroke-width="8"
/>

<line
    x1="{BEAM_LEFT}"
    y1="{BOTTOM_BEAM_BOTTOM}"
    x2="{BEAM_RIGHT}"
    y2="{BOTTOM_BEAM_BOTTOM}"
    stroke="#eeeeee"
    stroke-width="8"
/>
"""


# ==========================================================
# 帯筋
# ==========================================================
#
# 正方形の柱の中に配置
#
# ==========================================================

TIE_LEFT = (85 + {COLUMN_BAR_D}*0.5)
TIE_RIGHT = COLUMN_WIDTH - (85 + {COLUMN_BAR_D}*0.5)

TIE_TOP = (85 + {COLUMN_BAR_D}*0.5)
TIE_BOTTOM = COLUMN_HEIGHT -(85 + {COLUMN_BAR_D}*0.5)

svg += f"""
<rect
    x="{TIE_LEFT}"
    y="{TIE_TOP}"
    width="{TIE_RIGHT - TIE_LEFT}"
    height="{TIE_BOTTOM - TIE_TOP}"
    fill="none"
    stroke="#333333"
    stroke-width="{TIE_BAR_D}"
    rx="{TIE_BAR_D}*1.5+{TIE_BAR_D}*0.5"
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
# 上側：柱幅寸法
# ==========================================================

# 柱幅の寸法線位置
COLUMN_WIDTH_DIM_Y = -410

# 柱筋寸法線位置
COLUMN_CHAIN_Y = -340


# ----------------------------------------------------------
# 柱幅 1200 の寸法線
# ----------------------------------------------------------

svg += f"""
<!-- 柱幅寸法線 -->
<line
    x1="0"
    y1="{COLUMN_WIDTH_DIM_Y}"
    x2="{COLUMN_WIDTH}"
    y2="{COLUMN_WIDTH_DIM_Y}"
    stroke="black"
    stroke-width="1"
/>

<!-- 左端 -->
<line
    x1="0"
    y1="{COLUMN_WIDTH_DIM_Y}"
    x2="0"
    y2="{COLUMN_WIDTH_DIM_Y + 40}"
    stroke="black"
    stroke-width="1"
/>

<!-- 右端 -->
<line
    x1="{COLUMN_WIDTH}"
    y1="{COLUMN_WIDTH_DIM_Y}"
    x2="{COLUMN_WIDTH}"
    y2="{COLUMN_WIDTH_DIM_Y + 40}"
    stroke="black"
    stroke-width="1"
/>

<!-- 1200 -->
<text
    x="{COLUMN_WIDTH / 2}"
    y="{COLUMN_WIDTH_DIM_Y - 15}"
    text-anchor="middle"
    font-size="20">
    {COLUMN_WIDTH}
</text>
"""


# ==========================================================
# 上側：柱筋の寸法チェーン
# ==========================================================

# 柱左端を基準にする
previous = 0


# ----------------------------------------------------------
# 柱左端
# ----------------------------------------------------------

svg += f"""
<line
    x1="0"
    y1="{COLUMN_CHAIN_Y}"
    x2="0"
    y2="{COLUMN_CHAIN_Y + 40}"
    stroke="black"
    stroke-width="1"
/>
"""


# ----------------------------------------------------------
# 柱筋
# ----------------------------------------------------------

for x in COLUMN_BARS:

    # 前の位置から現在の位置まで
    distance = x - previous

    # 寸法文字の中央
    center = (previous + x) / 2

    # 鉄筋位置の縦線
    svg += f"""
    <line
        x1="{x}"
        y1="{COLUMN_CHAIN_Y}"
        x2="{x}"
        y2="{COLUMN_CHAIN_Y + 40}"
        stroke="black"
        stroke-width="1"
    />
    """

    # 寸法値
    svg += f"""
    <text
        x="{center}"
        y="{COLUMN_CHAIN_Y - 10}"
        text-anchor="middle"
        font-size="15">
        {distance}
    </text>
    """

    previous = x


# ----------------------------------------------------------
# 柱右端まで
# ----------------------------------------------------------

last = COLUMN_WIDTH - COLUMN_BARS[-1]

center = (COLUMN_BARS[-1] + COLUMN_WIDTH) / 2


# 右端の縦線
svg += f"""
<line
    x1="{COLUMN_WIDTH}"
    y1="{COLUMN_CHAIN_Y}"
    x2="{COLUMN_WIDTH}"
    y2="{COLUMN_CHAIN_Y + 40}"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{center}"
    y="{COLUMN_CHAIN_Y - 10}"
    text-anchor="middle"
    font-size="15">
    {last}
</text>
"""


# ==========================================================
# 下側：梁筋の寸法チェーン
# ==========================================================

# 梁筋寸法線の位置
BEAM_CHAIN_Y = BOTTOM_BEAM_BOTTOM + 70


# ----------------------------------------------------------
# 梁左端からスタート
# ----------------------------------------------------------

previous = BEAM_LEFT


# 梁左端の縦線
svg += f"""
<line
    x1="{BEAM_LEFT}"
    y1="{BOTTOM_BEAM_BOTTOM}"
    x2="{BEAM_LEFT}"
    y2="{BEAM_CHAIN_Y}"
    stroke="black"
    stroke-width="1"
/>
"""


# ----------------------------------------------------------
# 梁筋ごとの寸法
# ----------------------------------------------------------

for x in BEAM_BARS:

    # 前の位置から現在の鉄筋まで
    distance = x - previous

    # 寸法文字の中央
    center = (previous + x) / 2

    # 鉄筋位置の縦線
    svg += f"""
    <line
        x1="{x}"
        y1="{BOTTOM_BEAM_BOTTOM}"
        x2="{x}"
        y2="{BEAM_CHAIN_Y}"
        stroke="black"
        stroke-width="1"
    />
    """

    # 寸法値
    svg += f"""
    <text
        x="{center}"
        y="{BEAM_CHAIN_Y + 22}"
        text-anchor="middle"
        font-size="15">
        {distance}
    </text>
    """

    previous = x


# ----------------------------------------------------------
# 梁右端まで
# ----------------------------------------------------------

last = BEAM_RIGHT - BEAM_BARS[-1]

center = (BEAM_BARS[-1] + BEAM_RIGHT) / 2


# 梁右端の縦線
svg += f"""
<line
    x1="{BEAM_RIGHT}"
    y1="{BOTTOM_BEAM_BOTTOM}"
    x2="{BEAM_RIGHT}"
    y2="{BEAM_CHAIN_Y}"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{center}"
    y="{BEAM_CHAIN_Y + 22}"
    text-anchor="middle"
    font-size="15">
    {last}
</text>
"""


# ==========================================================
# 下側：梁幅 750
# ==========================================================

BEAM_DIM_Y = BEAM_CHAIN_Y + 65


# ----------------------------------------------------------
# 梁幅の横線
# ----------------------------------------------------------

svg += f"""
<line
    x1="{BEAM_LEFT}"
    y1="{BEAM_DIM_Y}"
    x2="{BEAM_RIGHT}"
    y2="{BEAM_DIM_Y}"
    stroke="black"
    stroke-width="1"
/>
"""


# ----------------------------------------------------------
# 梁左端の縦線
# ----------------------------------------------------------

svg += f"""
<line
    x1="{BEAM_LEFT}"
    y1="{BEAM_CHAIN_Y}"
    x2="{BEAM_LEFT}"
    y2="{BEAM_DIM_Y}"
    stroke="black"
    stroke-width="1"
/>
"""


# ----------------------------------------------------------
# 梁右端の縦線
# ----------------------------------------------------------

svg += f"""
<line
    x1="{BEAM_RIGHT}"
    y1="{BEAM_CHAIN_Y}"
    x2="{BEAM_RIGHT}"
    y2="{BEAM_DIM_Y}"
    stroke="black"
    stroke-width="1"
/>
"""


# ----------------------------------------------------------
# 750
# ----------------------------------------------------------

svg += f"""
<text
    x="{(BEAM_LEFT + BEAM_RIGHT) / 2}"
    y="{BEAM_DIM_Y + 25}"
    text-anchor="middle"
    font-size="20">
    {BEAM_WIDTH}
</text>
"""


# ==========================================================
# SVG終了
# ==========================================================

svg += """
</svg>
"""


# ==========================================================
# Streamlitに表示
# ==========================================================

components.html(
    svg,
    height=1200,
    scrolling=False
)