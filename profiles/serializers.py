from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password as default_validate_password
from django.db.models import Q
from profiles.models import Profile

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email_id',
            'roll_number',
            'department',
            'year',
            'contact',
            'password',
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data['username']
        email_id = validated_data['email_id']
        roll_number = validated_data['roll_number']
        department = validated_data['department']
        contact = validated_data['contact']
        year = validated_data['year']
        password = validated_data['password']
        validuser = User.objects.filter(username=username)
        user_obj = User(
            username=username,
            email_id=email_id,
            roll_number=roll_number,
            department=department,
            contact=contact,
            year=year,
        )
        user_obj.is_mentor = False
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

    def validate_username(self, value):
        user = User.objects.filter(username=value)
        if user.exists():
            raise ValidationError("User with username "+value+" already exists")

    def validate_email_id(self, value):
        user = User.objects.filter(email_id=value)
        if user.exists():
            raise ValidationError("User with email_id "+value+" already exists")


class UserModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email_id',
            'roll_number',
            'department',
            'year',
            'contact',
        ]


class UserLoginSerializer(serializers.ModelSerializer):
    id_field = serializers.CharField(label='Username or Email or Mobile number')
    password = serializers.CharField(label='Password')

    class Meta:
        model = User
        fields = [
            'id_field',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        id_field = data.get("id_field").casefold()
        password = data.get("password").casefold()
        if id_field and password:
            user_obj = Profile.objects.filter(
                                Q(username__iexact=id_field) |
                                Q(email_id__iexact=id_field) |
                                Q(contact__iexact=id_field)
                            ).distinct()
            if user_obj.exists() and user_obj.count() == 1:
                user_object = user_obj.first()
                user = authenticate(username=user_object.username, password=password)
                if user:
                    data["user"] = user
                else:
                    raise ValidationError("Username or password is incorrect")
        else:
            raise ValidationError("Both fields must be provided")
        return data

    def validate_id_field(self, value):
        if value:
            user_obj = Profile.objects.filter(
                                Q(username__iexact=value) |
                                Q(email_id__iexact=value) |
                                Q(contact=value)
                            ).distinct()
            if user_obj.exists() and user_obj.count() == 1:
                return value
            else:
                raise ValidationError("Username or Email or Mobile Number does not exist")


class UserPasswordChangeSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=30)
    confirm_password = serializers.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = [
            'old_password',
            'password',
            'confirm_password',
        ]

    def validate_password(self, value):
        default_validate_password(value)
        return value

    def validate_confirm_password(self, value):
        data = self.get_initial()
        password = data.get("password")
        confirm_password = value
        if confirm_password != password:
            raise ValidationError("Passwords don't match")
        return value


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email_id',
            'roll_number',
            'department',
            'year',
            'contact',
        ]
