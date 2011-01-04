# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from django.utils.translation import ugettext_lazy as _

from menu import CMSLatestNewsAppMenu


class CMSLatestNewsApp(CMSApp):
    name = _('News Application')
    urls = ['cmsplugin_news.urls']
    menus = [CMSLatestNewsAppMenu]

apphook_pool.register(CMSLatestNewsApp)

