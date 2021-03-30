from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.post_list,name='posts_list'),
    path('newpost/', views.post_new, name='new_post'),
    path('post/<int:id>/',views.post_view),
    path('post/<int:id>/edit',views.post_edit),
    path('post/<int:id>/delete',views.post_delete),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)