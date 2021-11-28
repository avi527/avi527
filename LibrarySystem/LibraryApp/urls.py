from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('createbook', views.CreateBook,name='createbook'),
    path('CreateLibraries', views.CreateLibraries,name='CreateLibraries'),
    path('CreateLibraryBookRecord', views.CreateLibraryBookRecord,name='CreateLibraryBookRecord'),
    path('CreateLibraryCheckInOut', views.CreateLibraryCheckInOut,name='CreateLibraryCheckInOut'),
    path('LibraryBookOutFromUser', views.LibraryBookOutFromUser,name='LibraryBookOutFromUser'),
    path('AllBookOutFromLib', views.AllBookOutFromLib,name='AllBookOutFromLib'),

]