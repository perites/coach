import logging
import confg

bot_logger = logging.getLogger('bot_logger')
if not bot_logger.handlers:
    _bot_handler = logging.FileHandler(confg.BOT_LOG_PATH)
    _bot_formatter = logging.Formatter(
        '%(levelname)s: %(asctime)s - %(message)s')
    _bot_handler.setFormatter(_bot_formatter)
    bot_logger.addHandler(_bot_handler)
    bot_logger.setLevel(logging.INFO)

    print("Bot logger created")
    logging.info("Bot logger created")
    bot_logger.info('Bot logger created | bot_logger')

bot_error_logger = logging.getLogger('bot_error_logger')
if not bot_error_logger.handlers:
    _bot_error_handler = logging.FileHandler(confg.BOT_ERROR_LOG_PATH)
    _bot_error_formatter = logging.Formatter(
        '%(levelname)s: %(asctime)s - %(message)s | %(filename)s - func: %(funcName)s - %(lineno)d')
    _bot_error_handler.setFormatter(_bot_error_formatter)
    bot_error_logger.addHandler(_bot_error_handler)
    bot_error_logger.setLevel(logging.INFO)

    print("Bot error logger created")
    logging.info("Bot error logger created")
    bot_error_logger.info("Bot error logger created | bot_error_logger")
