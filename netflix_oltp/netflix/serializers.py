from rest_framework import serializers
from .models import Content, Access, UserPlan, UserPayment, Director, Producer, Show, Movie, User, Genre, Payment, Plan, Watched, Cast, Ratings


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ('show_id', 'seasons')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id')

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('content_id', 'name', 'director_id', 'release_date', 'cast_id', 'ratings_id', 'genre_id', 'producer_id', 'time', 'show_id', 'movie_id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = ('user_id', 'password', 'username')

class UserPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlan
        fields = "__all__"

class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = ('user_id', 'payment_id', 'user_payment_id')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_id','genre_name', 'show_id', 'movie_id')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_id', 'plan_id', 'payment_amount')

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"

class WatchedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watched
        fields = ('watched_num', 'user_id')

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ('cast_id', 'cast_name')

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('ratings_id', 'user_id', 'ratings')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('director_id', 'director_name', 'director_desc')

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ('producer_id', 'producer_name', 'producer_desc')
