import os
import workos

from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse


workos.api_key = os.getenv('WORKOS_API_KEY')
workos.project_id = os.getenv('WORKOS_PROJECT_ID')
workos.base_api_url = 'http://localhost:8000/' if settings.DEBUG else workos.base_api_url

'''
In the real world, users will be signing in with email addresses that have
different domains, and some users will be using SSO while some will not.
This example assumes only users with workos.com domains are signing in,
and are doing so with SSO.
'''

WORKOS_CUSTOMER_EMAIL_DOMAIN = 'workos.com'


def login(request):
    return render(request, 'sso/login.html')


def auth(request):
    authorization_url = workos.client.sso.get_authorization_url(
        WORKOS_CUSTOMER_EMAIL_DOMAIN,
        reverse('auth_callback'),
        state={}
    )

    return redirect(authorization_url)


def auth_callback(request):
    code = request.args.get('code')
    profile = client.sso.get_profile(code)

    return profile.to_dict()
