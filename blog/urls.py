from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
]
#http://127.0.0.1:8000 => r'이후에 오는걸로 포스트_리스트 뷰 보여줘라

