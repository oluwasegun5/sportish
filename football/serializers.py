from rest_framework import serializers
from .models import *


class HostSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = Host
        fields = ['user', "organization", "profile_picture"]


class ManagerSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = Manager
        fields = ['user', "organization", "profile_picture"]


class TeamSerializer(serializers.ModelSerializer):
    manager = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='manager-detail'
    )

    class Meta:
        model = Team
        fields = ["teamName", "teamLogo", "date_created",
                  "manager"]


class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )
    team = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='team-detail'
    )

    class Meta:
        model = Player
        fields = ['user', 'organization', 'country',
                  'role', 'height', 'strong_foot', 'picture', 'team']


class CompetitionSerializer(serializers.ModelSerializer):
    host = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='host-detail'
    )

    class Meta:
        model = Competition
        fields = ["host", "competition_name", "minutes", "venue",
                  "competition_info", "competition_logo", "date_created",
                  "organization"]


####################################################
class HostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['user', "organization", "profile_picture"]


class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['user', 'organization', 'country',
                  'role', 'height', 'strong_foot', 'picture', 'team']


class ManagerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['user', "organization", "profile_picture"]


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["teamName", "teamLogo", "date_created",
                  "manager"]


class CompetitionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ["host", "competition_name", "minutes", "venue",
                  "competition_info", "competition_logo", "date_created",
                  "organization"]
