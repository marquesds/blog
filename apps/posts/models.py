from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.accounts.models import User


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=200)
    text = models.TextField(_('Text'))

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created_at']
