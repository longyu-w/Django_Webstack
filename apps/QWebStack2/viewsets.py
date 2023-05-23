from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from .serializers import *


@method_decorator(name='list', decorator=swagger_auto_schema(operation_summary='获取所有主页设置资料'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='获取指定主页设置资料'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='添加主页设置资料'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_summary='修改指定主页设置资料'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='部分修改指定主页设置资料'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='删除指定主页设置资料'))
class TitlesViewSet(viewsets.ModelViewSet):
    """主页设置相关操作"""
    serializer_class = TitlesSerializer
    queryset = Titles.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@method_decorator(name='list', decorator=swagger_auto_schema(operation_summary='获取所有分类资料'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='获取指定分类资料'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='添加分类资料'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_summary='修改指定分类资料'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='部分修改指定分类资料'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='删除指定分类资料'))
class CategoryViewSet(viewsets.ModelViewSet):
    """分类相关操作"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@method_decorator(name='list', decorator=swagger_auto_schema(operation_summary='获取所有子分类资料'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='获取指定子分类资料'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='添加子分类资料'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_summary='修改指定子分类资料'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='部分修改指定子分类资料'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='删除指定子分类资料'))
class SubCategoryViewSet(viewsets.ModelViewSet):
    """子分类相关操作"""
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@method_decorator(name='list', decorator=swagger_auto_schema(operation_summary='获取所有站点资料'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='获取指定站点资料'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='添加站点资料'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_summary='修改指定站点资料'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='部分修改指定站点资料'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='删除指定站点资料'))
class SiteViewSet(viewsets.ModelViewSet):
    """站点相关操作"""
    serializer_class = SiteSerializer
    queryset = Site.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@method_decorator(name='list', decorator=swagger_auto_schema(operation_summary='获取所有友情链接资料'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='获取指定友情链接资料'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='添加友情链接资料'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_summary='修改指定友情链接资料'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='部分修改指定友情链接资料'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='删除指定友情链接资料'))
class friendlinkViewSet(viewsets.ModelViewSet):
    """友情链接相关操作"""
    serializer_class = friendlinkSerializer
    queryset = friendlink.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

