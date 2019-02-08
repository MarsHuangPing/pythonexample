#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint
Consumers = Blueprint('Consumers', __name__, url_prefix='/api/v0.1')
from . import consumer