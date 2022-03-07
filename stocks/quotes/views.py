# -*- coding: utf-8 -*-
# every time we create a webpage need to create a corresponding view
# like the brains behind the scenes
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm


# Create your views here.
# this request is a browser request
# gets passed into this function and returns something rendered that correlates to the page here
# {} allows us to pass stuff into this functin 
# we will be connecting to a third party API
# pk_2d0972b3fb5d4998962a399a402b6291
def home(request):
    import requests
    import json

    # if someone has posted aka filled out the form, get that ticker from the api
    if request.method == 'POST':
        ticker = request.POST['ticker']

        # get data from API
        api_request = requests.get('https://cloud.iexapis.com/stable/stock/' +ticker+ '/quote?token=pk_2d0972b3fb5d4998962a399a402b6291')
        
        # do error checking for the data we got from the API
        try: 
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        # return home page after passing in api
        return render(request, 'home.html', {'api': api })
    # otherwise, just load the home page
    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol"});


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    import requests
    import json

    # if somebody filled out this form and clicked the button, do this stuff
    if request.method == 'POST':
        # created a form variable and set it to StockForm after passing in the POSTed stuff or nothing
        form = StockForm(request.POST or None)

        # if it's valid, then we save it to the database and send success message and redirect to homepage
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect("add_stock")
    # otherwise, spit out the stuff that was stored onto the screen like we had been doing
    else:
        ticker = Stock.objects.all()
        output = []

        # loop through objects in ticker and add call api (also make sure to convert object t to a string before concatonating into api url)
        for t in ticker:
            # get data from API
            api_request = requests.get('https://cloud.iexapis.com/stable/stock/' +str(t)+ '/quote?token=pk_2d0972b3fb5d4998962a399a402b6291')
            
            # do error checking for the data we got from the API
            try: 
                api = json.loads(api_request.content)
            except Exception as e:
                api = "Error..."
            
            # save all calls to python list
            output.append(api)


        return render(request, 'add_stock.html', {'ticker' : ticker, 'output' : output})

def delete(request, stock_id):
    # access the database Stock and get the item with a 'primary key' or ID equal to the passed in stock_id
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Successfully deleted stock"))
    return redirect("add_stock")

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker' : ticker})