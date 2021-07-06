from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('main.urls')),
    re_path(r'^(?:.*)/?$', include('main.urls'))
    # path('confirm/<uidb64>/<token>', email_confirmation, name="confirm")
]
