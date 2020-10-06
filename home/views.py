from django.shortcuts import render

# Create your views here.
from TopicComment.models import   Topic


def alltopic(request):
	topic = Topic.objects.all()
	return render(request,'home.html',{'all_topic':topic})