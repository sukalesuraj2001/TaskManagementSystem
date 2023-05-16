from django.urls import path
from mytask import views




urlpatterns = [

      path("",views.home),
      path("addtask",views.addtask),
      path("alltask/<sv>",views.alltask),
      path("pending/<sv>",views.pending),
      # path("completed",views.alltask),
      # path("completed",views.completed),
      path("viewtask",views.viewtask),
      path("deletetask/<rid>",views.deletetask),
      path("edittask/<rid>",views.edittask),
      path("register",views.user_register),
      path("login",views.user_login),
      path("logout",views.user_logout),
      
  
]