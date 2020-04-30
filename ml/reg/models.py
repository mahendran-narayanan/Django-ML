from django.db import models
from sklearn import linear_model
import numpy as np
# Create your models here.
class Data(models.Model):
	x = models.CharField(max_length=10000)
	y = models.CharField(max_length=10000,default="0")
	testx = models.CharField(max_length=10000,default="0")
	def ab(self):
		train_x = self.x
		train_x = train_x.split(",")
		train_x = list(map(float,train_x))
		train_x = np.asarray(train_x)
		train_x = train_x.reshape(-1,1)
		
		train_y = self.y
		train_y = train_y.split(",")
		train_y = list(map(float,train_y))
		train_y = np.asarray(train_y)
		train_y = train_y.reshape(-1,1)
		
		model = linear_model.LinearRegression()
		model.fit(train_x,train_y)
		test_x = self.testx
		test_x = test_x.reshape(-1,1)
		res = model.predict(test_x)
		return res