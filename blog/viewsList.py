'''
@Author: Alicespace
@Date: 2019-11-04 15:50:44
@LastEditTime: 2019-11-25 15:40:24
'''
from django.shortcuts import render
from .models import Article, ArticleColumn
from .viewsColumn import generateColumn
from django.http.response import Http404, HttpResponse
import re

ItemPerPage = 6
firstPage = 1
NavBarPerPage = 15

# Create your views here.


def abstract(s):
    abstract = s
    pattern = re.compile(
        u'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    items_to_filter = re.findall(pattern, s)
    items_to_filter += ['!', '#', '[', ']', '>', '(', ')', '```', '**', '-']
    for item in items_to_filter:
        abstract = abstract.replace(item, "")
    return abstract[:50]


def generateListContent(listId, context, ArticleSet):
    listItems = []
    listItemFirst = (listId - 1) * ItemPerPage
    for article_item in ArticleSet[listItemFirst:listItemFirst + ItemPerPage]:
        listItem = {}
        listItem[
            'title'] = '[' + article_item.article_column.title + ']' + article_item.article_title
        listItem['content'] = abstract(article_item.article_content[:300])
        listItem['url'] = '/blog/article/' + str(article_item.id)
        listItem['picurl'] = article_item.article_picurl
        if article_item.is_top:
            listItem['title'] = '[置顶] ' + listItem['title']
            listItems.insert(0, listItem)
        else:
            listItems.append(listItem)
    context['listItems'] = listItems
    return context


def generateListNavBar(listId, context, ArticleSet, listColumn):
    max_id = ArticleSet.count()
    listNavBars = []
    #  整除问题
    if listId % NavBarPerPage == 0:
        startId = (int(listId / NavBarPerPage) - 1) * NavBarPerPage + 1
    else:
        startId = int(listId / NavBarPerPage) * NavBarPerPage + 1
    if max_id % ItemPerPage == 0:
        endId = min(int(max_id / ItemPerPage), startId - 1 + NavBarPerPage)
    else:
        endId = min(int(max_id / ItemPerPage) + 1, startId - 1 + NavBarPerPage)
    #  生成NavBars
    for i in range(startId, endId + 1):
        listNavBar = {}
        listNavBar['barId'] = str(i)
        listNavBar['barIdUrl'] = '/blog/' + listColumn + '/' + str(i)
        if i == listId:
            listNavBar['active'] = 'active'
        else:
            listNavBar['active'] = ''
        listNavBars.append(listNavBar)
    context['listNavBars'] = listNavBars
    #  判断前一组按钮
    if startId == 1:
        context['previousDisabled'] = 'disabled'
    else:
        context['previousDisabled'] = ''
        context['previousUrl'] = '/blog/' + listColumn + '/' + str(startId - 1)
    #  判断后一组按钮
    if endId == int(max_id / ItemPerPage) + 1 or endId == 1:
        context['nextDisabled'] = 'disabled'
    else:
        context['nextDisabled'] = ''
        context['nextUrl'] = '/blog/' + listColumn + '/' + str(endId + 1)
    return context


def generateList(request, listColumn, listId):
    if listColumn == 'all':
        Articles = Article.objects.all()
    else:
        Articles = ArticleColumn.objects.get(title=listColumn).articles.all()
    context = {}
    context = generateListContent(listId, context, Articles)
    context = generateListNavBar(listId, context, Articles, listColumn)
    context = generateColumn(context)
    return render(request, 'calmlog-list.html', context)
