from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
   path('', views.home, name='home'),
   path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'app.views.custom_page_not_found_view'
handler500 = 'app.views.custom_error_view'
handler403 = 'app.views.custom_permission_denied_view'
handler400 = 'app.views.custom_bad_request_view'