#-*- coding: utf-8 -*-

from .conf.base import *  # import dev config

BASE_TEMPLATE_TITLE = '42cc'

TEMPLATE_CONTEXT_PROCESSORS += (
    't4_context_processor.context_processor.settings',
)

TEMPLATE_VISIBLE_SETTINGS = (
    'BASE_TEMPLATE_TITLE',
)

LOGIN_REDIRECT_URL = '/update/1'

ACCOUNT_ACTIVATION_DAYS = 7