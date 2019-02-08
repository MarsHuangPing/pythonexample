#!/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Blueprint
Recieves = Blueprint('Recieves', __name__, url_prefix='/api/v0.1')
from . import producer