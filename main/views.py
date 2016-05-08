from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Diary


def index(request):
    diary_list = Diary.objects.all().order_by('-date')
    paginator = Paginator(diary_list, 5)
    page = request.GET.get('page')
    try:
        diary_list = paginator.page(page)
    except PageNotAnInteger:
        diary_list = paginator.page(1)
    except EmptyPage:
        diary_list = paginator.page(paginator.num_pages)
    return render(request, 'main/index.html', {'diary_list': diary_list, })
