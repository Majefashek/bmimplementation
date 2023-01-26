from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
import uuid
from .models import Url
from django.http import HttpResponse
# Create your views here.


class Shotener(TemplateView):
    template_name = "index.html"
    

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def urlRedirect(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)

