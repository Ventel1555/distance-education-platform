from django.urls import path

from .views import MyLoginView
from django.contrib.auth.views import LogoutView 


urlpatterns =[
    path('login/', MyLoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(next_page='login_view'), name='logout_view'),
    # path('singup/', LogoutView.as_view(), name='singup_view'),
]