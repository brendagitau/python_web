from django.shortcuts import render
from .forms import EventForm
from .models import Event

# Create your views here.
def register_event(request):
    form =EventForm
    if request.method=='POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)  
    else:
         form= EventForm()
    return render(request,'event.html',{'form':form})
def event_list(request):
    events=Event.objects.all()
    return render(request,'event_list.html',{'events':events})         

    