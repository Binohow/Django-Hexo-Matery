import random
from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings
from .models import Links


def global_setting(request):
    """
    将settings里面的变量 注册为全局变量
    """
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESCRIPTION,
        'SITE_KEY': settings.SECRET_KEY,
        'SITE_MAIL': settings.SITE_MAIL,
        'SITE_ICP': settings.SITE_ICP,
        'SITE_ICP_URL': settings.SITE_ICP_URL,
        'SITE_TITLE': settings.SITE_TITLE,
        'SITE_TYPE_CHINESE': settings.SITE_TYPE_CHINESE,
        'SITE_TYPE_ENGLISH': settings.SITE_TYPE_ENGLISH
    }


class Index(View):
    """
    测试首页能否正常加载
    """
    def get(self, request):
        return render(request, 'index.html', {})


class Friends(View):
    """
    友链链接展示
    """
    def get(self, request):
        links = Links.objects.all()
        card_num = random.randint(1, 10)
        return render(request, 'friends.html', {
            'links': links,
            'card_num': card_num,
        })


