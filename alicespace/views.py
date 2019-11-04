'''
@Author: Alicespace
@Date: 2019-11-04 15:44:34
@LastEditTime: 2019-11-04 15:44:34
'''
from django.shortcuts import render


# Create your views here.
def welcomeIndex(request):
    return render(request, 'welcome.html')
