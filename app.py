from flask import Flask
from views import card_views


def main(host: str, port: int, debug_mode: bool = True):
    app = Flask(__name__)
    app.register_blueprint(card_views, url_prefix='/')
    app.run(host=host, port=port, debug=debug_mode)


if __name__ == '__main__':
    main(host='0.0.0.0', port=8000)
