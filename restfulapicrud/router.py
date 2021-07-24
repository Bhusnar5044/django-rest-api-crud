from employeeapi.viewsets import EmployeeViewset, DocumentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)
router.register('document',DocumentViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive