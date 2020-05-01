from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
from .models import Data
import numpy as np
from sklearn import linear_model
# Create your views here.

# Use onevariable regression made by you learnt in coursera
def ab(data):
	trainx = data['x']
	trainx = [int(i) for i in trainx.split(",")]
	train_x = np.asarray(trainx)
	train_x = train_x.reshape(-1,1)
	trainy = data['y']
	trainy = [int(j) for j in trainy.split(",")]
	train_y = np.asarray(trainy)
	train_y = train_y.reshape(-1,1)
	x = np.concatenate((train_x,train_y),axis=1)
	print(train_x)
	print(train_y)
	print(x)
	test_x = data['testx']
	test_x = int(test_x)
	model = linear_model.LinearRegression()
	y = np.dot(x, np.array([1, 1]))
	print(y)
	model.fit(x,y)
	res = model.predict([[3,7]])
	
	print(res)

def index(request):
	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():
			form.save()
			res = ab(form.cleaned_data)
			return render(request,'processed.html',{'rdata':form})
	else:
		form = DataForm()
	return render(request,'add_data.html',{'datap': form})