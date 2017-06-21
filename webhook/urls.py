#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from webhook import views


urlpatterns = [
    url(r'sample/$',
        views.SampleView.as_view(),
        name='sample-url'),
]