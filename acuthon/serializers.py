from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import AcuthonRegister, Acuthon


class TeamRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acuthon
        fields = [
            'name',
            'college',
            'slug',
        ]
        read_only_fields = ['slug', ]

    def validate_name(self, value):
        team = Acuthon.objects.filter(name=value)
        if team.exists():
            raise ValidationError("Team with this name already exists")
        return value

    def create(self, validated_data):
        return Acuthon.objects.create(name=validated_data['name'], college=validated_data['college'])


class AcuthonRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_null=True, allow_blank=True)
    contact = serializers.CharField(allow_blank=True, allow_null=True)
    team = serializers.SerializerMethodField()

    class Meta:
        model = AcuthonRegister
        fields = [
            'team',
            'college',
            'member',
            'email',
            'contact',
            'rollnumber',
        ]
        read_only_fields = ['college', 'team']

    def create(self, validated_data):
        team_obj = Acuthon.objects.get(slug=self.context.get('team'))
        reg = AcuthonRegister.objects.filter(member=validated_data["member"], rollnumber=validated_data['rollnumber'])
        if reg.exists():
            registered = AcuthonRegister.objects.filter(
                team=team_obj,
                member=validated_data["member"],
                rollnumber=validated_data['rollnumber']
            )
            if registered.exists():
                raise ValidationError("Team member already exists")
            raise ValidationError("Team member already exists in some other team")
        no = AcuthonRegister.objects.filter(team=team_obj)
        if no.exists():
            return AcuthonRegister.objects.create(
                team=team_obj,
                member=validated_data['member'],
                rollnumber=validated_data['rollnumber'],
                college=team_obj.college,
            )
        return AcuthonRegister.objects.create_leader(
            team=team_obj,
            member=validated_data['member'],
            email=validated_data['email'],
            contact=validated_data['contact'],
            rollnumber=validated_data['rollnumber'],
            college=team_obj.college,
        )

    def get_team(self, obj):
        return str(obj.team.name)

