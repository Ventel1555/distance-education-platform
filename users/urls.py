from django.urls import path

from .views import MyLoginView, logout_view


urlpatterns =[
    path('login/', MyLoginView.as_view(), name='login_view'),
    path('logout/', logout_view, name='logout_view')
    # path('singup/', LogoutView.as_view(), name='singup_view'),
]