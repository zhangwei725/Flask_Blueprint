from flask import Flask

from .ext import init_ext
from app.user.views import user, init_user_blue

# 实例化flask对象
app = Flask(__name__)
app.debug = True


def get_app():
    register_blue()
    init_ext(app)
    return app


# 奥克米
# 统一注册所有的蓝图对象
def register_blue():
    init_user_blue(app)
