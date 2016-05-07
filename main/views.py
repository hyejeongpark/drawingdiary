from django.shortcuts import render
from .models import Diary


def index(request):
    diary_list = Diary.objects.all().order_by('-date')
    return render(request, 'main/index.html', {'diary_list': diary_list, })
