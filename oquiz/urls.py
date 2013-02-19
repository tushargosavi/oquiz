from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from quiz.views import main_page, user_page, logout_page, register_page
from quiz.views import question_save_page, tag_page, tag_cloude_page

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', direct_to_template,
     { 'template' : 'registration/register_success.html' }),
    (r'^question/add/$', question_save_page),
    (r'^tag/([^\s]+)/$', tag_page),
    (r'^tag/$', tag_cloude_page),
    # Examples:
    # url(r'^$', 'oquiz.views.home', name='home'),
    # url(r'^oquiz/', include('oquiz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
