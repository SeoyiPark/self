from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserSignupForm
# 기본 메인 페이지
def home(request):
    return render(request, 'anime/home.html')

def signup(request):
    if request.method == 'POST':
        # UserCreationForm 대신 CustomUserSignupForm 사용
        form = CustomUserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        # 여기도 CustomUserSignupForm 사용
        form = CustomUserSignupForm()
        
    return render(request, 'accounts/signup.html', {'form': form})

# 로그아웃 기능 (최신 장고 버전에서는 보안상 뷰를 분리하는 것이 좋습니다)
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def delete_account(request):
    # 사용자가 탈퇴 확인 페이지에서 "정말 탈퇴하기"를 누르면 (POST)
    if request.method == 'POST':
        user = request.user
        user.delete()  # DB에서 유저 데이터 삭제 (관련 세션도 자동 종료됨)
        return redirect('/')  # 탈퇴 후 메인 페이지로 이동
        
    # 처음 탈퇴 페이지에 접속했을 때 (GET) 확인 화면 보여주기
    return render(request, 'accounts/delete_confirm.html')

@login_required
def profile(request):
    # 로그인한 유저의 정보(request.user)를 화면으로 넘겨줍니다.
    return render(request, 'accounts/profile.html')