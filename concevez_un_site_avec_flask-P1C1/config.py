import os

# Database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    # Nouvelle base de données pour les tests.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')
    # id de l'app TEST
    FB_APP_ID = <MY_FB_APP_ID>
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    FB_APP_ID = <MY_FB_APP_ID>

SECRET_KEY = <MY_SECRET_KEY>
