from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^(?P<question_id>[0-9]+)/submission/$',
        views.submission, name='submission'),
    path('userresponse/', views.UserResponseList.as_view()),
    path('userresponse/summary', views.UserResponseSummaryList.as_view()),
    path('report/', views.report, name='report'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
