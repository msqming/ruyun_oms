from django.urls import path

from auth_mage import views

urlpatterns = [
    path('', views.LoginAuth.as_view()),
    path('logout/', views.Logout.as_view()),

    path('index/', views.Index.as_view()),

]
