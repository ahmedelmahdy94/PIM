from django.conf.urls import include, url
from django.urls import path

from .views import *


urlpatterns = [

  path("Products/", ProductView.as_view()), #POST
  path('Products/<prod_id>', Productqu.as_view()), #PUT & GET & DELETE
  path("Products/GetAll/page/<page_num>", ProductGetAll.as_view()), #GET
  path("Products/GetAllActice/page/<page_num>", ProductGetAllActice.as_view()), #GET

  path("Category/", CategoryViewCreate.as_view()), #POST
  path('Category/<cate_id>', CategoryView.as_view()), #PUT & GET & DELETE
  path("Category/GetAll/page/<page_num>", CategoryGetAll.as_view()), #GET
  path("Category/GetAllActice/page/<page_num>", CategoryGetAllActice.as_view()), #GET

  # path("Productz/<str:product_name>", Productqu.as_view()),


]
