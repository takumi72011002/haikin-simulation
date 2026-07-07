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






