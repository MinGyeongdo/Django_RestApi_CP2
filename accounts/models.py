# accounts/model.py

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, name, gender, password=None ):
        if not email:
            raise ValueError('이메일 입력하세요!')
        
        
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,    
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password, gender):
        user = self.create_user(
            email,
            name=name,
            gender=gender,
            password=password,            
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # ( db에저장될이름, 선택사항 )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )
    # 수정필.. Superuser 생성시에 gender입력을 요구하는데, admin은 필요없게 구현하고 싶음.
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','gender']
    
    

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None): # True를 반환하여 권한이 있음을 알림
        return True

    def has_module_perms(self, app_label): # True를 반환하여 주어진 APP의 모델에 접근 가능하도록 함
        return True

    @property
    def is_staff(self): # True를 받아오면 장고의 관리자 화면에 로그인이 가능해짐.
        return self.is_admin
    
    class Meta:
        db_table = 'user' # 테이블명을 user로 설정