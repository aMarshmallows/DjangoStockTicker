# -*- coding: utf-8 -*-
# every time we create a webpage need to create a corresponding view
# like the brains behind the scenes
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
# this request is a browser request
# gets passed into this function and returns something rendered that correlates to the page here
# {} allows us to pass stuff into this functin 
# we will be connecting to a third party API
# pk_2d0972b3fb5d4998962a399a402b6291
def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']

        # get data from API
        api_request = requests.get('https://cloud.iexapis.com/stable/stock/' +ticker+ '/quote?token=pk_2d0972b3fb5d4998962a399a402b6291')
        # do error checking for the data we got from the API

        try: 
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api })

    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol"});


def about(request):
    return render(request, 'about.html', {})