
from django.contrib import admin
from django.urls import path , include
#Connecting the urls to urls.py in our app directory.


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('ManageSys.urls')),
]
