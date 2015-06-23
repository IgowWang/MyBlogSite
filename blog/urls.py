from django.conf.urls import include,url


urlpatterns = [
    url(r'^$',"blog.views.blog_index",name='bloghome'),
    url(r'^article/(?P<blog_id>\d+)/$',"blog.views.content")

]
