from django.shortcuts import render
from blogapp.models import Author, Topic
from blogapp.forms import UserForm
# Create your views here.

def index(request):
    context_dict = {'something':'Hello There!'}
    return render(request, 'blogapp/index.html', context_dict)

def topics(request):
    topic_list = Topic.objects.all()
    return render(request, 'blogapp/topics.html', {'topic_list':topic_list})

def topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    return render(request, 'blogapp/topic.html', {'topic':topic})

def login(request):
    return render(request, 'blogapp/login.html', context=None)

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print('username: ' + form.cleaned_data['username'])
            print('email: ' + form.cleaned_data['email'])
            form.save()

    return render(request, 'blogapp/register.html', {'form':form})
