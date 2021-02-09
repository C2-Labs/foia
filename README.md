# FOIA Demo Site

This site is used for customer demonstration of a Django-based architecture for re-imagining the Freedom of Information Act (FOIA) application hosted by the Environmental Protection Agency (EPA).

# Pre-Requisites

- Python 3.8 or greater
- Django - `pipenv install django~=3.1.6`
- pipenv
- git
- awscli
- ebcli
    - Install instructions for Mac:

    ```
    brew update
    brew install awsebcli
    eb --version
    ```

# Design

- [Leverages the US Web Design System (USWDS)](https://designsystem.digital.gov/)

# Managing the Virtual Environment (Running locally)

- Edit `config/settings.py` and comment out the following lines:

    ```
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    ```

    - Make sure `Debug = True`
- Start the virtual environment shell with `pipenv shell`
- Collect the static files: `python manage.py collectstatic`
- Run the application/server with  `python manage.py runserver`
- Stop the application with CTRL + C
- Exit the virtual environment with `exit`

# Database Migrations

- Create a migration with `python manage.py makemigrations app_name`
- Apply a migration with `python manage.py migrate`

# Create the God Mode Account

- `python manage.py createsuperuser`

# Hosting 

- Target environment is [Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) 
- Backend DB is Postgres in AWS RDS

# Deploying
This app is deployed on Elastic Beanstalk with an S3 bucket holding the static files. You will need to obtain the proper SSL keypair (` aws-eb`) to deploy.

After testing and ready for deployment, do the following:

- Ensure you have uncommented the lines to allow the static files to work with the S3 bucket in the `config/settings.py` file:

    ```
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    ```
- Create AWS credentials to login
    - Console
    - Click on your username
    - My Security Credentials
    - Create Access Key
- Update credentials with AWS CLI
    - `aws configure` OR
    - Update your `~/.aws/credentials` file
- Commit your code locally (you don't have to push, but you *DO* have to commit)
- Run `eb deploy`. This will take 5+ minutes to deploy to AWS. This deploy is doing the following:
    - Copying files to the beanstalk bucket
    - Creating the necessary migrations in the beanstalk container
    - Running the migrations in the beanstalk container
    - Collecting the static files in the beanstalk container and copying them to the S3 bucket
    - Updating the environment and deploying the app
