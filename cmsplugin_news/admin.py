# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _, ungettext

from models import News
from forms import NewsForm


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'pub_date')
    list_filter = ('is_published', )
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'pub_date'

    form = NewsForm

    actions = ['make_published', 'make_unpublished']

    def make_published(self, request, queryset):
        """Marks selected news items as published."""
        rows_updated = queryset.update(is_published=True)
        self.message_user(request, ungettext('%(count)d newsitem was published',
                                             '%(count)d newsitems where published',
                                             rows_updated) % {'count': rows_updated})
    make_published.short_description = _('Publish selected news')

    def make_unpublished(self, request, queryset):
        """Marks selected news items as unpublished."""
        rows_updated =queryset.update(is_published=False)
        self.message_user(request, ungettext('%(count)d newsitem was unpublished',
                                             '%(count)d newsitems where unpublished',
                                             rows_updated) % {'count': rows_updated})
    make_unpublished.short_description = _('Unpublish selected news')

admin.site.register(News, NewsAdmin)
