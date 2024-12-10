from django.shortcuts import render
from .models import MotivationQuotes
import datetime

# 뷰: 어플리케이션에 들어갈 로직 넣는 곳, 모델에서 정보를 가져와 템플릿에 뿌리는 역할

# Create your views here.
def home(request): 
    date = datetime.datetime.date(datetime.datetime.now())
    time = datetime.datetime.time(datetime.datetime.now())
    # 모델에 정의했던 MotivationQuotes 클래스의 모든 메소드를 가져옴
    motivationquotes = MotivationQuotes.objects.all()

    # 템플릿에 넘겨줄 파라미터 뭉치
    context = {
        "date":date,
        "time":time,
        "motivationquotes": motivationquotes,
    }

    # 파라미터 전달
    return render(request, 'home.html', context)