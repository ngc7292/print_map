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
from pyecharts import Geo

from pyecharts import GeoLines, Style
from time import strftime,gmtime
style = Style(
    title_color = "#fff",
    title_pos = "center",
    title_text_size = 24,
    title_top = 10,
    width=1600,
    height=800,
    background_color="#404a59"
)

data = []

date = strftime("%a, %d %b %Y", gmtime())
geolines = GeoLines(title = "My trip", subtitle = date,**style.init_style)
geolines.add(
    "from rizhao",
    data,
    is_legend_show=False,
    is_geo_effect_show=False,
    symbol_size=0.1
)

# geo = Geo(title = "My trip", subtitle = date,**style.init_style)
# geo.add("",[],[],maptype='china')
print(geolines.echarts_options())
#geolines.render()