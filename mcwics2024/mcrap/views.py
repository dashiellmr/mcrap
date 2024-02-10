from django.shortcuts import render
from .forms import TextForm
import os
import vertexai as vai
from vertexai.language_models import TextGenerationModel
openai_key = os.getenv('GEMINI_KEY')

def mcrap(request):
    return render(request, 'mcrap/main.html')

def rapTransform(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            rap_song = createRap(256, 'mcwics2024', 'us-central1', text)
            return render(request, 'mcrap/output', {'rap_song': rap_song})
    else: 
        form = TextForm()
    return request(request, 'mcrap/main.html', {'form': form})

def createRap(temperature, project_id, location, input):
    vai.init(project_id, location)
    params = {
        "temperature": temperature,
        "max_output_tokens": 1024,
        "top_p": 0.8,
        "top_k": 40,
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(f"Imagine you're the greatest rap lyricist in the world, 
                             create a rap song based on this text: {input}.",
                               **params)   
    print(f"Response from model: {response.text}")
    return response.text
