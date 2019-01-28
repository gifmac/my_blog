
#we will create blog /urls.py  that its urls will be imported to ifewebsite/urls.py using the inclue function.

from django.conf.urls import url
from . import views # . means import view from the current module
#We will include namespace to different url variables that with the same name
app_name = "blog" #we will copy this to  the template to different variables with the same name


# Note in order to the problem of admin not reversible, urlpatterns should be a list [...].
#  I had it before as a  set {...}    we changed pattern  from a set to {} to a list []
# we will assign view named  index  to ^$ url when a user enter  an empty string, django will display the index page
# blog/index. It  makes blog/index.html the home page



urlpatterns = [
    url(r"^$", views.index, name="index"),
]

