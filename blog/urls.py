from django.conf.urls import include,url


urlpatterns = [
    url(r'^$',"blog.views.blog_index",name='bloghome'),
    url(r'^article/(?P<blog_id>\d+)/$',"blog.views.content",name='article'),
    url(r'^category/(?P<class_id>\d+)/$','blog.views.classification',name='category'),
    url(r'^create/$','blog.views.createArticle',name='create')


]
