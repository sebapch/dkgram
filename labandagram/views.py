"""MODULO URL DE LABANDAGRAM"""
#DJANGO
from django.http import HttpResponse

#UTILITIES
from datetime import datetime

def hello_world(request):
#RETURN GREETING
	#return HttpResponse('Hello World!')
#RETURN DATETIME
	
	return HttpResponse('Hoy es : {now}'.format(
		now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	))

def hi(request):
	#het the string of numbers
	numbers = request.GET['numbers']
	#convert the string to int and map it to int using a separator
	numbers = list(map(int,request.GET['numbers'].split(',')))
	#sort the array
	numbers.sort()
	#return the data
	return HttpResponse(str(numbers))
	