from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),  # ← важно!
    path('api/v1/auth/', include('djoser.urls.jwt')),  # ← эндпоинты от Djoser
    path('redoc/', include('redoc.urls')),  # ← для документации
]
