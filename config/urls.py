from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render  

def home(request):
    return render(request, 'index.html')  

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include core app routes at root level
    path('', include('core.urls')),  

    # (Optional) keep API-specific routes under /api/ if needed
    # path('api/', include('core.urls')),

    # Home page
    path('', home, name='home'),
]
