from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    path('',views.index, name='home'),
    path('login/',views.customerLogin, name='app-login'),
    path('signup/',views.signup, name='app-signup'),
    path('logout/', views.customerLogout, name='app-logout'),
    path('house-register/login/', views.customerLogin, name='login-register'),
    path('house-register/', views.houseReg, name='house-register'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
