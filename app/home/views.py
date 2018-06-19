from flask import Blueprint, render_template, abort, request
import logging

home = Blueprint('home', __name__)

def init_home_blue(app):
    app.register_blueprint(home)


@home.route('/')
def index(year):
    return '默认首页'


@home.route('/test/')
def test1():
    return '带/和不带/的区别'


@home.route('/converter/<regex("\d{4}"):year>/')
def converter(year):
    print(year)
    return '自定义转化器'


#  get  查     post 增      put 更新   delete  删除   key: values
@home.route('/method/', methods=['post', 'get', 'head', 'put', 'delete'])
def method():
    return '限制请求方式'


"""
全局错误的处理
"""


@home.route('/1/')
def test2():
    if request.method == 'POST':
        pass
    else:
        return abort(400)


@home.errorhandler(404)
@home.errorhandler(400)
def error(e):
    if e.code == 404:
        return render_template('/errors/404.html')
    elif e.code == 400:
        return render_template('/errors/400.html')
    else:
        return render_template('/errors/error.html')
