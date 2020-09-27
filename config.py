class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://test1:Test1P@ssw0rd@localhost/test1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = "172.24.225.165:5000"
    SECRET_KEY = "secret"
