from django.contrib import admin
from django.urls import path, include

"""
СПбГУ
ИТМО
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
