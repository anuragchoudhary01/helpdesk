import sys
import yaml

# from api.datamodel import db
from utils.log_utils import logger

from flask import Flask
from flask_cors import CORS

from sqlalchemy.sql import text

# from .extensions import mail


def create_app(config=None):
    if config is None:
        logger.error('Please provide the config file. Exiting...')
        sys.exit(99)
    with open(config, 'r') as config_handle:
        cfg = yaml.safe_load(config_handle)

    app = Flask(__name__)
    app.config.update(cfg)
    app.secret_key = 'tHiSiShElDeSkSeCrEtKeY'

    # setup specifics for sqlalchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{username}:{password}@{host}/{db}".format(
        username=cfg['mysql']['user'],
        password=cfg['mysql']['pw'],
        host=cfg['mysql']['host'],
        db=cfg['mysql']['db'])

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_NATIVE_UNICODE'] = True

    # Mail Configuration
    app.config['MAIL_SERVER'] = cfg['email-server']['server']
    app.config['MAIL_USERNAME'] = cfg['email-server']['username']
    app.config['MAIL_PASSWORD'] = cfg['email-server']['password']
    app.config['MAIL_PORT'] = cfg['email-server']['port']
    app.config['MAIL_DEFAULT_SENDER'] = cfg['email-server']['username']
    app.config['MAIL_USE_SSL'] = cfg['email-server']['use_ssl']
    app.config['MAIL_USE_TLS'] = cfg['email-server']['use_tls']

    app.config['SWAGGER_UI_JSONEDITOR'] = True
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    app.config['SWAGGER_DOC_URL'] = cfg['swagger']['SWAGGER_DOC_URL']

    # db.init_app(app)

    # deal with CORS
    CORS(app)

    # register the extensions
    # register_extensions(app)

    # register the endpoints
    # register_blueprints(app)

    # API init
    from app.api import api
    api.init_app(app)

    return app

#
# def register_extensions(app):
#     """ Connects the flask extension to the app """
#     mail.init_app(app)
#
#
# def register_stored_procedures(app):
#     """ Register the sql functions """
#     with app.app_context():
#         engine = db.get_engine()
#
#         # Prepare the list of stored procedures kept in repo
#         relative_path_to_sql_functions = 'api/sql_functions'
#         sql_func_list = []
#         for (_dirpath, _dirname, filenames) in os.walk(relative_path_to_sql_functions):
#             sql_func_list.extend(filenames)
#
#         # Execute each stored procedures
#         for file_ in sql_func_list:
#             with open(os.path.join(relative_path_to_sql_functions, file_), 'r') as fh:
#                 proc = fh.read()
#                 engine.execute(text(proc))
#
#     @app.after_request
#     def after_request(response):
#         response.headers.add('Access-Control-Expose-Headers', '*')
#         response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Accept')
#         response.headers.add('Access-Control-Allow-Credentials', 'true')
#         response.headers.add('Access-Control-Allow-Methods', 'GET,HEAD,POST,PUT,DELET,OPTIONS')
#         return response
#
#     return app
#
#
# def delete_stored_procedures(app):
#     """ Delete SQL Functions """
#     pass
#
#
# def register_blueprints(app):
#     """ Register blueprints on prepared app in create_app() """
#     from api.endpoints import index_bp
#
#     app.register_blueprint(index_bp)
