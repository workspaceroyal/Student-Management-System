from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
                path('admin/', admin.site.urls),
                path('base/', views.BASE, name='base'),

                # Login Path
                path('', views.LOGIN, name='login'),
                path('doLogin',views.doLogin,name='doLogin'),

                path('doLogout',views.doLogout,name='logout'),

                # Hod Panel Path
                path('Hod/Home',Hod_Views.HOME,name='hod_home'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
