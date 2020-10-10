from django.shortcuts import render,redirect
from .models import Topic,Comments,Like
from accounts.models import Profile
from .forms import CommentForm
from django.urls import reverse
# Create your views here.

def all_topic(request):
	user = request.user
	profile = Profile.objects.get(user=user)
	all_topic = Topic.objects.filter(user=user)
	return render(request,'topic/topic.html',{'all_topic':all_topic,'profile':profile})


def topic_details(request,id):
	user = request.user
	# profile = Profile.objects.get(user=user)
	topc_title = Topic.objects.get(id=id)
	comments = Comments.objects.filter(topc_title=topc_title,reply=None).order_by('-id')
	total_comments = comments.count()
	if request.method == 'POST':
		form = CommentForm(request.POST)
 

		if form.is_valid():
			myform = form.save(commit=False)
			reply_id = request.POST.get('comments_id')
			comment_qs = None
			if reply_id:
				comment_qs = Comments.objects.get(id=reply_id)

			myform.reply=comment_qs
			myform.userComment = request.user
			myform.topc_title = topc_title
			myform.save()

	else:
		form = CommentForm()
 


	return render(request,'topic/topic_details.html',{'topc_title':topc_title,'comments':comments,'form':form,'total_comments':total_comments})
 
def like_topic(request):
	 
	user = request.user
	 
	if request.method == 'POST':
		topic_id = request.POST.get('topic_id')
		topic_like = Topic.objects.get(id=topic_id)

		if user in topic_like.like.all():
			topic_like.like.remove(user)

		else:
			topic_like.like.add(user)
		like, created = Like.objects.get_or_create(user=user,topic_id=topic_id)
		if not created:
			if like.value == 'Like':
				like.value == 'UnLike'
			else:
				like.value == 'Like'

		like.save()

	return redirect('TopicComment:all_topic')  