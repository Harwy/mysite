from django.urls import path
from . import views
from django.conf.urls.static import static
from mysite.settings.base import MEDIA_ROOT, MEDIA_URL


# start with file
urlpatterns = [
    path('file_list/', views.file_list, name="file_list"),
    path('upload_file/', views.upload_file, name="upload_file"),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)