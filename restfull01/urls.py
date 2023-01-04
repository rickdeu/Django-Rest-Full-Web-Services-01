from django.contrib import admin
from django.urls import path, include
from toys import urls as toy_url
from drones import urls as drone_url
from rest_framework.documentation import include_docs_urls #api documentation

API_TITLE = 'DRONES API' # new
API_DESCRIPTION = 'A WEB API FOR DRONES.'



urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('toys/', include(toy_url)),
    #path('drones/', include(drone_url)),
    path('api/', include(drone_url)),
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
