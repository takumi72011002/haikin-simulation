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

# ----------------------------------------------------------
# 柱
# ----------------------------------------------------------

COLUMN_WIDTH = 1200          # 柱幅(mm)
COLUMN_HEIGHT = 1200         # 柱せい(mm)

COLUMN_BAR_D = 38            # 柱筋 D
TIE_BAR_D = 13               # 帯筋 D
COLUMN_BAR_NUM = 8           # 柱筋本数


# 柱筋のX座標(mm)
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


# ----------------------------------------------------------
# 梁
# ----------------------------------------------------------

BEAM_WIDTH = 750             # 梁幅(mm)
BEAM_BAR_D = 19              # 梁筋 D
STIRRUP_D = 13               # あばら筋 D
BEAM_BAR_NUM = 7             # 梁筋本数


# 梁筋のX座標(mm)
BEAM_BARS = [
    259,
    351,
    453,
    554,
    644,
    744,
    842
]


# ----------------------------------------------------------
# 梁の長さ
# ----------------------------------------------------------

BEAM_LENGTH_TOP = 400
BEAM_LENGTH_BOTTOM = 400


# ==========================================================
# 座標計算
# ==========================================================

# 梁は柱の中央に配置
BEAM_LEFT = (COLUMN_WIDTH - BEAM_WIDTH) / 2
BEAM_RIGHT = BEAM_LEFT + BEAM_WIDTH


# 柱の上下位置
COLUMN_TOP = 0
COLUMN_BOTTOM = COLUMN_HEIGHT


# 梁の上下端
TOP_BEAM_TOP = -BEAM_LENGTH_TOP
TOP_BEAM_BOTTOM = 0

BOTTOM_BEAM_TOP = COLUMN_HEIGHT
BOTTOM_BEAM_BOTTOM = COLUMN_HEIGHT + BEAM_LENGTH_BOTTOM


# ==========================================================
# SVG開始
# ==========================================================

svg = f"""
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="100%"
    viewBox="-180 -620 1560 2450"
>


<!-- ======================================================
     コンクリート
     中央：1200×1200の柱
     上下：梁幅750
     ====================================================== -->

<path
    d="
        M {BEAM_LEFT} {TOP_BEAM_TOP}

        H {BEAM_RIGHT}
        V {COLUMN_TOP}

        H {COLUMN_WIDTH}
        V {COLUMN_BOTTOM}

        H {BEAM_RIGHT}
        V {BOTTOM_BEAM_BOTTOM}

        H {BEAM_LEFT}
        V {COLUMN_BOTTOM}

        H 0
        V {COLUMN_TOP}

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
# 柱の内部に矩形の帯筋を描く
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
    y1="{TIE_TOP + 40}"
    x2="{TIE_LEFT + 65}"
    y2="{TIE_TOP + 95}"
    stroke="#333333"
    stroke-width="{TIE_BAR_D}"
    stroke-linecap="round"
/>
"""


# ==========================================================
# 柱筋
# ==========================================================
#
# 柱筋はD38なので、円の直径を38として表示
#
# 上下の横方向に配置
#
# ==========================================================

COLUMN_BAR_RADIUS = COLUMN_BAR_D / 2

for x in COLUMN_BARS:

    # 上側
    svg += f"""
    <circle
        cx="{x}"
        cy="{TIE_TOP}"
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
        cy="{TIE_BOTTOM}"
        r="{COLUMN_BAR_RADIUS}"
        fill="#666666"
        stroke="black"
        stroke-width="1"
    />
    """


# ==========================================================
# 梁筋
# ==========================================================
#
# 梁筋は長方形
#
# 上梁と下梁に配置
#
# ==========================================================

for x in BEAM_BARS:

    # ------------------------------
    # 上梁
    # ------------------------------

    svg += f"""
    <rect
        x="{x - BEAM_BAR_D / 2}"
        y="{TOP_BEAM_TOP}"
        width="{BEAM_BAR_D}"
        height="{BEAM_LENGTH_TOP}"
        fill="#222222"
    />
    """


    # ------------------------------
    # 下梁
    # ------------------------------

    svg += f"""
    <rect
        x="{x - BEAM_BAR_D / 2}"
        y="{BOTTOM_BEAM_TOP}"
        width="{BEAM_BAR_D}"
        height="{BEAM_LENGTH_BOTTOM}"
        fill="#222222"
    />
    """


# ==========================================================
# 上側：柱幅寸法
# ==========================================================

COLUMN_DIM_Y = -520

svg += f"""
<!-- 柱幅寸法線 -->

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
    y2="-450"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{COLUMN_WIDTH}"
    y1="{COLUMN_DIM_Y}"
    x2="{COLUMN_WIDTH}"
    y2="-450"
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
# 上側：柱筋の寸法チェーン
# ==========================================================

COLUMN_CHAIN_Y = -450

previous = 0

for x in COLUMN_BARS:

    # 寸法線の縦線
    svg += f"""
    <line
        x1="{x}"
        y1="{COLUMN_CHAIN_Y}"
        x2="{x}"
        y2="-400"
        stroke="black"
        stroke-width="1"
    />
    """

    # 中央位置
    center = (previous + x) / 2

    # 寸法値
    distance = x - previous

    svg += f"""
    <text
        x="{center}"
        y="{COLUMN_CHAIN_Y - 15}"
        text-anchor="middle"
        font-size="16">
        {distance}
    </text>
    """

    previous = x


# 最後の区間
last_distance = COLUMN_WIDTH - COLUMN_BARS[-1]

svg += f"""
<line
    x1="{COLUMN_BARS[-1]}"
    y1="{COLUMN_CHAIN_Y}"
    x2="{COLUMN_BARS[-1]}"
    y2="-400"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{COLUMN_BARS[-1] + last_distance / 2}"
    y="{COLUMN_CHAIN_Y - 15}"
    text-anchor="middle"
    font-size="16">
    {last_distance}
</text>
"""


# ==========================================================
# 下側：梁筋寸法チェーン
# ==========================================================

BEAM_CHAIN_Y = BOTTOM_BEAM_BOTTOM + 60

previous = BEAM_LEFT

for x in BEAM_BARS:

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

    center = (previous + x) / 2
    distance = x - previous

    svg += f"""
    <text
        x="{center}"
        y="{BEAM_CHAIN_Y + 25}"
        text-anchor="middle"
        font-size="16">
        {distance:.0f}
    </text>
    """

    previous = x


# 最後の区間
last_distance = BEAM_RIGHT - BEAM_BARS[-1]

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
    x="{BEAM_BARS[-1] + last_distance / 2}"
    y="{BEAM_CHAIN_Y + 25}"
    text-anchor="middle"
    font-size="16">
    {last_distance:.0f}
</text>
"""


# ==========================================================
# 下側：梁幅寸法
# ==========================================================

BEAM_DIM_Y = BEAM_CHAIN_Y + 70

svg += f"""
<!-- 梁幅寸法線 -->

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
    y="{BEAM_DIM_Y + 30}"
    text-anchor="middle"
    font-size="20">
    {BEAM_WIDTH}
</text>


</svg>
"""


# ==========================================================
# Streamlitに表示
# ==========================================================

components.html(
    svg,
    height=1300,
    scrolling=False
)