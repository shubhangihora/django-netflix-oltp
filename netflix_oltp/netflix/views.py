from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ContentSerializer, AccessSerializer, UserPlanSerializer, UserPaymentSerializer, DirectorSerializer, ProducerSerializer, ShowSerializer, MovieSerializer, UserSerializer, GenreSerializer, PaymentSerializer, PlanSerializer, WatchedSerializer, CastSerializer, RatingsSerializer
from .models import Content, Access, UserPlan, UserPayment, Director, Producer, Show, Movie, User, Genre, Payment, Plan, Watched, Cast, Ratings

class AccessViewSet(ModelViewSet):
    serializer_class = AccessSerializer
    queryset = Access.objects.all()

class UserPlanViewSet(ModelViewSet):
    serializer_class = UserPlanSerializer
    queryset = UserPlan.objects.all()

class UserPaymentViewSet(ModelViewSet):
    serializer_class = UserPaymentSerializer
    queryset = UserPayment.objects.all()

class DirectorViewSet(ModelViewSet):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()

class ProducerViewSet(ModelViewSet):
    serializer_class = ProducerSerializer
    queryset = Producer.objects.all()

class ContentViewSet(ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

class ShowViewSet(ModelViewSet):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()

class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

class PlanViewSet(ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()

class WatchedViewSet(ModelViewSet):
    serializer_class = WatchedSerializer
    queryset = Watched.objects.all()

class CastViewSet(ModelViewSet):
    serializer_class = CastSerializer
    queryset = Cast.objects.all()

class RatingsViewSet(ModelViewSet):
    serializer_class = RatingsSerializer
    queryset = Ratings.objects.all()
