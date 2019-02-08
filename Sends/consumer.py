#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import abort, request, jsonify

import dbUtills
import base64

from . import Consumers
import ConfigParser


@Consumers.route('/addCameraMonitor/', methods=['POST'])
def addCameraMonitor():
    if not request.json or 'cameras' not in request.json:
        abort(400)

    cameras = request.json['cameras']
    leng = len(cameras)

    result = True

    for camera in cameras:
        cn = camera['cameraName']
        noc = camera['numberOfCamera']
        basestring = camera['baseImage']

        print basestring
        fh = open("./upload/%s.jpeg" % cn, "wb")
        fh.write(base64.b64decode(basestring))
        fh.close()

        sql = '''insert into CameraMonitor(
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
                   );''' % (cn, noc)

        try:
            dbUtills.execute_insert(sql)

            # id = 0
            # rows = dbUtills.execute_select("SELECT MAX(id) FROM CameraMonitor")
            # if len(rows) != 0:
            #     id = rows[0][0]

            # return jsonify({'result': True, 'message': 'success', 'id': id})
        except Exception as e:
            result = False
            break
            # return jsonify({'result': False, 'message': e.message})

    if result:
        return jsonify({'result': True, 'message': 'success', 'id': 0})
    else:
        return jsonify({'result': False, 'message': ''})

# @Consumers.route('/addCameraMonitor/', methods=['POST'])
# def addCameraMonitor():
#     if not request.json or 'cameraName' not in request.json or 'numberOfCamera' not in request.json:
#         abort(400)
#
#     cn = request.json['cameraName']
#     noc = request.json['numberOfCamera']
#     basestring = request.json['baseImage']
#
#     print basestring
#     fh = open("./upload/%s.jpeg"%cn, "wb")
#     fh.write(base64.b64decode(basestring))
#     fh.close()
#
#     sql = '''insert into CameraMonitor(
#            cameraName,
#            numberOfCamera,
#            base64OfImage,
#            cameraStatus,
#            updateTime)
#            values(
#            '%s',
#            '%s',
#            'boi',
#            1,
#            'ut'
#            );'''%(cn, noc)
#
#     try:
#         dbUtills.execute_insert(sql)
#
#         id = 0
#         rows = dbUtills.execute_select("SELECT MAX(id) FROM CameraMonitor")
#         if len(rows) != 0:
#             id = rows[0][0]
#
#         return jsonify({'result': True, 'message':'success', 'id': id})
#     except Exception as e:
#         return jsonify({'result': False, 'message': e.message})