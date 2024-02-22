from django.shortcuts import render
from django.http import HttpResponse
from .tasks import scrape_proxy_data
# Create your views here.
def test(request):
    scrape_proxy_data.delay()
    return HttpResponse("Done")