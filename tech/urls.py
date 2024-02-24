from django.urls import path
from . import views

urlpatterns= [
   path('', views.home, name="home"), 
   path('info/<int:pk>', views.info, name= "info"),
   path('add-project', views.AddProject.as_view(), name="add-project"),
   path('edit-project/<int:pk>', views.EditProject.as_view(), name="edit-project"),
   path('delete-project/<int:pk>', views.DelProject.as_view(), name="delete-project"),
   path('edit-profile/<int:pk>', views.EditProfile.as_view(), name="edit-profile"),
   path('add-blog/', views.AddBlog.as_view(), name= "add-blog"),
   path('edit-blog/<int:pk>', views.EditBlog.as_view(), name= "edit-blog"),
   path('del-blog/<int:pk>', views.DeleteBlog.as_view(), name= "del-blog")
]
