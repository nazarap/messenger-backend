from django.conf.urls import url
from api import views as local_views
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    url(r'^user/login/$', local_views.LoginViewSet.as_view({'post': 'user_login'})),
    url(r'^user/create/$', local_views.LoginViewSet.as_view({'post': 'create_user'})),

    # Session Login
    url(r'^user/auth/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),

    url(r'^user/data/$', local_views.UserViewSet.as_view({'post': 'user_by_token'})),
    url(r'^user/update/$', local_views.UserViewSet.as_view({'post': 'user_data_update'})),

    # Contacts request
    url(r'^contacts/$', local_views.ContactViewSet.as_view({'get': 'get_contacts_by_user'})),
    url(r'^friends/$', local_views.FriendViewSet.as_view({'get': 'get_user_friends'})),
    url(r'^messages/(?P<user_id>[0-9]+)/$', local_views.MessageViewSet.as_view({'get': 'get_messages_by_user'})),
    url(r'^send/message/$', local_views.MessageViewSet.as_view({'post': 'send_message'})),

    url(r'^find/users/$', local_views.UserViewSet.as_view({'post': 'find_user_by_name'})),
    url(r'^find/contacts/$', local_views.ContactViewSet.as_view({'post': 'find_contacts_by_name'})),
]
