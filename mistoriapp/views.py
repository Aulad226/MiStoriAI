from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import openai 
import datetime
from django.views.generic import ListView
from mistoriapp.models import form
from .secret_key import API_KEY

# Create my views here.

class StoryListView(ListView):
    model = form
    context_object_name = 'form'
def home(request):
    now = datetime.datetime.now()
    hour = now.hour

    if hour <12:
        message = 'Good Morning!'
    elif hour <18:
        message = 'Good Afternoon!'
    else:
        message = 'Good Evening!'
    return render(request,'home.html', {'message': message})

def form(request):
    return render(request,'form.html', {})

def form_submit(request):
    openai.api_key = API_KEY
    name = topic = audience = keyword = ''
    if request.method == 'POST':
        name = request.POST.get('name', '')
        topic = request.POST.get('topic', '')
        audience = request.POST.get('audience', '')
        keyword = request.POST.get('keyword', '')

    page_data = {
        'name': name,
        'topic': topic,
        'audience': audience,
        'keyword': keyword,
    }

    gpt_prompt = page_data

    response = openai.Completion.create(
        model="text-davinci-003",
        page_data=gpt_prompt,
        temperature=0.8,
        max_tokens=600,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )

    page_data = response['choices'][0]['text']
    
    return render(request, 'form.html', {'page_data': page_data})

