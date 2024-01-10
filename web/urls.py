from django.contrib import admin
from django.urls import path

from news.views import CarApiList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarApiList.as_view())
]
