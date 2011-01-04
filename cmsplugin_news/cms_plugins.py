# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import LatestNewsPlugin, News
from settings import DISABLE_LATEST_NEWS_PLUGIN


class CMSLatestNewsPlugin(CMSPluginBase):
    """
    Render widget showing latest news.

    """
    model = LatestNewsPlugin
    name = _('Latest news')
    render_template = 'cmsplugin_news/latest_news.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'latest': News.published.all()[:instance.limit],
            'placeholder': placeholder,
            })
        return context

if not DISABLE_LATEST_NEWS_PLUGIN:
    plugin_pool.register_plugin(CMSLatestNewsPlugin)
