from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Situation(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(verbose_name='Описание')
    what_i_feel = models.TextField(verbose_name='Что я чувствую')
    what_i_think = models.TextField(verbose_name='Что я думаю')
    what_i_do = models.TextField(verbose_name='Что я делаю')
    what_i_want = models.TextField(verbose_name='Чего я хочу')
    pic = models.ImageField(null=True, blank=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Ситуация'
        verbose_name_plural = 'Ситуации'

    def __str__(self):
        return self.title
