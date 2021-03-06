from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from inicio.views import login_view, logout_view

urlpatterns = patterns('', 
    url(r'^$', TemplateView.as_view(template_name='index.html'), name = 'vista_inicio'),
    url(r'^acceso_denegado/$', TemplateView.as_view(template_name='acceso_denegado.html'), name = 'vista_acceso_denegado'),
    url(r'^login/$', login_view, name = 'vista_login'),
    url(r'^logout/$', logout_view, name = 'vista_logout'),
)