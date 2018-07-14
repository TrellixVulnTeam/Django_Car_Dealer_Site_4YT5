from django.shortcuts import render
from .models import Araba
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def anasayfa(request):
    arabalar_list = Araba.objects.all()
    paginator = Paginator(arabalar_list, 6)
    page = request.GET.get('sayfa')
    arabalar = paginator.get_page(page)
    return render(request, 'anasayfa.html', {'arabalar':arabalar})

def incele(request,id):
    id = Araba.objects.get(id=id)
    return render(request,'incele.html', {'id':id})

def hakkimizda(request):
    return render(request,'hakkimizda.html')