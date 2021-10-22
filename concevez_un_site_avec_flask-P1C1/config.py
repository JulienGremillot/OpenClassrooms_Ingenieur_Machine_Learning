import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

FB_APP_ID = <MY_FB_APP_ID>

SECRET_KEY = <MY_SECRET_KEY>
