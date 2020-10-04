from django.shortcuts import render
from .models import Topic,Comments
from .forms import CommentForm
# Create your views here.

def all_topic(request):

	all_topic = Topic.objects.all()
	return render(request,'topic/topic.html',{'all_topic':all_topic})


def topic_details(request,id):

	topic_details = Topic.objects.get(id=id)
	comments = Comments.objects.filter(topic_details=topic_details)
	
	if request.method == POST:
		form = CommentForm()

	else:
		form = CommentForm()


	return render(request,'topic/topic_details.html',{'topic_details':topic_details,'form':form})


 