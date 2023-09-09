from rest_framework import routers
from .api import ProductViewSet,ClientViewSet,RolesViewset,CollaboratorViewSet,SalesViewSet,SalesDetailViewSet

router = routers.DefaultRouter()

router.register('api/products', ProductViewSet, 'products')
router.register('api/Clients', ClientViewSet, 'clients')
router.register('api/Roles',RolesViewset, 'roles')
router.register('api/Collaborators',CollaboratorViewSet, 'collab')
router.register('api/Sales',SalesViewSet, 'sale')
router.register('api/SalesDetails',SalesDetailViewSet, 'saleDetails')


urlpatterns = router.urls
