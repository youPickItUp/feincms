from __future__ import absolute_import, unicode_literals

import os

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

from feincms.module.page.sitemap import PageSitemap


try:
    from django.urls import include, re_path
except ImportError:
    from django.conf.urls import include, url as re_path


sitemaps = {"pages": PageSitemap}

admin.autodiscover()

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {"document_root": os.path.join(os.path.dirname(__file__), "media/")},
    ),
    re_path(r"^sitemap\.xml$", sitemap, {"sitemaps": sitemaps}),
    re_path(r"", include("feincms.contrib.preview.urls")),
    re_path(r"", include("feincms.urls")),
]

urlpatterns += staticfiles_urlpatterns()
