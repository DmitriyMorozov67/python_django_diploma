from django.urls import path
from .views import Catalog, BannerList, CategoriesList


urlpatterns = [
    path('api/catalog', Catalog.as_view(), name='products_list'),
    path('api/banners', BannerList.as_view(), name='banners'),
    path('api/categories', CategoriesList.as_view(), name='categories'),
]