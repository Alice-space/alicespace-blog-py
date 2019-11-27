'''
@Author: Alicespace
@Date: 2019-11-04 15:36:02
@LastEditTime: 2019-11-27 23:53:50
'''
from django.contrib import admin
from .models import Article, ArticleColumn
from mdeditor.widgets import MDEditorWidget
from django.db import models


# Register your models here.
class ControlArticle(admin.ModelAdmin):
    def article_column_title(self, obj):
        return u'%s' % obj.article_column.title

    article_column_title.short_description = u'目录'
    # 显示的字段
    list_display = ('article_title', 'article_content', 'article_auth',
                    'create_time', 'update_time', 'article_column_title')
    # 搜索条件
    search_fields = ('article_title', )

    formfield_overrides = {models.TextField: {'widget': MDEditorWidget}}


class ControlArticleColumn(admin.ModelAdmin):
    # 显示的字段
    list_display = ('title', 'created')
    # 搜索条件
    search_fields = ('title', )


# 注册Article表
admin.site.register(Article, ControlArticle)
admin.site.register(ArticleColumn, ControlArticleColumn)
