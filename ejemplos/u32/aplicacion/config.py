import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://smartnet:051000@smartnet.mysql.pythonanywhere-services.com/smartnet$tienda'
SQLALCHEMY_TRACK_MODIFICATIONS = False
