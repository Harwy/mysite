#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

# from types import MethodType # 类动态绑定
import os

# 头像上传目录(统一头像目录)
AVATAR_ROOT = "avatar"
AVATAR_DEFAULT = os.path.join(AVATAR_ROOT, 'default_64.png')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default="", verbose_name='昵称')
    userimg = models.ImageField(upload_to="user_img/%Y/%m/%d", null=True, blank=True, default=AVATAR_DEFAULT, verbose_name='头像')
    # avatar = models.ImageField(upload_to=AVATAR_ROOT, default=AVATAR_DEFAULT)

    def __str__(self):
        return '<Profile>: %s for %s' % (self.nickname, self.user.username)

    class Meta:
        verbose_name = '昵称库'
        verbose_name_plural = verbose_name


def get_userimg(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.userimg
    else:
        return AVATAR_DEFAULT


# 动态绑定nickname
def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ''


def get_nickname_or_username(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return self.username


def has_nickname(self):
    return Profile.objects.filter(user=self).exists()


'''
# 动态绑定头像方法
def get_avatar_url(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.avatar
    else:
        return AVATAR_DEFAULT
'''

# User.get_avatar_url = get_avatar_url
User.get_userimg = get_userimg
User.get_nickname = get_nickname
User.has_nickname = has_nickname
User.get_nickname_or_username = get_nickname_or_username
