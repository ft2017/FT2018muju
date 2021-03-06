from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # path(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    path('dev', views.indexDev, name='indexDev'),
    path('muju/<int:muju_id>/', views.detail, name='detail'),
    path('schedula', views.schedula, name='schedula'),
    # path(r'^accounts/login/$', views)
]
    #path('index_old', views.index_old, name='index_old'),

     #ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),

    # path('<int:muju_wo>/', views.index_old, name='index_old'),
    # ex: /polls/5/results/
   # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
   # path('<int:question_id>/vote/', views.vote, name='vote'),
