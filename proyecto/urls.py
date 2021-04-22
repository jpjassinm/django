from django.contrib import admin
from django.urls import path
from proyecto import views # se llama el archivo desde el proyecto y la vista

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('hello_word/', views.hello_word),
    path('mensaje_dia/',views.mensaje_dia),



]
