from django.contrib import admin
from django.urls import path
from APP.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index),
    path('home/', index2),
    path('about/', about),
    path('contact/', contact),
    path('ITGO/', ITGO),
    path('ITGOContact/', ITGOContact),
    path('ITGOGames/', ITGOGames),
    path('ITGOGContact/', ITGOGContact),
    path('ITGOabout/', ITGOabout),
    path('zakaz/', zakaz),
    path('aboutITGOGames/', AGOG),
    path('AllGame/', allGame),
    path('DownloadLiam/', DownloadLiam),
    path('recognize/', Uzn),
    path('checkout/', withdrawal_notice_form, name='withdrawal_notice_form'),  # Добавлено имя
    path('android_download/', android_download),
    path('linux_download/', linux_download),
    path('windows_download_zip/', windows_download_zip),
    path('windows_download_exe/', windows_download_exe),
    path('mac_download/', mac_download),
    path('admin/', admin.site.urls),
]