from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ItemList

urlpatterns = [
    url(r'^items/', ItemList.as_view()),
]

# # Format suffixes
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
#
# # Default login/logout views
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
