from django.shortcuts import render
from .models import Article
from .viewsColumn import generateColumn
from django.http.response import Http404
import markdown


# Create your views here.
def generateDetail(request, articleId):
    context = {}
    try:
        articleDetile = Article.objects.get(pk=articleId)
        context[
            'blog_detail_title'] = '[' + articleDetile.article_column.title + ']' + articleDetile.article_title
        context['blog_detail_time_release'] = articleDetile.create_time
        context['blog_detail_content'] = markdown.markdown(
            articleDetile.article_content,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])
        context['blog_detail_time_edit'] = articleDetile.update_time
        context['blog_detail_auth'] = articleDetile.article_auth
        context = generateColumn(context)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'calmlog-details.html', context)
