from django.contrib import admin
from .models import Article, ArticleColumn


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


class ControlArticleColumn(admin.ModelAdmin):
    # 显示的字段
    list_display = ('title', 'created')
    # 搜索条件
    search_fields = ('title', )


# 注册Article表
admin.site.register(Article, ControlArticle)
admin.site.register(ArticleColumn, ControlArticleColumn)
