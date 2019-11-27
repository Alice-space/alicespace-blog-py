'''
@Author: Alicespace
@Date: 2019-11-04 15:36:02
@LastEditTime: 2019-11-27 23:48:55
'''
from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
class ArticleColumn(models.Model):
    """
    栏目的 Model
    """
    # 栏目标题
    title = models.CharField(max_length=100, blank=True)
    # 创建时间
    created = models.DateTimeField(auto_now=True)


class Article(models.Model):
    article_title = models.CharField(max_length=150, verbose_name='标题')
    # article_content = models.TextField(verbose_name='正文')
    article_content = MDTextField()
    article_auth = models.CharField(max_length=20, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    article_picurl = models.CharField(max_length=1500, verbose_name='标题图片')
    is_top = models.BooleanField(verbose_name='置顶', default=False)
    # 文章栏目的 “一对多” 外键
    article_column = models.ForeignKey(ArticleColumn,
                                       null=True,
                                       blank=True,
                                       on_delete=models.CASCADE,
                                       related_name='articles')

    class Meta:
        ordering = ('-create_time', )
