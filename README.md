# python-django-sso-example
An example Django application demonstrating how to use the [WorkOS Python SDK](https://github.com/workos-inc/workos-python) to authenticate users via SSO.

## Prerequisites
- Python 3.6+

## Setup

1. Navigate to the directory into which you want to clone this git repo.
   ```bash
   $ cd ~/Desktop/
   ```

2. Clone this git repo using your preferred secure method (HTTPS or SSH).
   ```bash
   # HTTPS
   $ git clone https://github.com/workos-inc/python-django-sso-example.git
   ```

   or

   ```bash
   # SSH
   $ git clone git@github.com:workos-inc/python-django-sso-example.git
   ```

3. Navigate to the cloned repo.
   ```bash
   $ cd python-django-sso-example
   ```

4. Create and source a Python virtual environment. You should then see `(env)` at the beginning of your command-line prompt.
   ```bash
   $ python3 -m venv env
   $ source env/bin/activate
   ```

4. Install the cloned app's dependencies.
   ```bash
   pip install -r requirements.txt
   ```

--- LEFT OFF HERE ---
1. The example app looks for the following environment variables:
    - WORKOS_API_KEY - The WorkOS API key can be found [here](https://dashboard.workos.com/api-keys).
    - WORKOS_PROJECT_ID - The WorkOS Client ID is specific to SSO and can be found [here](https://dashboard.workos.com/sso/configuration)

1. Follow the [SSO authentication flow instructions] to set up an SSO connection. The redirect URL for the example app (if you made no customizations) will be http://localhost:8000/auth/callback.

## Running the app

1. Naviagte to the `python-django-sso-example` directory, which contains the `manage.py` file. Use the following command to run the app locally:

   ```bash
   $ python3 manage.py runserver
   ```

Once running, navigate to the following URL for a demonstration on the SSO workflow: http://localhost:8000.
