'''
@Author: Alicespace
@Date: 2019-11-04 15:50:18
@LastEditTime: 2019-11-04 15:50:19
'''
from .models import ArticleColumn


# to generate column at rightbar
def generateColumn(context):
    columnSet = ArticleColumn.objects.all()
    columnItems = []
    for column in columnSet:
        columnItem = {}
        columnItem['columnUrl'] = '/blog/' + column.title + '/1'
        articleNum = ArticleColumn.objects.get(
            title=column.title).articles.all().count()
        columnItem['columnContent'] = column.title + '(' + str(
            articleNum) + ')'
        columnItems.append(columnItem)
    context['columnItems'] = columnItems
    return context
