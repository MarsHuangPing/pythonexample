#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import abort, request, jsonify

import psycopg2

from . import Recieves
import ConfigParser


import DateTimeManager
import dbUtills


def convert_row_to_dict(row):
    return {
        'id': row[0],
        'cameraName': row[1],
        'numberOfCamera': row[2],
        'base64OfImage': row[3],
        'cameraStatus': row[4],
        'updateTime': row[5]
    }

@Recieves.route('/getCameras', methods=['POST'])
def getCameras():
    if not request.json or 'id' not in request.json:
        abort(400)

    cp = ConfigParser.SafeConfigParser(allow_no_value=True)
    cp.read('config.ini')
    conn = psycopg2.connect(database=cp.get('db', 'database'), user=cp.get('db', 'user'), password=cp.get('db', 'password'), host=cp.get('db', 'host'), port=cp.get('db', 'port'))
    print "Opened database successfully"

    id = request.json['id']

    cur = conn.cursor()
    sql = "SELECT * from CameraMonitor where id = %s;"%(id)
    cur.execute(sql)

    rows = cur.fetchall()

    print "selected all data successfully"
    conn.close()

    cameras = []
    print "call the method of other file :%s"%DateTimeManager.curDatetime()

    for row in rows:
        camera = convert_row_to_dict(row)
        cameras.append(camera)

    return jsonify({'result': 'success','cameras': cameras})


@Recieves.route('/getCamerasFromDbUtil', methods=['POST'])
def getCamerasFromDbUtil():
    if not request.json or 'id' not in request.json:
        abort(400)

    rows = []
    id = request.json['id']
    sql = "SELECT * from CameraMonitor where id = %s;" % (id)

    try:
        rows = dbUtills.execute_select(sql)
        camera = {}
        if len(rows) != 0:
            row = rows[0]
            camera = convert_row_to_dict(row)

        return jsonify({'result': True, 'message':'success', 'camera': camera})
    except Exception as e:
        return jsonify({'result': False, 'message': e.message})