from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views
urlpatterns = [
    path('index/',views.index, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('locations',views.locations, name='locations'),
    path('register',views.register, name='register'),
    path('',views.loginuser, name='login'),
    path('logout',views.logoutuser,name="logout"),
    path('reg', views.reg, name='reg'),
     path('itenary',views.itenary, name='itenary'),
# path('enquiry/', views.enquiry_view, name='enquiry'),
#     path('thank-you/', views.thank_you, name='thank_you'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
