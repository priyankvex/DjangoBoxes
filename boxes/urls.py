from __future__ import absolute_import

from django.conf.urls import url

from boxes.views import LoginView, CreateBoxView, UpdateBoxView, ListBoxView

urlpatterns = [
    url(r'login/', LoginView.as_view(), name="login_view"),
    url(r'create_box/', CreateBoxView.as_view(), name="create_box_view"),
    url(r'update_box/(?P<pk>[\d]+)', UpdateBoxView.as_view(), name="update_box_view"),
    url(r'boxes/', ListBoxView.as_view(), name="list_box_view"),
]
