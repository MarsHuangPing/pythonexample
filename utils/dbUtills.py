#!/usr/bin/env python
# -*- coding:utf-8 -*-

import psycopg2
import ConfigParser


cp = ConfigParser.SafeConfigParser(allow_no_value=True)
cp.read('config.ini')

__database = cp.get('db', 'database')
__user = cp.get('db', 'user')
__passwd = cp.get('db', 'password')
__host = cp.get('db', 'host')
__port = cp.get('db', 'port')


def execute(sql_str):
    if sql_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(sql_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        conn = psycopg2.connect(database=__database, user=__user,
                                password=__passwd, host=__host, port=__port)
        cur = conn.cursor()  # 获取一个游标
        cur.execute(sql_str)
        data = cur.fetchall()
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return data
    except Exception as e:
        raise e


# 插入数据，返回数据主键
def execute_insert(insert_str):
    if insert_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(insert_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        conn = psycopg2.connect(database=__database, user=__user,
                                password=__passwd, host=__host, port=__port)
        cur = conn.cursor()
        cur.execute(insert_str)

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        raise e


# 更新数据，返回更新条数
def execute_update(update_str, data):
    if update_str is None:
        raise Exception("参数不能为空：update_str")
    if len(update_str) == 0:
        raise Exception("参数不能为空：update_str")
    try:
        conn = psycopg2.connect(database=__database, user=__user,
                                password=__passwd, host=__host, port=__port)
        cur = conn.cursor()  # 获取一个游标
        count = cur.execute(update_str, data)
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return count
    except Exception as e:
        raise e


# 执行带参数的查询，返回查询结果
def execute_select(select_str):
    if select_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(select_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        conn = psycopg2.connect(database=__database, user=__user,
                                password=__passwd, host=__host, port=__port)
        cur = conn.cursor()  # 获取一个游标
        cur.execute(select_str)
        data = cur.fetchall()
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return data
    except Exception as e:
        raise e


# 执行带参数的删除
def execute_delete(select_str, data):
    if select_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(select_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        conn = psycopg2.connect(database=__database, user=__user,
                                password=__passwd, host=__host, port=__port)
        cur = conn.cursor()  # 获取一个游标
        cur.execute(select_str, data)
        data = cur.fetchall()
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return data
    except Exception as e:
        raise e