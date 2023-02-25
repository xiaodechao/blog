
from django.urls import path, include, re_path
from . import views 
# from django.views.static import serve
# from web_video import settings
# from django.conf import settings
# from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls.static import static

from . import views



urlpatterns = [
    
    path('', views.Blog.as_view(), name='blog'),
    path('comment/', views.Comment.as_view(), name='comment'),
    # path('useradmin/', views.User_admin.as_view(), name='useradmin'),
    # path('article/', views.User_admin.as_view(), name='article_detail'),
    re_path(r'^article_detail/(?P<article_id>.*)/$', views.Article_detail.as_view()),
    re_path(r'^(?P<condition>.*)/(?P<param>.*)/$', views.Blog.as_view()),
    
    
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    # re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
   
    
 ] 
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  ## 没有这一句无法显示上传的图片
