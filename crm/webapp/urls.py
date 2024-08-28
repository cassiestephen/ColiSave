from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=""), # keep name same as route name (1st arg)
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout_user, name='logout'),
    path('create-horse', views.create_horse, name='create-horse'),

    # dynamic URL
    path('update-horse/<int:pk>', views.update_horse, name='update-horse'),
    path('view-horse/<int:pk>', views.view_horse, name='view-horse'),
    path('delete/<int:pk>', views.delete_horse, name='delete'),


]














