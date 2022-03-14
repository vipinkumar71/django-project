from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from polls.models import Poll


def index(request):
    return render(request, "index.html", {"name": "vipin", "student": ["xyz", "vipin", "vikas", "yogi"]})


def about(request):
    return render(request, "about.html", {"name": "vipin"})


def polls(request):
    poll_list = Poll.objects.all()
    return render(request, "poll_list.html", {"polls": poll_list})


def rate(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    poll.rating += 1
    poll.save()
    return HttpResponseRedirect("/polls/poll-list/")


def create_poll(request):
    if request.POST:
        title = request.POST.get("title")
        description = request.POST.get("description")
        Poll.objects.create(title=title, description=description)
        return HttpResponseRedirect('/polls/poll-list')
    return render(request, "poll-form.html", {})


def poll_details(request, poll_id):
    return render(request, 'poll-details.html', {"poll": Poll.objects.get(id=poll_id)})
