from flask import Flask

from app.home.converter import RegexConverter
from app.home.views import home, init_home_blue
from app.search.views import init_search_blue
from .ext import init_ext
from app.user.views import user, init_user_blue

# 404

# 实例化flask对象
app = Flask(__name__)
app.debug = True
# 注册
app.url_map.converters['regex'] = RegexConverter


def get_app():
    register_blue()
    init_ext(app)
    return app


# 奥克米
# 统一注册所有的蓝图对象
def register_blue():
    init_user_blue(app)
    init_home_blue(app)
    init_search_blue(app)
