# -*- coding: utf-8 -*-

"""
@author: onefeng
@time: 2022/9/22 14:43
"""
import os


def load_config(env):
    """Load config."""
    try:
        if env == 'prod':
            from .prod import ProductionConfig
            return ProductionConfig
        elif env == 'test':
            from .test import TestingConfig
            return TestingConfig
        else:
            from .dev import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from .default import Config
        return Config
