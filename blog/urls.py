from django.urls import path
from . import views
from django.conf.urls.static import static
from mysite.settings.base import MEDIA_ROOT, MEDIA_URL

# start with blog
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    # http://localhost:8000/blog/1
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
    path('date/<int:year>/<int:month>', views.blogs_with_date, name="blogs_with_date"),
    path('timeline', views.blog_timeline, name="blog_timeline"),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
