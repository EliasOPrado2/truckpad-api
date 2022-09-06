from django.urls import include, path
from rest_framework_nested import routers

from core.api.viewsets import (
    DestinationCoordinateViewSet,
    OriginCoordinateViewSet,
    TruckDriverViewSet,
) 

app_name = 'core'

router = routers.DefaultRouter()
router.register(r"origins", OriginCoordinateViewSet, basename="origins")
router.register(r"destinations", DestinationCoordinateViewSet, basename="destinations")
router.register(r"truck-drivers", TruckDriverViewSet, basename="truck-drivers")

destination_routers = routers.NestedSimpleRouter(
    router, r"truck-drivers", lookup="truckdrivers"
)

destination_routers.register(
    r"destinations", DestinationCoordinateViewSet, basename="destinations"
)

origin_routers = routers.NestedSimpleRouter(
    router, r"truck-drivers", lookup="truckdrivers"
)

origin_routers.register(
    r"origins", OriginCoordinateViewSet, basename="origins"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(destination_routers.urls)),
    path("", include(origin_routers.urls)),
    # path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]