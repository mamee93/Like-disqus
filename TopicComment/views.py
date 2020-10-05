from django.shortcuts import render,redirect
from .models import Topic,Comments
from .forms import CommentForm
from django.urls import reverse
# Create your views here.

def all_topic(request):

	all_topic = Topic.objects.all()
	return render(request,'topic/topic.html',{'all_topic':all_topic})


def topic_details(request,id):

	topc_title = Topic.objects.get(id=id)
	comments = Comments.objects.filter(topc_title=topc_title)
	total_comments = comments.count()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			myform = form.save(commit=False)
			myform.userComment = request.user
			myform.topc_title = topc_title
			myform.save()

	else:
		form = CommentForm()


	return render(request,'topic/topic_details.html',{'topc_title':topc_title,'comments':comments,'form':form,'total_comments':total_comments})
 
 