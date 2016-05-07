from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
import main.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main.views.index, name="index"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
