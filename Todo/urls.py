
from django.contrib import admin
from django.urls import path

# from .views import *
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',todo),
    path('register/',signup),
    path('todo_delete/<int:num>/',delete),
    path('',loginView),
    path('logout/',logoutView),

]
