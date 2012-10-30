# -*- coding: UTF-8 -*-
from django.db import models


class webnotepad(models.Model):
    title = models.CharField(max_length=150, verbose_name=u'Название')
    memory = models.TextField(verbose_name=u'Содержание')

    def __unicode__(self):
        return self.title
