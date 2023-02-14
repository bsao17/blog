from django.urls import path
from .views import articles, api


urlpatterns = [
    path('', articles),
    path('api', api)
]