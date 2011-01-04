# -*- coding: utf-8 -*-

from django.conf import settings as django_settings

# Disables the latest news plugin. Defaults to False
DISABLE_LATEST_NEWS_PLUGIN = getattr(django_settings, \
    'CMSPLUGIN_NEWS_DISABLE_LATEST_NEWS_PLUGIN', False)
