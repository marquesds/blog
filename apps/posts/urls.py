from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PostList, PostDetail

urlpatterns = [
    url(r'^posts/$', PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
