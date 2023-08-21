# coding: utf-8
import os


class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = False

    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    LOG_LEVEL = 'DEBUG'

    TOKEN_EXPIRATION_TIME = 60 * 60 * 12
    SECRET_KEY = 'dyulkjy*%&*%&gjgj^%^&vJHG'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.118.129:3306/webconfig'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TABLE_SCHEMA = 'webconfig'

    # socket 配置
    SOCKET_HOST = '10.10.78.183'
    SOCKET_PORT = 6789
    SOCKET_SWITCH = True  # socket发送开关
