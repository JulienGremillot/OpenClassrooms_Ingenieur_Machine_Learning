import os
SECRET_KEY = '<MY_SECRET_KEY>'

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

# Active le debogueur
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10

# Facebook test user
FB_USER_NAME = "toto toto"
FB_USER_PW = "toto123"
FB_USER_EMAIL = "toto_pjznlqe_toto@tfbnw.net"
FB_USER_ID = <MY_FB_USER_ID>
FB_USER_GENDER = 'female'

SERVER_NAME = 'localhost:8943'
