from django.urls import path
from .views import alltopic

app_name = 'home'
urlpatterns = [
    path('',alltopic,name='all_topic'),
    
]