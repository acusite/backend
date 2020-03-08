from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import AcuthonRegister, Acuthon


class AcuthonRegisterSerializer(serializers.ModelSerializer):
    team = serializers.CharField(max_length=100)
    email = serializers.EmailField(allow_null=True, allow_blank=True)
    contact = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = AcuthonRegister
        fields = [
            'team',
            'member',
            'email',
            'contact',
            'rollnumber',
        ]

    def create(self, validated_data):
        team, created = Acuthon.objects.get_or_create(name=validated_data['team'])
        reg = AcuthonRegister.objects.filter(team=team, member=validated_data["member"])
        if reg.exists():
            raise ValidationError("Team member already exists")
        no = AcuthonRegister.objects.filter(team=team)
        if no.exists():
            return AcuthonRegister.objects.create(
                team=team,
                member=validated_data['member'],
                rollnumber=validated_data['rollnumber'],
            )
        return AcuthonRegister.objects.create_leader(
            team=team,
            member=validated_data['member'],
            email=validated_data['email'],
            contact=validated_data['contact'],
            rollnumber=validated_data['rollnumber']
        )



