from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('post',views.PostViewset)

urlpatterns = [
    path('',views.post_list,name='posts_list'),
    path('newpost/', views.post_new, name='new_post'),
    path('post/<int:id>/',views.post_view),
    path('post/<int:id>/edit',views.post_edit),
    path('post/<int:id>/delete',views.post_delete),
    path('api/',include(router.urls))
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)