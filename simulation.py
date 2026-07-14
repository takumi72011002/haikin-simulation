import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

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

import streamlit.components.v1 as components

# ==========================================
# 配筋データ
# ==========================================

# 梁筋（縦棒）のX座標
beam_bars = [180, 300, 390, 450, 510, 600, 720]

# 柱筋（丸）のX座標
column_bars = [90, 240, 320, 390, 480, 560, 660, 770]

svg = """
<svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 850 900"
    preserveAspectRatio="xMidYMid meet"
    style="width:100%; height:auto;">

    <!-- 柱 -->
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

<!-- 上の線を消す -->
<line x1="100" y1="0" x2="750" y2="0"
      stroke="#ececec" stroke-width="3"/>

<!-- 下の線を消す -->
<line x1="100" y1="900" x2="750" y2="900"
      stroke="#ececec" stroke-width="3"/>

"""




# ==========================================
# 梁筋（縦棒）
# ==========================================

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

# ==========================================
# 柱筋（丸）
# ==========================================

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

svg += "</svg>"

components.html(
    svg,
    height=900,
    scrolling=False,
)

beam_no = list(range(1, len(beam_bars)+1))
column_no = list(range(1, len(column_bars)+1))

beam_table = pd.DataFrame([
    ["梁筋"] + beam_no + [""] * (8-len(beam_no)),
    ["梁筋の座標"] + beam_bars + [""] * (8-len(beam_bars))
])

column_table = pd.DataFrame([
    ["柱筋"] + column_no,
    ["柱筋の座標"] + column_bars
])

# 列名を空にする
column_table.columns = [f"c{i}" for i in range(len(column_table.columns))]
beam_table.columns = [f"c{i}" for i in range(len(beam_table.columns))]

st.dataframe(column_table, hide_index=True, use_container_width=True)
st.write("")
st.dataframe(beam_table, hide_index=True, use_container_width=True)