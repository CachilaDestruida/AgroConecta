from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register/', views.registerPage),
    path('logout/', views.logoutPage),
    path('login/', views.loginPage),
    path('acerca/', views.acerca),
    path('agregarproducto/', views.agregarproducto),
    
]