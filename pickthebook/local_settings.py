# -*- coding: utf-8 -*-
"""
title              :local_settings
description        :
date               :24.10.16
"""
import os
from .settings import BASE_DIR
__author__ = 'Vitold Komorovski'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
