from rest_framework import serializers
from .models import Login_User

# normal serializer
# class Login_User_Serializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField()
#     phone_no=serializers.IntegerField()
    
#model serializer
class Login_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Login_User
        fields=['id','first_name','last_name','email','password','phone_no']