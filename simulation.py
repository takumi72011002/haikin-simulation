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
    height="100%"
    viewBox="-150 -500 1500 2200"
    preserveAspectRatio="xMidYMid meet"
    style="max-width:100%; max-height:100%;"
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

TIE_LEFT = 85 - TIE_BAR_D * 1.5 - TIE_BAR_D * 0.5
TIE_RIGHT = COLUMN_WIDTH - (85 - TIE_BAR_D * 1.5 - TIE_BAR_D * 0.5)

TIE_TOP = 85 - TIE_BAR_D * 0.5 - COLUMN_BAR_D*0.5
TIE_BOTTOM = COLUMN_HEIGHT - (85 - TIE_BAR_D * 0.5 - COLUMN_BAR_D*0.5)

# 帯筋の角の曲げ半径
TIE_RADIUS = TIE_BAR_D * 1.5 + TIE_BAR_D*0.5

svg += f"""
<rect
    x="{TIE_LEFT}"
    y="{TIE_TOP}"
    width="{TIE_RIGHT - TIE_LEFT}"
    height="{TIE_BOTTOM - TIE_TOP}"
    fill="none"
    stroke="#333333"
    stroke-width="{TIE_BAR_D}"
    rx="{TIE_RADIUS}"
    ry="{TIE_RADIUS}"
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
# SVG終了
# ==========================================================

svg += """
</svg>
"""


# ==========================================================
# Streamlitに表示
# ==========================================================

components.html(
    f"""
    <div style="
        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    ">
        {svg}
    </div>
    """,
    height=800,
    scrolling=False
)