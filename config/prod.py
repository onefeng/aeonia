# coding: utf-8
from .default import Config


class ProductionConfig(Config):
    # App config
    # Flask app config
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@10.150.0.25:23306/webconfig'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # socket 配置
    SOCKET_HOST = '34.85.237.7'
    SOCKET_PORT = 6789
    SOCKET_SWITCH = True  # socket发送开关
    TABLE_SCHEMA = 'webconfig'

    SCHEDULER_API_ENABLED = True
    JOBS = [{
        'id': 'sync_data',
        'func': 'application.utils.scheduler_job:sync_data',
        'trigger': 'interval',
        'seconds': 60
    }]
