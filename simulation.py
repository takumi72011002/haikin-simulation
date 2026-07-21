import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="配筋シミュレーション",
    page_icon="🌸",
)

st.title("配筋シミュレーション")

# ==========================================
# 配筋データ
# ==========================================

beam_bars = [180, 300, 390, 450, 510, 600, 720]
column_bars = [90, 240, 320, 390, 480, 560, 660, 770]

C=850
CL = 0
CR = CL+C

svg = f"""
<svg
xmlns="http://www.w3.org/2000/svg"
viewBox="-80 -120 1010 1300"
preserveAspectRatio="xMidYMid meet"
style="width:100%;height:auto;">

<defs>
<marker id="arrow"
markerWidth="8"
markerHeight="8"
refX="4"
refY="4"
orient="auto">
<path d="M0,0 L8,4 L0,8 Z" fill="black"/>
</marker>
</defs>
"""

# ==================================================
# 寸法線　柱幅
# ==================================================

svg += f"""
<line
x1="{CL}"
y1="-80"
x2="{CR}"
y2="-80"
stroke="black"
stroke-width="2"/>


<line
x1="{CL}"
y1="-80"
x2="{CL}"
y2="0"
stroke="black"
stroke-width="2"/>

<line
x1="{CR}"
y1="-80"
x2="{CR}"
y2="0"
stroke="black"
stroke-width="2"/>

<text
x="{(CL+CR)/2}"
y="-92"
text-anchor="middle"
font-size="22">
{C}
</text>
"""

# ==================================================
# 上　柱筋寸法チェーン
# ==================================================

previous = 0

for x in column_bars:

    svg += f"""
    <line
    x1="{x}"
    y1="-40"
    x2="{x}"
    y2="0"
    stroke="black"
    stroke-width="1"/>
    """

    center = (previous + x) / 2

    svg += f"""
    <text
    x="{center}"
    y="-48"
    text-anchor="middle"
    font-size="16">
    {x-previous}
    </text>
    """

    previous = x

last = CR - column_bars[-1]

svg += f"""
<text
x="{(CR+column_bars[-1])/2}"
y="-48"
text-anchor="middle"
font-size="16">
{last}
</text>
"""

svg += f"""
    <line
    x1="{CL}"
    y1="-40"
    x2="{CR}"
    y2="-40"
    stroke="black"
    stroke-width="1"/>
    """




# ==================================================
# コンクリート
# ==================================================

svg += """
<path
d="
M100 0
L750 0
L750 100
L850 100
L850 800
L750 800
L750 900
L100 900
L100 800
L0 800
L0 100
L100 100
Z"
fill="#ececec"
stroke="black"
stroke-width="2"/>

<!-- 上下の線を消す -->
<line x1="100" y1="0" x2="750" y2="0"
      stroke="#ececec"
      stroke-width="3"/>

<line x1="100" y1="900" x2="750" y2="900"
      stroke="#ececec"
      stroke-width="3"/>
"""

# ==================================================
# 梁筋
# ==================================================

for x in beam_bars:

    svg += f"""
    <line
        x1="{x}"
        y1="0"
        x2="{x}"
        y2="900"
        stroke="#222"
        stroke-width="12"/>
    """

# ==================================================
# 柱筋
# ==================================================

for x in column_bars:

    svg += f"""
    <circle
        cx="{x}"
        cy="160"
        r="18"
        fill="#666"
        stroke="black"
        stroke-width="1"/>

    <circle
        cx="{x}"
        cy="740"
        r="18"
        fill="#666"
        stroke="black"
        stroke-width="1"/>
    """

# ==================================================
# 下　梁筋寸法チェーン
# ==================================================

previous = 100

for x in beam_bars:

    svg += f"""
    <line
        x1="{x}"
        y1="900"
        x2="{x}"
        y2="940"
        stroke="black"
        stroke-width="1"/>
    """

    center = (previous + x) / 2

    svg += f"""
    <text
        x="{center}"
        y="960"
        text-anchor="middle"
        font-size="16">
        {x-previous}
    </text>
    """

    previous = x

last = CR -100 - beam_bars[-1]

svg += f"""
<text
x="{(CR-100+beam_bars[-1])/2}"
y="960"
text-anchor="middle"
font-size="16">
{last}
</text>
"""

svg += f"""
    <line
        x1="{CL+100}"
        y1="940"
        x2="{CR-100}"
        y2="940"
        stroke="black"
        stroke-width="1"/>
    """

# ==================================================
# 下　梁幅
# ==================================================

svg += f"""
<line
x1="{CL+100}"
y1="1020"
x2="{CR-100}"
y2="1020"
stroke="black"
stroke-width="2"/>

<line
x1="{CL+100}"
y1="900"
x2="{CL+100}"
y2="1020"
stroke="black"
stroke-width="2"/>

<line
x1="{CR-100}"
y1="900"
x2="{CR-100}"
y2="1020"
stroke="black"
stroke-width="2"/>

<text
x="{(CL+CR)/2}"
y="1045"
text-anchor="middle"
font-size="22">
B
</text>
"""

svg += "</svg>"

components.html(
    f"""
    <div style="width:100%;">
        {svg}
    </div>
    """,
    height=1200,
    scrolling=False,
)