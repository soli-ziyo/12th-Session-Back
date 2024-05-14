"""
URL configuration for blogproject project.

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
from django.urls import path

import blog.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name='home'),
    path('post/<int:post_id>', blog.views.detail, name="detail"),
    path('new/',blog.views.new,name="new"),
    path('create/',blog.views.create,name="create"),
    path('delete/<int:post_id>', blog.views.delete,name="delete"),
    path('update_page/<int:post_id>',blog.views.update_page, name="update_page"),
    path('update/<int:post_id>',blog.views.update,name="update"),
    path('<int:post_id>/comment',blog.views.add_comment,name="add_comment"),
    path('accounts/login', accounts.views.login_view, name="login"),
    path('accounts/logout', accounts.views.logout_view, name="logout"),
    path('accounts/signup', accounts.views.signup_view, name="signup"),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)