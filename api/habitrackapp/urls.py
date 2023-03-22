from django.contrib import admin
from django.urls import path, include
from habitrackapp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("templates",
                views.TemplateViewSet,
                basename="template")


router.register("users",
                views.UserViewSet,
                basename="user")

router.register("subscriptions",
                views.SubscriptionViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('session/', views.SessionView.as_view(), name='session'),
    path('auth_user/', views.AuthUserView.as_view(), name='auth_user'),

    path('templates/subscribe/<int:template_id>/',
         views.subscribe_to_template, name='subscribe_to_template'),

]
