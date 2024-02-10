from django.shortcuts import render
from .forms import TextForm
import os
import openai
openai_key = os.environ.get('OPENAI_KEY')

def mcrap(request):
    return render(request, 'mcrap/main.html')

def rapTransform(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            openai.api_key=openai_key
            response = openai.ChatCompletion.create(
                model="gpt-4", 
                messages=[{"role": "system", "content": "You are the most talented rap lyricist in the world."},
                          {"role": "user", "content": f"Convert the following text into a rap song: {text}"}]
            )
            rap_song = response.choices[0].message['content']
            return render(request, 'mcrap/output', {'rap_song': rap_song})
    else: 
        form = TextForm()
    return request(request, 'mcrap/main.html', {'form': form})