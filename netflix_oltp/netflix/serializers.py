from rest_framework import serializers
from .models import Content, Access, UserPlan, UserPayment, Director, Producer, Show, Movie, User, Genre, Payment, Plan, Watched, Cast, Ratings


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = "__all__"

class UserPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlan
        fields = "__all__"

class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"

class WatchedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watched
        fields = "__all__"

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = "__all__"

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = "__all__"

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"
