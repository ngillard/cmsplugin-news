# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

now = datetime.datetime.now()

__all__ = ['News', 'LatestNewsPlugin']


class PublishedNewsManager(models.Manager):
    """
    Filters out all unpublished and items with a publication date in the future.

    """
    def get_query_set(self):
        return super(PublishedNewsManager, self).get_query_set().filter(
            is_published=True).filter(pub_date__lte=now)


class News(models.Model):

    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), unique_for_date='pub_date',
        help_text=_('A slug is a short name which uniquely identifies the news item for this day'))
    excerpt = models.TextField(_('Excerpt'), blank=True, help_text=_('Short description'))
    content = models.TextField(_('Content'), blank=True)

    is_published = models.BooleanField(_('Published'), default=False)
    pub_date = models.DateTimeField(_('Publication date'), default=now)

    # For internal use

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    objects = models.Manager()
    published = PublishedNewsManager()

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        ordering = ('-pub_date', )

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%m"),
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug,
            })


class LatestNewsPlugin(CMSPlugin):
    """
    Model for the settings when using the latest news cms plugin.

    """
    limit = models.PositiveIntegerField(_('Number of news items to show'),
        help_text=_('Limits the number of items that will be displayed'))
