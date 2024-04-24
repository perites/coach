import datetime
from flask import render_template

from web_app.web_app_logging import web_app_error_logger


def error_catcher(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            web_app_error_logger.error("Error occured!")
            web_app_error_logger.exception(e)
            return render_template("error.html", error=e)

    return wrapper


def get_week_dates(year, week_number):
    first_day = datetime.datetime(year, 1, 1)
    first_day_of_week = first_day + datetime.timedelta(days=(week_number - 1) * 7 - first_day.weekday())
    last_day_of_week = first_day_of_week + datetime.timedelta(days=6)
    return f"{first_day_of_week:%d.%m}", f"{last_day_of_week:%d.%m}"
