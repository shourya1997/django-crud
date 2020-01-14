from django.contrib import admin
from django.urls import path, include

import employee.urls
import product.urls
from .swagger import schema_view, api_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(employee.urls, namespace='employee')),
    path('', include(product.urls, namespace='product')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

]
