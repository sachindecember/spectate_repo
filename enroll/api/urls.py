from django.urls import path
from .import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [

     path('',views.getRoutes),
    #  path('overviewin/',views.overviewapis,name='overviewapis'),
     path('snippet-list/',views.snippetlist,name='snippetlistview'),
      path('snippet-detail/<str:pk>/',views.snippetdetail,name='snippetdetailview'),
      path('snippet-create/',views.snippetcreate,name='snippetcreatetview'),
      path('snippet-update/<str:pk>',views.snippetupdate,name='snippetupdatetview'),
      path('snippet-delete/<str:pk>',views.snippetdelete,name='snippetdeleteview'),


     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
 