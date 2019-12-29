import logging
import traceback
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler
from sys import stdout

# from api.datamodel.data_model import db
from flask import request
from sqlalchemy import event


def get_logger():
    """
    Return a logger which should have been initialized in the app startup
    :return:
    """
    return logging.getLogger('api.log_utils')


def logger(app):
    """
    Logging Methods
    :param app:
    :return:
    """
    cfg = app.config
    logger = logging.getLogger(__name__)
    log_name = cfg['log']['log_name']
    if log_name == 'stdout':
        file_handler = StreamHandler(stdout)
    else:
        # create a TimedRotatingFileHandler
        file_handler = TimedRotatingFileHandler(filename=log_name,
                                                when=cfg['log']['ROLLOVER'],
                                                interval=cfg['log']['INTERVAL'],
                                                backupCount=cfg['log']['BACKUP_COUNT'])

    file_handler.setFormatter(logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    formatter = logging.formatter(
            '%(asctime)s, %(levelname)-8s [%(filename)s:%''(module)s:%(funcName)s:%(lineno)d]%(message)s')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    @app.after_request
    def response_request_logger(response):
        # Log return variables
        method = request.method
        endpoint = request.url
        host = request.url_root
        status_code = response.status
        """ Logging after every request, logs the flask server stream """
        if response.status_code != 500:
            logger.info('REQUEST: Method: {0}, Host: {1}, Endpoint: {2}, Status Code: {3}'.format(method,
                                                                                                  host,
                                                                                                  endpoint,
                                                                                                  status_code))
            return response

    @app.errorhandler(Exception)
    def log_uncaught_exceptions(error):
        endpoint = request.url
        method = request.method
        host = request.url_root
        exception_name = error.__class__.__name__
        exception_traceback = traceback.format_exc()
        logger.critical('EXCEPTION: Method: {0}, Host: {1}, Ebdpoint: {2}, \n Exception Type: {3}\n {4}'.format(method,
                                                                                                                host,
                                                                                                                endpoint,
                                                                                                                exception_name,
                                                                                                                exception_traceback))
