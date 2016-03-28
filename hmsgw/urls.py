from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
from hmsapp.models import Patient,Physician
admin.autodiscover()

from rest_framework import permissions, routers, serializers, viewsets, generics
from rest_framework import filters

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


# first we define the serializersn
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient

class PhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physician

# ViewSets define the view behavior.
class PhysicianViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Physician.objects.all()
    serializer_class = PhysicianSerializer


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


#class PatientViewSearch(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#    queryset = Patient.objects.all()
#    serializer_class = PatientSerializer
#    filter_backends = (filters.SearchFilter,)
#    search_fields = ('first_name')

class PatientViewName(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = PatientSerializer

    def get_queryset(self):
        xfirst_name = self.kwargs['first_name']
        return Patient.objects.filter(first_name=xfirst_name)

class PatientViewID(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = PatientSerializer

    def get_queryset(self):
        xid = self.kwargs['id']
        return Patient.objects.filter(pk=xid)

class PhysicianViewName(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = PatientSerializer

    def get_queryset(self):
        xfirst_name = self.kwargs['first_name']
        return Patient.objects.filter(first_name=xfirst_name)

class PhysicianViewID(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = PatientSerializer

    def get_queryset(self):
        xid = self.kwargs['id']
        return Patient.objects.filter(pk=xid)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()

    #username = request.query_params.get('name', None)
    #if username is not None:
#        queryset = queryset.filter(patient__first_name=username)

    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'physicians', PhysicianViewSet)
#router.register(r'patientssearch', PatientViewSearch)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),

    # Filtering Method
    url('^patients/name/(?P<first_name>.+)/$', PatientViewName.as_view()),
    url('^patients/id/(?P<id>.+)/$', PatientViewID.as_view()),
    url('^physicians/name/(?P<first_name>.+)/$', PhysicianViewName.as_view()),
    url('^physicians/id/(?P<id>.+)/$', PhysicianViewID.as_view()),


    # Users login
    url(r'^oauthClient/', include('oauthClient.urls')),

)
