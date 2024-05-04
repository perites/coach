import logging
import confg

web_app_logger = logging.getLogger('web_app_logger')
if not web_app_logger.handlers:
    _web_app_handler = logging.FileHandler(confg.WEB_APP_LOG_PATH)
    _web_app_formatter = logging.Formatter('%(levelname)s: %(asctime)s - %(message)s')
    _web_app_handler.setFormatter(_web_app_formatter)
    web_app_logger.addHandler(_web_app_handler)
    web_app_logger.setLevel(logging.INFO)

    print("web app logger initialized")
    logging.info("web app logger initialized")
    web_app_logger.info('web app logger initialized | web_app_logger')

web_app_error_logger = logging.getLogger('web_app_error_logger')
if not web_app_error_logger.handlers:
    _web_app_error_handler = logging.FileHandler(confg.WEB_APP_ERROR_LOG_PATH)
    _web_app_error_formatter = logging.Formatter(
        '%(levelname)s: %(asctime)s - %(message)s | %(filename)s - func: %(funcName)s - %(lineno)d')
    _web_app_error_handler.setFormatter(_web_app_error_formatter)
    web_app_error_logger.addHandler(_web_app_error_handler)
    web_app_error_logger.setLevel(logging.INFO)

    print("web app error logger initialized")
    logging.info("web app error logger initialized")
    web_app_error_logger.info('web app error logger initialized | web_app_error_logger')
