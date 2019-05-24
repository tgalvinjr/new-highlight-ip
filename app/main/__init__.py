from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from ..config import config_options


app = Flask (__name__, instance_relative_config=True)

app.config.from_object (DevConfig) # setup configuration
bootstrap = Bootstrap(app)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .request import configure_request
    configure_request(app)

    return app

from app import views
from app import error