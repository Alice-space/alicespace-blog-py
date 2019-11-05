from django.urls import path
from .viewsList import generateList
from .viewsDetail import generateDetail

urlpatterns = [
    path('article/<int:articleId>', generateDetail),
    path('<str:listColumn>/<int:listId>', generateList),
]
