from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from views import ItemList, ItemDetail

urlpatterns = patterns('',
    url(r'^root/', ItemList.as_view()),
    url(r'^detail/', ItemDetail.as_view()),

)

# # Format suffixes
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
#
# # Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
