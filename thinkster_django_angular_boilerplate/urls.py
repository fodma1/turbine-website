from django.conf.urls import include, patterns, url

from rest_framework_nested import routers

from authentication.views import AccountViewSet, LoginView, LogoutView
from thinkster_django_angular_boilerplate.views import IndexView, send_simple_message

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)

urlpatterns = patterns(
    '',

    url(r'^sendmail/', send_simple_message),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^.*$', IndexView.as_view(), name='index'),
)
