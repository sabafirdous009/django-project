from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic

# Create your views here.
def index(request):
   webpage_list = AccessRecord.objects.order_by('date')
   data_dict = {'access_records':webpage_list}
   return render(request,template_name='first_app/index.html',context= data_dict)