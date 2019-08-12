# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json

    #Get Crypto Currency values
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,LTC,BCH,BNB,OKB,XRP,TRX,ETC&tsyms=USD,EUR')
    price = json.loads(price_request.content)

    #Get Crypto News Data
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, "home.html", {'api':api, 'price': price})

def prices(request):
    print ("Request is")
    if request.method == "POST":
        import requests
        import json
        quote = request.POST.get('quote').upper()
        price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+quote+'&tsyms=USD')
        crypto = json.loads(price_request.content)

        if crypto.get('Response'):
            notfound = "Sorry, "+ quote + " doesn't exist. Please Try Again"
            return render(request, "prices.html",{'notfound':notfound})
        else:
            return render(request, "prices.html",{'crypto': crypto, 'quote':quote})


    notfound = "Please enter a crypto symbol into the search bar"

    return render(request, "prices.html",{'notfound':notfound})
