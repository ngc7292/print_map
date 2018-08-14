#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'ralph'
__mtime__ = '2018/8/4'
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
from django.conf.urls import url
from django.urls import path
from .views import login,register,logout,get_map,inde

urlpatterns = [
    url('user/login',login),
    url('user/register',register),
    url('user/logout',logout),
    url('map',get_map),
    url('',inde),
]