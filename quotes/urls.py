# every app needs its own urls.py file
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

# views.home accesses the home fuction from the views file (which was imported above)
# in django 2.2 we now use 'url' instead of 'path' to create paths
# not sure what the r means but it works in stopping all urls matching the empty one
urlpatterns = [
    url('add_stock.html', views.add_stock, name="add_stock"),
    # don't want delete.html - want to pass in stock id
    # not sure why (?P<stock_id>.*) works for allowing this url to take in data 
    # (simply using <stock_id> did not work) but it does!
    url('delete/(?P<stock_id>.*)', views.delete, name="delete"),
    url('delete_stock', views.delete_stock, name="delete_stock"),
    url(r'^$', views.home, name="home"),
]

urlpatterns += staticfiles_urlpatterns()