import requests
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
def home(request): 
	context = {}
	return render(request, 'home.html', context)  


def home(request):
	apidata_list = requests.get('https://api.coingecko.com/api/v3/coins/list').json() 
	currencies = ['AED','ARS','AUD','BDT','BHD','BMD','BRL','CAD','CHF','CLP','CZK','DKK','GBP','HKD','HUF','ILS','INR','KWD','LKR','MMK','MXN','MYR','NGN','NOK','NZD','PHP','PKR','PLN','SAR','SEK','SGD','THB','TRY','UAH','VEF','VND','ZAR','XDR']
	default_currency = 'USD'
	currency_choice = str(request.GET.get('currency_choice'))
	if currency_choice in currencies: 
		apidata = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=' + currency_choice + '&order=market_cap_desc'
		print (apidata)
		apiresult = requests.get(apidata).json() 
		data = {'apiresult' : apiresult}
		return JsonResponse(data) 
	else:
		apidata = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=' + default_currency + '&order=market_cap_desc').json()
		context = {
			'apidata' : apidata,
			'apidata_list': apidata_list, 
			'currencies' : currencies,
			'default_currency': default_currency
		}
		return render(request, 'home.html', context)

def search(request): 
	search_result = str(request.GET.get('search_result'))
	apiresult = 'https://api.coingecko.com/api/v3/coins/'+search_result
	print(apiresult) 
	apiresult = requests.get(apiresult).json() 
	data = {'apiresult' : apiresult}
	return JsonResponse(data) 