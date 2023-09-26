from django.urls import path
from .views import *
urlpatterns = [
   path('', loginUserView, name='loginUser'),
   path('logout/', logoutuserview, name='logoutuser'),
   path('regUser/', regUserView, name='regUser'),
   path('login/', loginUserView, name='loginuser'),
]