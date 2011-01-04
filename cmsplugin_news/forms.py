# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings

from cms.plugin_pool import plugin_pool
from cms.plugins.text.settings import USE_TINYMCE

from cmsplugin_news.widgets.wymeditor_widget import WYMEditor

from models import News

__all__ = ['NewsForm']


class NewsForm(forms.ModelForm):

    class Meta:
        model = News

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        # Use either TinyMCEEditor or WYMEditor
        plugins = plugin_pool.get_text_enabled_plugins(placeholder=None, page=None)
        if USE_TINYMCE and 'tinymce' in settings.INSTALLED_APPS:
            from cmsplugin_news.widgets.tinymce_widget import TinyMCEEditor
            widget = TinyMCEEditor(installed_plugins=plugins)
        else:
            widget = WYMEditor(installed_plugins=plugins)
        self.fields['content'].widget = widget
