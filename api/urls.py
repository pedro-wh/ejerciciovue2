

from api.views import ColumnAPI, TodoAPI
from rest_framework import routers


router = routers.SimpleRouter()
router.register("columns", ColumnAPI)
router.register("todos", TodoAPI)

urlpatterns = [

]

urlpatterns += router.urls