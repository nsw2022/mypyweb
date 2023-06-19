
from django.contrib import admin
from django.urls import path, include

from poll import views

urlpatterns = [

    #http://127.0.0.1:8000/poll/
    path('admin/', admin.site.urls),

    #http://127.0.0.1:8000/poll/test/
    path('poll/', include('poll.urls')),

    #http://127.0.0.1:8000/
    path('',views.index),
]
