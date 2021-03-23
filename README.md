# python-django-sso-example
An example Django application demonstrating how to use the [WorkOS Python SDK](https://github.com/workos-inc/workos-python) to authenticate users via SSO.

## Prerequisites
- Python 3.6+


## Django Project Setup

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

5. Install the cloned app's dependencies.
   ```bash
   (env) $ pip install -r requirements.txt
   ```

6. Obtain and make note of the following values. In the next step, these will be set as environment variables.
   - Your [WorkOS API key](https://dashboard.workos.com/api-keys)
   - Your [SSO-specific, WorkOS Project ID](https://dashboard.workos.com/sso/configuration)

7. Ensure you're in the root directory for the example app, `python-django-sso-example/`. Create a `.env` file to securely store the environment variables. Open this file with the Nano text editor.
   ```bash
   (env) $ touch .env
   (env) $ nano .env
   ```

8. Once the Nano text editor opens, you can directly edit the `.env` file by listing the environment variables:
   ```bash
   export WORKOS_API_KEY=<value found in step 6>
   export WORKOS_PROJECT_ID=<value found in step 6>
   ```

   To exit the Nano text editor, type `CTRL + x`. When prompted to "Save modified buffer", type `Y`, then press the `Enter` or `Return` key.

9. Source the environment variables so they are accessible to the operating system.
   ```bash
   (env) $ source .env
   ```

   You can ensure the environment variables were set correctly by running the following commands. The output should match the corresponding values.
   ```bash
   (env) $ echo $WORKOS_API_KEY
   (env) $ echo $WORKOS_PROJECT_ID
   ```

10. The final setup step is to start the server. Again, ensure you're in the `python-django-sso-example/` directory where the `manange.py` file is.
   ```bash
   (env) $ python3 manage.py runserver
   ```

   You'll know the server is running when you see no warnings or errors in the CLI, and output similar to the following is displayed:

   ```bash
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).
   March 18, 2021 - 04:54:50
   Django version 3.1.7, using settings 'workos_django.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.
   ```

   Navigate to `localhost:8000`. You should see a "Login" link. If you click on this link, you'll be redirected to an HTTP `404` page because we haven't set up SSO yet!

   You can stop the local Django server for now by entering `CTRL + c` on the command line.


## SSO Setup with WorkOS

Follow the [SSO authentication flow instructions](https://workos.com/docs/sso/guide/introduction) to set up an SSO connection. If you get stuck, reach out to us at support@workos.com so we can help. The redirect URL for the example app will be http://localhost:8000/auth/callback.

## Testing the Integration

1. Naviagte to the `python-django-sso-example` directory, which contains the `manage.py` file. Source the virtual environment we created earlier. Start the Django server locally.

   ```bash
   $ cd ~/Desktop/python-django-sso-example/
   $ source env/bin/activate
   (env) $ python3 manage.py runserver
   ```

   Once running, navigate to http://localhost:8000 to test out the SSO workflow.

   Hooray!

## Need help?

If you get stuck and aren't able to resolve the issue by reading our API reference or tutorials, you can reach out to us at support@workos.com and we'll lend a hand.
