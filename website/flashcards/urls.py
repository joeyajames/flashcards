# flashcards URLs
from flashcards import views
from django.urls import re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'flashcards'

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	re_path(r'^(?P<flashcard_id>[0-9]+)/$', views.detail, name='detail'),
	re_path(r'^fc_import/$', views.fc_import, name='fc_import'),
	re_path(r'^listview/', views.FlashcardList.as_view()),
	re_path(r'^my_flashcards/$', views.my_flashcards, name='my_flashcards'),
	
]
urlpatterns += staticfiles_urlpatterns()