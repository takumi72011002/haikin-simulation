import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="配筋シミュレーション",
    page_icon="🌸",
)

st.title("配筋シミュレーション")

st.write("こんにちは！")

name = st.text_input("名前")

if name:
    st.success(f"こんにちは、{name}さん！")

st.markdown("""
<svg width="60" height="60">
    <rect x="10" y="10" width="40" height="40"
          fill="black" />
</svg>
""", unsafe_allow_html=True)

st.markdown("""
<svg width="100" height="100">
    <circle cx="50" cy="50" r="30" fill="red"/>
</svg>
""", unsafe_allow_html=True)

st.markdown("""
<svg width="500" height="500">
    <rect x="50" y="50" width="300" height="300"
          fill="black" />
</svg>
""", unsafe_allow_html=True)

components.html("""
<svg
    width="100%"
    viewBox="0 0 1000 1000"
    preserveAspectRatio="xMidYMid meet">

    <rect x="100" y="100"
          width="800"
          height="800"
          fill="lightgray"
          stroke="black"
          stroke-width="8"/>

</svg>
""", height=1000)


import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="配筋シミュレーション")

# =====================================
# 寸法
# =====================================
COLUMN_W = 400     # 柱幅
COLUMN_H = 900

BEAM_W = 180       # 梁の出幅
BEAM_H = 700

# 梁筋（縦棒）
beam_bars = [260, 340, 410, 450, 490, 560, 640]

# 柱筋（丸）
column_bars = [60, 200, 280, 360, 540, 620, 700, 840]

svg = f"""
<svg width="100%" viewBox="0 0 900 900">

<!-- =========================
     左梁
========================= -->
<rect
    x="0"
    y="100"
    width="{BEAM_W}"
    height="{BEAM_H}"
    fill="#efefef"
    stroke="black"
    stroke-width="2"/>

<!-- =========================
     柱
========================= -->
<rect
    x="250"
    y="0"
    width="{COLUMN_W}"
    height="{COLUMN_H}"
    fill="#efefef"
    stroke="black"
    stroke-width="2"/>

<!-- =========================
     右梁
========================= -->
<rect
    x="720"
    y="100"
    width="{BEAM_W}"
    height="{BEAM_H}"
    fill="#efefef"
    stroke="black"
    stroke-width="2"/>
"""

# =============================
# 梁筋（縦棒）
# =============================
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

# =============================
# 柱筋（丸）
# =============================
for x in column_bars:
    svg += f"""
    <circle
        cx="{x}"
        cy="160"
        r="18"
        fill="#666"
        stroke="black"/>

    <circle
        cx="{x}"
        cy="740"
        r="18"
        fill="#666"
        stroke="black"/>
    """

svg += "</svg>"

components.html(svg, height=900)