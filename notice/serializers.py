# notice/serializers.py
"""
Serializer 작성.

공지사항 정보를 받아올때 유저 상세 정보도 받아오도록 설정한다.
"""
from rest_framework import serializers
from .models import Notice
from accounts.serializers import UserInfoSerializer


class NoticeSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True) # 유저 정보를 가져온다 !

    class Meta:
        model = Notice
        fields = '__all__'