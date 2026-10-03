from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.urls import include, path

from portfolio.sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}

# ==========================================
# ROBOTS.TXT
# ==========================================

def robots_txt(request):

    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]

    return HttpResponse(
        "\n".join(lines),
        content_type="text/plain"
    )


# ==========================================
# URLS
# ==========================================

urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        include("portfolio.urls")
    ),

    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": sitemaps
        },
        name="sitemap"
    ),

    path(
        "robots.txt",
        robots_txt,
        name="robots_txt"
    ),

]


# ==========================================
# MEDIA FILES
# ==========================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )