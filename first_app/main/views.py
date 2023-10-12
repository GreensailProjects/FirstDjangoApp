from django.shortcuts import render, HttpResponse
from .models import Topic


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'main/topics.html', context)
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'main/topic.html', context)
