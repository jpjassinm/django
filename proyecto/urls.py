from django.contrib import admin
from django.urls import path
from proyecto import views as local_views # se llama el archivo desde el proyecto y la vista
from posts import views as posts_views

#https://docs.djangoproject.com/en/3.2/topics/http/urls/

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('hello_word/', local_views.hello_word),
    path('mensaje_dia/',local_views.mensaje_dia),
    path('hi/',local_views.hi),
    path('mensaje/',local_views.mensaje),
    path('posts/', posts_views.list_post)



]
