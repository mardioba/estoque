
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('projeto.core.urls')),
    path('produto/', include('projeto.produto.urls')),
    path('admin/', admin.site.urls),
]
