from django.urls import path
from docs.views import (custom_view,Static_view,setcookie,showcookie,deletecookie,
    Docs_create_view,Docs_list_view,Docs_detail_view,Docs_update_view,Docs_delete_view
)

app_name='docs'

urlpatterns = [
    path('custom_view',custom_view),
    path('setcookie',setcookie,name='setcookie'),
    path('showcookie',showcookie),
    path('deletecookie',deletecookie),
    path('static/',Static_view,name='static_view'),
    path('docs_create',Docs_create_view,name='docs_create_view'),
    path('docs_list',Docs_list_view,name='docs_list_view'),
    path('<int:pk>/',Docs_detail_view,name='docs_detail_view'),
    path('<int:pk>/update',Docs_update_view,name='docs_update_view'),
    path('<int:pk>/delete',Docs_delete_view,name='docs_delete_view'),
]
