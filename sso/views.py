import os

import workos

from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse


workos.api_key = os.getenv('WORKOS_API_KEY')
workos.project_id = os.getenv('WORKOS_PROJECT_ID')

# In workos_django/settings.py, you can use DEBUG=True for local development,
# but you must use DEBUG=False in order to test the full authentication flow
# with the WorkOS API.
workos.base_api_url = 'http://localhost:8000/' if settings.DEBUG else workos.base_api_url


def login(request):
    return render(request, 'sso/login.html')


def auth(request):

    CUSTOMER_EMAIL_DOMAIN = 'gmail.com'  # Change this to match your email domain
    REDIRECT_URI = 'http://localhost:8000/auth/callback'
    authorization_url = workos.client.sso.get_authorization_url(
        CUSTOMER_EMAIL_DOMAIN,
        REDIRECT_URI,
        state={}
    )
    return redirect(authorization_url)


def auth_callback(request):
    code = request.args.get('code')
    profile = client.sso.get_profile(code)

    return profile.to_dict()
