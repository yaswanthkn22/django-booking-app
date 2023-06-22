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
    path('house/<int:houseId>/', views.houseDetails, name='house-details'),
    path('house/booking/<int:houseId>/', views.bookings, name='house-booking'),
    path('bookings/login/', views.customerLogin, name='booking-login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
