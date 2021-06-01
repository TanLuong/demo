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
    re_path('result/(\d+)$', views.result, name= 'result'),
    path('lesson/',views.lessonList, name='lesson'),
    path('lesson/basic/', views.lessonlevelListView, name = 'basic'),
    path('lesson/intermedia/', views.lessonlevelListView, name = 'intermedia'),
    path('lesson/advance/', views.lessonlevelListView, name = 'advance'),
    path('lesson/<int:pk>', views.lessonDetailView.as_view(), name = 'lesson-detail'),
    path('search/', views.searchListView.as_view(), name = 'search-result')
]
