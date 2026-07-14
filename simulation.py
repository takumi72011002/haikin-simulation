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

st.set_page_config(page_title="配筋図")

svg = """
<svg width="100%" viewBox="0 0 800 900">

    <!-- 背景 -->
    <rect x="0" y="0" width="800" height="900" fill="white"/>

    <!-- 柱 -->
    <rect
        x="100"
        y="0"
        width="600"
        height="900"
        fill="#e8e8e8"
        stroke="black"
        stroke-width="2"/>

    <!-- 左張り出し -->
    <rect
        x="0"
        y="100"
        width="100"
        height="700"
        fill="#e8e8e8"
        stroke="black"/>

    <!-- 右張り出し -->
    <rect
        x="700"
        y="100"
        width="100"
        height="700"
        fill="#e8e8e8"
        stroke="black"/>

    <!-- ===== 縦筋 ===== -->

    <line x1="150" y1="0" x2="150" y2="900"
          stroke="#333" stroke-width="12"/>

    <line x1="260" y1="0" x2="260" y2="900"
          stroke="#333" stroke-width="12"/>

    <line x1="340" y1="0" x2="340" y2="900"
          stroke="#333" stroke-width="12"/>

    <line x1="400" y1="0" x2="400" y2="900"
          stroke="#333" stroke-width="12"/>

    <line x1="460" y1="0" x2="460" y2="900"
          stroke="#333" stroke-width="12"/>

    <line x1="540" y1="0" x2="540" y2="900"
          stroke="#333" stroke-width="12"/>

    <line x1="650" y1="0" x2="650" y2="900"
          stroke="#333" stroke-width="12"/>

    <!-- ===== 上の梁筋 ===== -->

    <circle cx="70" cy="160" r="18" fill="#666"/>
    <circle cx="210" cy="160" r="18" fill="#666"/>
    <circle cx="290" cy="160" r="18" fill="#666"/>
    <circle cx="370" cy="160" r="18" fill="#666"/>
    <circle cx="470" cy="160" r="18" fill="#666"/>
    <circle cx="550" cy="160" r="18" fill="#666"/>
    <circle cx="650" cy="160" r="18" fill="#666"/>
    <circle cx="760" cy="160" r="18" fill="#666"/>

    <!-- ===== 下の梁筋 ===== -->

    <circle cx="70" cy="740" r="18" fill="#666"/>
    <circle cx="210" cy="740" r="18" fill="#666"/>
    <circle cx="290" cy="740" r="18" fill="#666"/>
    <circle cx="370" cy="740" r="18" fill="#666"/>
    <circle cx="470" cy="740" r="18" fill="#666"/>
    <circle cx="550" cy="740" r="18" fill="#666"/>
    <circle cx="650" cy="740" r="18" fill="#666"/>
    <circle cx="760" cy="740" r="18" fill="#666"/>

</svg>
"""

components.html(svg, height=900)






