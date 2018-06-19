import json

"""


"""

from flask import Blueprint, render_template, jsonify

from app.ext import db
from .models import User

user = Blueprint('user', __name__, static_folder='static', template_folder='templates')


def init_user_blue(app):
    app.register_blueprint(user, url_prefix='/user')


"""
/index
/index/
"""


@user.route('/index')
def index1():
    user = User(name='老王', )
    db.session.add(user)
    db.session.commit()
    return render_template('index.html', msg='非洲热还是武汉热')


""""
查表 行跟列的组合
查询所有   
SELECT * FROM 表
SELECT  列 ,列  FROM 表

"""


@user.route('/find/')
def find():
    # 通过id查询对象
    user = User.query.get(1)
    User.query.all()
    User.query.filter(User.name == '老王').first()
    # html_start = r'<!DOCTYPE html>  <head>  <meta charset = "UTF-8" > <title>用户信息 </title ></head>'
    # body_start = '<body>' + user.name + str(user.uid)
    # body_end = ' </body>'
    # html_end = r'<!DOCTYPE html>'
    # response_str = html_start + body_start + body_end + html_end
    return 
