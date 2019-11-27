'''
@Author: Alicespace
@Date: 2019-11-04 15:36:02
@LastEditTime: 2019-11-28 01:12:58
'''
from django.shortcuts import render
from .models import Article
from .viewsColumn import generateColumn
from django.http.response import Http404


# Create your views here.
def generateDetail(request, articleId):
    context = {}
    try:
        articleDetile = Article.objects.get(pk=articleId)
        context[
            'blog_detail_title'] = '[' + articleDetile.article_column.title + ']' + articleDetile.article_title
        context['blog_detail_time_release'] = articleDetile.create_time
        context['blog_detail_content'] = articleDetile.article_content
        context['blog_detail_time_edit'] = articleDetile.update_time
        context['blog_detail_auth'] = articleDetile.article_auth
        context = generateColumn(context)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'calmlog-details.html', context)
