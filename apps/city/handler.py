# -*- coding: utf-8 -*-

"""
    alter by: Daemon
    alter on 2016-09-20
"""

from projects.apps.base.handler import TokenHandler,SingleStandardHanler,MultiStandardHandler
from projects.libs.loglib import get_logger
from projects.libs.oauthlib import get_provider

logger = get_logger("debug")

class CityListHandler(MultiStandardHandler,TokenHandler):
    _model = "city.CityModel"

class CityHandler(SingleStandardHanler,TokenHandler):
    _model = "city.CityModel"

handlers = [
            (r"", CityListHandler,get_provider('frontend')),
            (r"/(.*)", CityHandler,get_provider('frontend')),
            ]
