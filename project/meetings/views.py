from django.shortcuts import render, redirect
from .models import Meetings
from.forms import MeetingForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, "index.html")

def meetings(request):
    meetings_list = Meetings.objects.all()    
    return render(request, "meetings.html", {'meetings_list': meetings_list})

def add_meeting(request):
    submitted = False
    if request.method == "POST":
        form=MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_meeting?submitted=True')
    else:
        form = MeetingForm
        if 'submitted' in request.GET:
            submitted=True    
    return render(request, "addmeeting.html", {'form': form, 'submitted': submitted})

def delete_meeting(request, meeting_id):
    meeting = Meetings.objects.get(pk= meeting_id)
    meeting.delete()
    return redirect('meetings')

def update_meeting(request, meeting_id):
    meeting = Meetings.objects.get(pk= meeting_id)
    form = MeetingForm(request.POST or None, instance=meeting)
    if form.is_valid():
        form.save()
        return redirect('meetings')
    return render(request, 'updatemeeting.html', {'meeting': meeting, 'form': form})