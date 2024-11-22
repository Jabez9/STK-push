from django.urls import path
from . import views 

# appname = 'stk'

urlpatterns = [
    path('',views.home,name = 'home'),
    path('stk_push/',views.stk_push, name= 'stk_push'),
    path('thanks/',views.thank_you, name='thanks'),
    path('error/',views.stk_error, name = 'error')
]