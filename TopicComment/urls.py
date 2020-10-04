from django.urls import path
from .views import all_topic
urlpatterns = [
    path('',all_topic,name='all_topic'),
]