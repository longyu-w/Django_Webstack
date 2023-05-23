from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from .viewsets import *

router = DefaultRouter()

router.register('titles', TitlesViewSet, basename='titles')

router.register('category', CategoryViewSet, basename='category')

router.register('sub_category', SubCategoryViewSet, basename='sub_category')

router.register('site', SiteViewSet, basename='site')

router.register('friendlink', friendlinkViewSet, basename='friendlink')



urlpatterns = [
    path('',views.index_view),
    # path('', include(router.urls))
]