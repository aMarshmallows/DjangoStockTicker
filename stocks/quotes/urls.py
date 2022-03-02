# every app needs its own urls.py file
from django.conf.urls import url
from . import views

# views.home accesses the home fuction from the views file (which was imported above)
# in django 2.2 we now use 'url' instead of 'path' to create paths
# not sure what the r means but it works in stopping all urls matching the empty one
urlpatterns = [
    url('about.html', views.about, name="about"),
    url(r'^$', views.home, name="home"),
]
