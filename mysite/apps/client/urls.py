from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
   
    path('index/', views.Index.as_view(), name='index'),
    # path('admin/', admin.site.urls),
]
