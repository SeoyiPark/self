# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 장고의 기본 회원가입 폼을 상속받아서 나만의 폼을 만듭니다.
class CustomUserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
        # 라벨(글자)을 내 마음대로 덮어씌웁니다.
        labels = {
            'username': '아이디 (문자, 숫자 조합)',
        }