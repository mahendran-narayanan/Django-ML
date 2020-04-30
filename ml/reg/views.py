from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
from .models import Data
# Create your views here.
def index(request):
	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():
			form.save()
			inst = Data.objects.reverse()[0]
			res = Data.ab(inst)
			return render(request,'processed.html',{'rdata':form})
	else:
		form = DataForm()
	return render(request,'add_data.html',{'datap': form})