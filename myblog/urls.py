#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Chenxiforever
from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'^$',index),
]