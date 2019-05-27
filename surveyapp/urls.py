'surveyapp URL Configuration'

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('survey/', include('survey.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/survey/', permanent=True)),
]