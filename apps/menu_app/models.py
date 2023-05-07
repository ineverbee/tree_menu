from django.db import models
from django.utils.translation import gettext_lazy as _


class Menu(models.Model):
    name = models.CharField(
        max_length = 150,
        verbose_name = _('name'),
    )
    root = models.ForeignKey(
        'self',
        verbose_name = _('root'),
        related_name = u'leaf',
        blank = True,
        null = True,
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        verbose_name = _('parent'),
        related_name = u'child',
        blank = True,
        null = True,
        on_delete=models.CASCADE
    )
    parent_uri = models.SlugField(
        verbose_name = _('ParentURL'),
        blank = True,
        default='',
    )
    uri = models.SlugField(
        verbose_name = _('URL'),
        blank = True,
        null = True,
    )
    
    class Meta:
        verbose_name = _('menu')
        verbose_name_plural = _('menu')
        ordering = ('uri',)
    
    def get_absolute_url(self):
        return '/%s' % self.uri

    def __str__(self) -> str:
        return self.uri
    
    def __unicode__(self):
        return self.name