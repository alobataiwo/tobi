from django.urls import path
from . import views
app_name= 'other'

urlpatterns = [
    path('simpleview/',views.simple_view,name='simpleview'),
    path('design/',views.design, name='design'),
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup, name='signup'),
    path('homeview/',views.homeview, name='homeview')
]