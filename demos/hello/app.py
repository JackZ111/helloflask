# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask  # 导入Flask类

app = Flask(__name__)  # 实例类得到app实例，传入特殊变量__name__（此处＝app）


# the minimal Flask application
@app.route('/')  # app.route装饰器/注册路由/路由负责管理URL和函数之间的映射
def index():  # 视图函数
    return '<h1>Hello, World!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')  # 一个视图函数一次性绑定多个URL
def say_hello():
    return '<h1>Hello, Flask!</h1>' # java语言


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>') # 视图函数动态绑定URL，两种不同绑定方式，第二种若用户未输入name变量会返回404
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
