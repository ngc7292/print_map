#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'ralph'
__mtime__ = '2018/8/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃       ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
              ┃   ┗━━━┓
              ┃神兽保佑┣┓
              ┃永无BUG  ┏┛
              ┗┓┓┏━┳┓┏━┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
from pyecharts import GeoLines

from pyecharts import GeoLines, Style

style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#404a59"
)

data = [
    ["日照","莒县",10],
    ["莒县","临沂",20],
    ["临沂","费县"],
    ["费县","曲阜"],
    ["曲阜","兖州"],
    ["兖州","泰安"],
    ["泰安","济南"],
]
geolines = GeoLines(title = "My trip", **style.init_style)
geolines.add("从广州出发", data, is_legend_show=False,is_geo_effect_show=True,symbol_size=1)
geolines.render()