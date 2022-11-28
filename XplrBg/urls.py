from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('XplrBg.common.urls')),
    path('accounts/', include('XplrBg.accounts.urls')),
    path('locations/', include('XplrBg.locations.urls')),
    path('posts/', include('XplrBg.posts.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
