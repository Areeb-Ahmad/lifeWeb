from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('progress.urls')),
    path('typingTest/', include('typingTest.urls')),
]