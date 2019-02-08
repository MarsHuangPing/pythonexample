#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import abort, request, jsonify

import psycopg2
import dbUtills
import base64

from . import Consumers
import ConfigParser


@Consumers.route('/addCameraMonitor/', methods=['POST'])
def addCameraMonitor():
    if not request.json or 'cameraName' not in request.json or 'numberOfCamera' not in request.json:
        abort(400)

    cn = request.json['cameraName']
    noc = request.json['numberOfCamera']
    basestring = request.json['baseImage']

    print basestring
    fh = open("./upload/%s.jpeg"%cn, "wb")
    fh.write(base64.b64decode(basestring))
    fh.close()


    conn = psycopg2.connect(database="monitordb", user="postgres", password="fphuang", host="127.0.0.1", port="5432")
    print "Opened database successfully"

    cur = conn.cursor()

    cur.execute('''insert into CameraMonitor(
           cameraName,
           numberOfCamera,
           base64OfImage,
           cameraStatus,
           updateTime)
           values(
           '%s',
           '%s',
           'boi',
           1,
           'ut'
           );'''%(cn,noc))



    print "Table created successfully"

    conn.commit()
    conn.close()
    return jsonify({'result': 'success'})