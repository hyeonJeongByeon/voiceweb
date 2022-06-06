from django.shortcuts import render
from django.http import HttpResponse
#from .manipulate_voice import voice_converter

#manipulate_voice.py import 하기

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Webpage for loading voice inputs.")

"""

def convert_user_voice(request):
    # Parsing user REQUEST
    # get voice data and factor from user
    file = open("/path/to/your/song.mp3", "rb").read() 
    request['Content-Disposition'] = 'attachment; filename=filename.mp3' 
    factor1 = request.POST['factor1']
    factor2 = request.POST['factor2']
    factor3 = request.POST['factor3']
    factor4 = request.POST['factor4']

    # convert voice 
    converted_voice = voice_converter(
        # 사용자에게 받은 팩터들을 통해서
        # 변조된 음성 데이터를 리턴해주는 함수
        factor1=factor1,
        factor2=factor2,
        )

    # return response with converted voice data
    return HttpResponse(converted_voice, mimetype="audio/mpeg")

# Create your views here.
"""