from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index , name = 'index'),
    path('story/', views.ieltsstoriesListView.as_view(), name='stories'),
    path('story/<int:pk>', views.ieltsstoriesDetailView.as_view(), name='ieltsstories-detail'),
    path('test/', views.test_list, name='test'),
    re_path('test/(\d+)$', views.testDetailView, name='test-detail'),
    re_path('result/(\d+)$', views.result, name= 'result')
]
