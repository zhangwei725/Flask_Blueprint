from flask import render_template, Blueprint, Flask

search = Blueprint('search', __name__)


def init_search_blue(app):
    app.register_blueprint(search, url_prefix='/search')


class Shop:
    def __init__(self, title, name):
        self.name = name
        self.title = title


@search.route('/temp/')
def temp1():
    return render_template('/search/search.html', hello='world',
                           li=['1', 2, 3],
                           dt={'name': '小明', 'age': 18},
                           shop=Shop('手机', '华为')
                           )
