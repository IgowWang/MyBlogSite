from django.conf.urls import include,url


urlpatterns = [
    url(r'^$',"blog.views.blog_index",name='bloghome')
]
