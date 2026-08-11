import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="配筋シミュレーション",
    page_icon="🌸",
)

st.title("配筋シミュレーション")


# ==========================================================
# 配筋データ
# ==========================================================

# ---------- 柱 ----------
column_width = 1200          # 柱幅 mm
column_bar_d = 38            # 柱筋 D
tie_bar_d = 13               # 帯筋 D
column_bar_num = 8           # 柱筋本数

column_bars = [
    85,
    226,
    384,
    522,
    677,
    874,
    995,
    1115
]


# ---------- 梁 ----------
beam_width = 750             # 梁幅 mm
beam_bar_d = 19              # 梁筋 D
stirrup_d = 13               # あばら筋 D
beam_bar_num = 7             # 梁筋本数

beam_bars = [
    259,
    351,
    453,
    554,
    644,
    744,
    842
]


# ==========================================================
# 表示用設定
# ==========================================================

# 柱の高さ
column_height = 900

# 柱・梁の中心
column_center = column_width / 2

# 梁は柱の中央に配置
beam_left = (column_width - beam_width) / 2
beam_right = beam_left + beam_width


# ==========================================================
# SVG開始
# ==========================================================

svg = f"""
<svg
    width="100%"
    viewBox="-100 -130 {column_width + 200} 1200"
    xmlns="http://www.w3.org/2000/svg"
>


<!-- =====================================================
     上側：柱幅寸法
     ===================================================== -->

<line
    x1="0"
    y1="-60"
    x2="{column_width}"
    y2="-60"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="0"
    y1="-60"
    x2="0"
    y2="0"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{column_width}"
    y1="-60"
    x2="{column_width}"
    y2="0"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{column_center}"
    y="-75"
    text-anchor="middle"
    font-size="18">
    {column_width}
</text>
"""


# ==========================================================
# 上側：柱筋寸法チェーン
# ==========================================================

previous = 0

for x in column_bars:

    svg += f"""
    <line
        x1="{x}"
        y1="-40"
        x2="{x}"
        y2="0"
        stroke="black"
        stroke-width="1"
    />
    """

    center = (previous + x) / 2

    svg += f"""
    <text
        x="{center}"
        y="-50"
        text-anchor="middle"
        font-size="16">
        {x - previous}
    </text>
    """

    previous = x


# 最後の区間
last = column_width - column_bars[-1]

svg += f"""
<line
    x1="{column_bars[-1]}"
    y1="-40"
    x2="{column_bars[-1]}"
    y2="0"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{column_bars[-1] + last / 2}"
    y="-50"
    text-anchor="middle"
    font-size="16">
    {last}
</text>
"""


# ==========================================================
# コンクリート
# ==========================================================

svg += f"""
<!-- 柱 -->
<rect
    x="0"
    y="0"
    width="{column_width}"
    height="{column_height}"
    fill="#eeeeee"
    stroke="black"
    stroke-width="2"
/>
"""


# ==========================================================
# 梁筋
# ==========================================================
# 梁筋は長方形で描画
# 太さ = beam_bar_d
# ==========================================================

for x in beam_bars:

    svg += f"""
    <rect
        x="{x - beam_bar_d / 2}"
        y="0"
        width="{beam_bar_d}"
        height="{column_height}"
        fill="#222222"
    />
    """


# ==========================================================
# 帯筋
# ==========================================================
# 帯筋は長方形
# 太さ = tie_bar_d
# ==========================================================

tie_x = 70
tie_y = 160
tie_width = column_width - 140
tie_height = column_height - 320

svg += f"""
<rect
    x="{tie_x}"
    y="{tie_y}"
    width="{tie_width}"
    height="{tie_height}"
    fill="none"
    stroke="#333333"
    stroke-width="{tie_bar_d}"
/>
"""


# ==========================================================
# 帯筋フック
# ==========================================================

svg += f"""
<line
    x1="{tie_x}"
    y1="{tie_y + 40}"
    x2="{tie_x + 65}"
    y2="{tie_y + 95}"
    stroke="#333333"
    stroke-width="{tie_bar_d}"
    stroke-linecap="round"
/>
"""


# ==========================================================
# 柱筋
# ==========================================================
# D38 → 円の直径38
# 半径 = 19
# ==========================================================

column_bar_r = column_bar_d / 2

for x in column_bars:

    svg += f"""
    <circle
        cx="{x}"
        cy="{tie_y}"
        r="{column_bar_r}"
        fill="#666666"
        stroke="black"
        stroke-width="1"
    />

    <circle
        cx="{x}"
        cy="{tie_y + tie_height}"
        r="{column_bar_r}"
        fill="#666666"
        stroke="black"
        stroke-width="1"
    />
    """


# ==========================================================
# 下側：梁筋寸法チェーン
# ==========================================================

previous = beam_left

for x in beam_bars:

    svg += f"""
    <line
        x1="{x}"
        y1="{column_height}"
        x2="{x}"
        y2="{column_height + 40}"
        stroke="black"
        stroke-width="1"
    />
    """

    center = (previous + x) / 2

    svg += f"""
    <text
        x="{center}"
        y="{column_height + 60}"
        text-anchor="middle"
        font-size="16">
        {x - previous:.0f}
    </text>
    """

    previous = x


# 最後の区間

last = beam_right - beam_bars[-1]

svg += f"""
<line
    x1="{beam_bars[-1]}"
    y1="{column_height}"
    x2="{beam_bars[-1]}"
    y2="{column_height + 40}"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{beam_bars[-1] + last / 2}"
    y="{column_height + 60}"
    text-anchor="middle"
    font-size="16">
    {last:.0f}
</text>
"""


# ==========================================================
# 下側：梁幅
# ==========================================================

svg += f"""
<line
    x1="{beam_left}"
    y1="{column_height + 90}"
    x2="{beam_right}"
    y2="{column_height + 90}"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{beam_left}"
    y1="{column_height}"
    x2="{beam_left}"
    y2="{column_height + 90}"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{beam_right}"
    y1="{column_height}"
    x2="{beam_right}"
    y2="{column_height + 90}"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{(beam_left + beam_right) / 2}"
    y="{column_height + 120}"
    text-anchor="middle"
    font-size="20">
    {beam_width}
</text>

</svg>
"""


# ==========================================================
# 表示
# ==========================================================

components.html(
    svg,
    height=1200,
    scrolling=False,
)