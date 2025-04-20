from django.contrib import admin
from django.urls import path
from .views import signup,   signin, signout, test

app_name = 'core'

urlpatterns = [
    path('api/signup', signup, name='signup'),
    path('api/signin', signin, name='signin'),
    path('api/signout', signout, name='signout'),
    path('api/test', test, name='test' )
]
