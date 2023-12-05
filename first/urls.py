from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name='index')
    , path('select/', views.select, name='select')
    , path('result/', views.result, name='result')
    # , path('select/<int:year>', ) # path variable이 필요할 경우
    # , re_path(r'^select/(?P<year>[0-9]/$') # 정규식이 필요한 경우
}
