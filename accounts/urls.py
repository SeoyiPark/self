from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # 로그아웃은 장고의 내장 뷰를 사용하도록 덮어씌웁니다 (보안 표준)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete/', views.delete_account, name='delete_account'),
    path('profile/', views.profile, name='profile'), # 👈 마이페이지 추가!
]