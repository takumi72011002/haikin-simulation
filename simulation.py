import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="配筋シミュレーション",
    page_icon="🌸",
)

st.title("配筋シミュレーション")


# ==========================================================
# 入力値
# ==========================================================

# ---------- 柱 ----------
column_width = 1200       # 柱幅(mm)
column_bar_d = 38         # 柱筋(D)
tie_bar_d = 13            # 帯筋(D)
column_bar_num = 8

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
beam_width = 750          # 梁幅(mm)
beam_bar_d = 19           # 梁筋(D)
stirrup_d = 13            # あばら筋(D)
beam_bar_num = 7

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
# 表示用
# ==========================================================

column_height = 900

# 梁幅750を柱幅1200の中央に配置
beam_left = (column_width - beam_width) / 2
beam_right = beam_left + beam_width


# ==========================================================
# SVG
# ==========================================================

svg = f"""
<svg
    width="100%"
    viewBox="-100 -150 1400 1200"
    xmlns="http://www.w3.org/2000/svg"
>


<!-- ======================================================
     上：柱幅
     ====================================================== -->

<line
    x1="0"
    y1="-90"
    x2="{column_width}"
    y2="-90"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="0"
    y1="-90"
    x2="0"
    y2="0"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{column_width}"
    y1="-90"
    x2="{column_width}"
    y2="0"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{column_width / 2}"
    y="-105"
    text-anchor="middle"
    font-size="20">
    {column_width}
</text>
"""


# ==========================================================
# 上：柱筋寸法
# ==========================================================

previous = 0

for x in column_bars:

    svg += f"""
    <line
        x1="{x}"
        y1="-60"
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
        y="-70"
        text-anchor="middle"
        font-size="16">
        {x - previous}
    </text>
    """

    previous = x


# 最後

last = column_width - column_bars[-1]

svg += f"""
<line
    x1="{column_bars[-1]}"
    y1="-60"
    x2="{column_bars[-1]}"
    y2="0"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{column_bars[-1] + last / 2}"
    y="-70"
    text-anchor="middle"
    font-size="16">
    {last}
</text>
"""


# ==========================================================
# コンクリート
# ==========================================================

svg += f"""
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

tie_left = 70
tie_right = column_width - 70
tie_top = 160
tie_bottom = 740

svg += f"""
<rect
    x="{tie_left}"
    y="{tie_top}"
    width="{tie_right - tie_left}"
    height="{tie_bottom - tie_top}"
    fill="none"
    stroke="#333333"
    stroke-width="{tie_bar_d}"
    rx="15"
/>
"""


# ==========================================================
# 帯筋フック
# ==========================================================

svg += f"""
<line
    x1="{tie_left}"
    y1="{tie_top + 35}"
    x2="{tie_left + 65}"
    y2="{tie_top + 90}"
    stroke="#333333"
    stroke-width="{tie_bar_d}"
    stroke-linecap="round"
/>
"""


# ==========================================================
# 柱筋
# ==========================================================

column_bar_r = column_bar_d / 2

for x in column_bars:

    svg += f"""
    <circle
        cx="{x}"
        cy="{tie_top}"
        r="{column_bar_r}"
        fill="#666666"
        stroke="black"
        stroke-width="1"
    />

    <circle
        cx="{x}"
        cy="{tie_bottom}"
        r="{column_bar_r}"
        fill="#666666"
        stroke="black"
        stroke-width="1"
    />
    """


# ==========================================================
# 下：梁筋寸法
# ==========================================================

previous = beam_left

for x in beam_bars:

    svg += f"""
    <line
        x1="{x}"
        y1="{column_height}"
        x2="{x}"
        y2="{column_height + 45}"
        stroke="black"
        stroke-width="1"
    />
    """

    center = (previous + x) / 2

    svg += f"""
    <text
        x="{center}"
        y="{column_height + 65}"
        text-anchor="middle"
        font-size="16">
        {x - previous:.0f}
    </text>
    """

    previous = x


# 最後

last = beam_right - beam_bars[-1]

svg += f"""
<line
    x1="{beam_bars[-1]}"
    y1="{column_height}"
    x2="{beam_bars[-1]}"
    y2="{column_height + 45}"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{beam_bars[-1] + last / 2}"
    y="{column_height + 65}"
    text-anchor="middle"
    font-size="16">
    {last:.0f}
</text>
"""


# ==========================================================
# 下：梁幅
# ==========================================================

svg += f"""
<line
    x1="{beam_left}"
    y1="{column_height + 100}"
    x2="{beam_right}"
    y2="{column_height + 100}"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{beam_left}"
    y1="{column_height}"
    x2="{beam_left}"
    y2="{column_height + 100}"
    stroke="black"
    stroke-width="1"
/>

<line
    x1="{beam_right}"
    y1="{column_height}"
    x2="{beam_right}"
    y2="{column_height + 100}"
    stroke="black"
    stroke-width="1"
/>

<text
    x="{(beam_left + beam_right) / 2}"
    y="{column_height + 130}"
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
    height=1050,
    scrolling=False,
)