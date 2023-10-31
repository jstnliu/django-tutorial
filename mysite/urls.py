"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#  STEP 3
#  insert an 'include()' in the django.urls pattern
#  'include()' function allows referencing other URLconfs
#  it will 'include' whatever parts match and send the 
#  remainder to the proper URLconf for further processing 
from django.urls import include, path

urlpatterns = [
    # localhost:8000/polls/
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

#  now that we have completed the routing, we can create our models in 'polls/models.py'
