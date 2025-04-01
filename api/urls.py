

from api.views import ColumnAPI
from rest_framework import routers


router = routers.SimpleRouter()
router.register("columns", ColumnAPI) #AQUIIII

urlpatterns = [

]

urlpatterns += router.urls