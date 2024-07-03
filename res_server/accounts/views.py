from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django.views.generic import ListView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from oauth2_provider.views import ProtectedResourceView


class MyEndpoint(ProtectedResourceView):
    """
    A GET endpoint that needs OAuth2 authentication
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

class UserSerializer(ModelSerializer):
    auth_user = SerializerMethodField(read_only=True)

    def get_auth_user(self, obj):
        return self.context.get('request', None).user.username

    class Meta:
        model = User
        fields = '__all__'


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CustomView(LoginRequiredMixin, ListView):
    model = User
    template_name = "accounts/custom.html"


class Dummy(RedirectView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('code', None) is not None:
            authenticate_user(request)
        return HttpResponse({'msg': 'hey'})



import requests

def exchange_code_for_token(authorization_code):
    token_endpoint = 'http://localhost:8000/o/token/'

    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'client_id': 'dL8BKNFaZyiEa0Ha9bxIBIR2WouLMmnqDyBMvCz6',
        'client_secret': 'jHyTGavbJ7WVX4LQldG7gP12BmVli1H5WQUL3jyAQWy0YU56sjbX0HeXSHYg5XhDhjlOwueaZTm3zk0fNryKcDzIGo3s9SFG5Xt9XDmvtUIqsrs5rsLPoyLWC6lLmomN',
        'code_verifier': settings.CODE_VERIFIER,
        'redirect_uri': 'http://localhost:9000/home'
    }

    response = requests.post(token_endpoint, data=data)
    print(response._content)

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        return access_token
    else:
        # Handle error response
        return None


def authenticate_user(request):
    authorization_code = request.GET.get('code')
    print(authorization_code)
    if authorization_code:
        access_token = exchange_code_for_token(authorization_code)
        if access_token:
            print(access_token)
            # Authenticate user using access token
            # You may need to decode/validate the access token and associate the user with the request
            # Example: request.user = get_user_from_access_token(access_token)
            return True
    return False
