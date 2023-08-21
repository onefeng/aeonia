# coding: utf-8
from .default import Config


class DevelopmentConfig(Config):
    SCHEDULER_API_ENABLED = True
    JOBS = [{
        'id': 'sync_data',
        'func': 'application.utils.scheduler_job:sync_data',
        'trigger': 'interval',
        'seconds': 60
    }]
