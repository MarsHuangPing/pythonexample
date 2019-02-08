#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, abort, request, jsonify
import base64
import psycopg2

app = Flask(__name__)

# 测试数据暂时存放
tasks = []
cameras = []

from Recieves import Recieves as producers
app.register_blueprint(producers)

from Sends import Consumers as consumers
app.register_blueprint(consumers)


def convert_row_to_dict(row):
    return {
        'id': row[0],
        'cameraName': row[1],
        'numberOfCamera': row[2],
        'base64OfImage': row[3],
        'cameraStatus': row[4],
        'updateTime': row[5]
    }

@app.route('/getAllCamera', methods=['POST'])
def getAllCamera():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)

    conn = psycopg2.connect(database="monitordb", user="postgres", password="fphuang", host="127.0.0.1", port="5432")
    print "Opened database successfully"

    cur = conn.cursor()
    cur.execute('''SELECT * from CameraMonitor;''')

    rows = cur.fetchall()

    print "selected all data successfully"
    conn.close()

    cameras = []

    for row in rows:
        camera = convert_row_to_dict(row)
        cameras.append(camera)

    return jsonify({'result': 'success','cameras': cameras})


@app.route('/addCameraMonitor/', methods=['POST'])
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


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)