from django.db import models

class Access(models.Model):
    username = models.CharField(max_length = 255, primary_key = True)
    password = models.CharField(max_length = 255)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)

class User(models.Model):
    user_id = models.IntegerField(primary_key = True)
    user_fname = models.CharField(max_length = 255)
    user_lname = models.CharField(max_length = 255)
    user_email = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Plan(models.Model):
    plan_id = models.IntegerField(primary_key = True)
    plan_name = models.CharField(max_length = 255)
    plan_desc = models.CharField(max_length = 255)

class UserPlan(models.Model):
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    plan_id = models.ForeignKey('Plan', on_delete = models.CASCADE)
    user_plan_id = models.IntegerField(primary_key = True)

class Payment(models.Model):
    payment_id = models.IntegerField(primary_key = True)
    plan_id = models.ForeignKey('Plan', on_delete = models.CASCADE)
    payment_amount = models.IntegerField()

class UserPayment(models.Model):
    payment_id = models.ForeignKey('Payment', on_delete = models.CASCADE)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    user_payment_id = models.IntegerField(primary_key = True)

class Watched(models.Model):
    watched_id = models.IntegerField(primary_key = True)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    ratings_id = models.ForeignKey('Ratings', on_delete = models.CASCADE)

class Ratings(models.Model):
    ratings_id = models.IntegerField(primary_key = True)
    ratings = models.IntegerField()

class Content(models.Model):
    content_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 255)
    director_id = models.ForeignKey('Director', on_delete = models.CASCADE)
    release_date = models.IntegerField()
    cast_id = models.ForeignKey('Cast', on_delete = models.CASCADE)
    ratings_id = models.ForeignKey('Ratings', on_delete = models.CASCADE)
    genre_id = models.ForeignKey('Genre', on_delete = models.CASCADE)
    producer_id = models.ForeignKey('Producer', on_delete = models.CASCADE)
    time = models.IntegerField()
    show_id = models.ForeignKey('Show', on_delete = models.CASCADE)
    movie_id = models.ForeignKey('Movie', on_delete = models.CASCADE)

class Show(models.Model):
    show_id = models.IntegerField(primary_key = True)
    seasons = models.IntegerField()

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key = True)

class Genre(models.Model):
    genre_id = models.CharField(max_length = 255, primary_key = True)
    genre_name = models.CharField(max_length = 255)

class Cast(models.Model):
    cast_id = models.IntegerField(primary_key = True)
    cast_name = models.CharField(max_length = 255)

class Director(models.Model):
    director_id = models.IntegerField(primary_key = True)
    director_name = models.CharField(max_length = 255)
    director_desc = models.CharField(max_length = 255)

class Producer(models.Model):
    producer_id = models.IntegerField(primary_key = True)
    producer_name = models.CharField(max_length = 255)
    producer_desc = models.CharField(max_length = 255)
