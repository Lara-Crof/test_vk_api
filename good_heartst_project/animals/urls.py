from django.urls import path, include
from .views import AnimalList, AnimalPostDetail, CategoryList, CreatView

app_name ='animals'

urlpatterns = [
    path('', AnimalList.as_view(), name='list'),
    path('category/<int:category_id>/', CategoryList.as_view(), name='category'),
    path('<slug:animals_slug>/', AnimalPostDetail.as_view(), name='detail'),
    path('add_post', CreatView.as_view(), name='add'),

]

