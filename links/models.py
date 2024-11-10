from django.db import models


class Link(models.Model):
    """Model for storing links with their shortened versions"""
    full_url = models.URLField(unique=True, verbose_name='Link', help_text='Enter a link')
    short_url = models.CharField(max_length=7, db_index=True, verbose_name='Shortened link')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_url} -> {self.short_url}'
