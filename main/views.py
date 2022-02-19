import requests
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
def home(request): 
	context = {}
	return render(request, 'home.html', context)  


def home(request):
	apidata = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc').json()
	apidata_list = requests.get('https://api.coingecko.com/api/v3/coins/list').json() 
	context = {
		'apidata' : apidata,
		'apidata_list': apidata_list, 
	}
	return render(request, 'home.html', context)

def search(request): 
	search_result = str(request.GET.get('search_result'))
	apiresult = 'https://api.coingecko.com/api/v3/coins/'+search_result
	print(apiresult) 
	apiresult = requests.get(apiresult).json() 
	data = {'apiresult' : apiresult}
	return JsonResponse(data) 