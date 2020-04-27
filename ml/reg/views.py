from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
# Create your views here.
def index(request):
	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Data Added to DB')
	else:
		form = DataForm()
	return render(request,'add_data.html',{'datap': form})