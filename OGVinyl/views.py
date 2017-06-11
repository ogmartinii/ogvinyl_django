from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import loader
from .models import Artist
from .models import Record


# Create your views here.

def index(request):
    featured_records = Record.objects.filter(featured=1)
    latest_records = Record.objects.order_by('-created')[:3]
    artist_list = Artist.objects.order_by('name')[:10]
    
    context = { 'artist_list' : artist_list,
                'featured_records' : featured_records,
                'latest_records' : latest_records }
    
    return render(request, 'OGVinyl/index.html', context)

def record_list(request):
    records = Record.objects.order_by('name')
    paginator = Paginator(records, 10)
    
    page = request.GET.get('page')
    try:
        record_list = paginator.page(page)
    except PageNotAnInteger:
        record_list = paginator.page(1)
    except EmptyPage:
        record_list = paginator.page(paginator.num_pages)
    
    context = { 'record_list' : record_list }
    
    return render(request, 'OGVinyl/records.html', context)

def record_detail(request, id):
    record = Record.objects.get(pk=id)
    
    context = { 'record' : record }

    return render(request, 'OGVinyl/record_detail.html', context)