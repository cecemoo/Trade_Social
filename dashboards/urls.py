from django.urls import path
from . import views

urlpatterns = [
    # category crud
    path("", views.dashboard, name="dashboard"),
    path("categories/", views.categories, name="categories"),
    path("categories/add/", views.add_category, name="add_category"),
    path("categories/edit/<int:id>/", views.edit_category, name="edit_category"),
    path("categories/delete/<int:id>/", views.delete_category, name="delete_category"),
    # blgo post crud
    path("posts/", views.posts, name="posts"),
    path("posts/add/", views.add_post, name="add_post"),
    path("posts/edit/<int:id>/", views.edit_post, name="edit_post"),
    path("posts/delete/<int:id>/", views.delete_post, name="delete_post"),
    # users
    path("users/", views.users, name="users"),
    path("users/add/", views.add_user, name="add_user"),
    path("users/edit/<int:id>/", views.edit_user, name="edit_user"),
    path("users/delete/<int:id>/", views.delete_user, name="delete_user"),
]
