from django.contrib import admin
from django.urls import path
from proyecto import views # se llama el archivo desde el proyecto y la vista
#https://docs.djangoproject.com/en/3.2/topics/http/urls/

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('hello_word/', views.hello_word),
    path('mensaje_dia/',views.mensaje_dia),
    path('hi/',views.hi),
    path('menmsaje/',views.mensaje),



]
