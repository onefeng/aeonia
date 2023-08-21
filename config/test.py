# coding: utf-8
import os

from .default import Config


class TestingConfig(Config):
    # Flask app config
    # socket 配置
    SOCKET_HOST = '10.10.77.193'
    SOCKET_PORT = 6789
    SOCKET_SWITCH = True  # socket发送开关

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.118.129:3306/webconfig1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TABLE_SCHEMA = 'webconfig1'

    SCHEDULER_API_ENABLED = True
    JOBS = [{
        'id': 'sync_data',
        'func': 'application.utils.scheduler_job:sync_data',
        'trigger': 'interval',
        'seconds': 60
    }]
