# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100) #blog title
    category = models.CharField(max_length = 50, blank = True)#Blog_BiaoQian
    date_time = models.DateTimeField(auto_now_add = True) # blog_time
    content = models.TextField(blank = True, null= True) #blog_ZhengWen
    def __str__(self):
	return self.title
    class Meta: #time_PaiXu
	ordering = ['-date_time']
    
# Create your models here.
