from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    # path((r'^accounts/login/$', VIEW),)
    # path(r'^accounts/login/$', 'django.contrib.auth.views.login'),
]
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
