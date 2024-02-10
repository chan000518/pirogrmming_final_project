from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.region.models import Region

# 유저 모델
class User(AbstractUser):
    username = models.CharField('아이디', max_length=15, null=False, unique=True)
    nickname = models.CharField('닉네임', max_length=31, null=False)
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField('이메일', max_length=255, null=False, unique=True)
    address = models.CharField(max_length=255, null=False)
    detail_address = models.CharField(max_length=255, null=True, blank=True)
    first_login = models.BooleanField(default=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    # 친구 속성 추가
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.nickname
    
    def save(self, *args, **kwargs):
        print("save!!")
        super().save(*args, **kwargs)
