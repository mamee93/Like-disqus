from django.urls import path
from .views import all_topic,topic_details,like_topic

app_name = 'TopicComment'
urlpatterns = [
    path('topic',all_topic,name='all_topic'),
    path('<int:id>/',topic_details,name='topic_details'),
    path('like/',like_topic, name='like_topic'),
	 
     
]