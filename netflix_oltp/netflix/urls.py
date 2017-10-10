from rest_framework.routers import SimpleRouter
from .views import ContentViewSet, AccessViewSet, UserPlanViewSet, UserPaymentViewSet, DirectorViewSet, ProducerViewSet, ShowViewSet, MovieViewSet, UserViewSet, GenreViewSet, PaymentViewSet, PlanViewSet, WatchedViewSet, CastViewSet, RatingsViewSet

router =  SimpleRouter()
router.register("access", AccessViewSet)
router.register("userplans", UserPlanViewSet)
router.register("userpayments", UserPaymentViewSet)
router.register("directors", DirectorViewSet)
router.register("producers", ProducerViewSet)
router.register("content", ContentViewSet)
router.register("shows", ShowViewSet)
router.register("movies", MovieViewSet)
router.register("users", UserViewSet)
router.register("genres", GenreViewSet)
router.register("payments", PaymentViewSet)
router.register("plans", PlanViewSet)
router.register("watched", WatchedViewSet)
router.register("cast", CastViewSet)
router.register("ratings", RatingsViewSet)
urlpatterns = router.urls
