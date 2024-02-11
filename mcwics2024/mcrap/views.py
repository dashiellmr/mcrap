from django.shortcuts import render
from .forms import TextForm
import cohere
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


client = cohere.Client('xiRQw9XMonQhgxXa3x2WLAfuG7tdQwBAerIEPiUz')
def mcrap(request):
    return render(request, 'mcrap/main.html')

def rap_transform(request):
    if request.method == "POST":
        rap_song_input = request.POST.get('rap_song')
        if rap_song_input:
            rap_song = createRap(rap_song_input)  
            rap_split = rap_song.split('\n')
            clean_lyrics = []
            for lyric in rap_split:
                if "(" not in lyric and "[" not in lyric and ":" not in lyric:
                    clean_lyrics.append(lyric)
            clean_lyrics = clean_lyrics[:-1]
            
            return render(request, 'mcrap/output.html', {'rap_song': clean_lyrics}) 
    return render(request, 'mcrap/main.html')


def createRap(text):
    response = client.generate(
        prompt=f'''Imagine youre the greatest rap lyricist of all time -- write a rap about these notes but make it help with 
        comprehension, please dont add any additional text except the lyrics of the song, also prioritze rhyming over everything: {text}''',
    )
    return response.generations[0].text

def increaseSpeed(song, target_speed=1.5):
    speech = AudioSegment.from_mp3("rap.mp3")
    new_speed = speech.speedup(playback_speed=target_speed)
    new_speed.export("modified_speech.mp3", format="mp3")