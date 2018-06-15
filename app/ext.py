# 实例化sqlalchemy对象
# 配置连接数据库的参数
# 注册SQLAlchemy对象

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
# 实例化迁移对象
migrate = Migrate()


# 所有第三方插件的配置总方法
def init_ext(app):
    """
    配置数据库
    """
    config_db(app)
    # 初始化 SQLAlchemy
    db.init_app(app)
    # 注册迁移命令
    migrate.init_app(app=app, db=db)


# 配置数据库连接的参数
def config_db(app):
    # 配置数据库连接的url地址
    # 地址格式 数据库类型 + 驱动://用户名:密码@ip地址:端口/数据库名?key=value
    # 例如  mysql+pymysql://root:root@127.0.0.1:3306/flask?charset=utf8
    app.config['SECRET_KEY'] = '13131231321'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask?charset=utf8'
