from .changeable_confg import *
from .sessions_type_confg import *

import logging

logging.basicConfig(format='%(levelname)s: %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    filename=PATH_TO_GENERAL_LOGS, filemode='w', level=logging.INFO,
                    encoding='utf-8')

import pytz

KYIV_TZ = pytz.timezone('Europe/Kiev')

ADMINS_CHAT_IDS = ['753637902']

SUPPORT_USERNAME = "@kryskaks"

DONATE_URL = "https://send.monobank.ua/jar/5WmqGmXKoF"

LOG_FOLDER_LINK = "https://www.pythonanywhere.com/user/perite/files/home/perite/coachtelegrambot/logs"

BOOK_SESSION_LINK = 'https://forms.gle/cdZfdDa9myKhJw1z5'

SESSIONS_STATUSES = {
    1: ["Open", "Вільна"],
    2: ["Booked", "Заброньована"],
    3: ["Happend", "Відбулась"],
    4: ["Canceled", "Відмінена"],
    5: ["Postponed", "Перенесена"],
    6: ["Expired", "Просрочена"]
}

MIN_AMOUNT_FOR_GROUP_SESSION = 3
GROUP_SESSIONS_STATUSES = {
    1: ["Open", "Вільна"],
    2: ["Booked", "Заброньована"],
    3: ["Happend", "Відбулась"],
    4: ["Canceled", "Відмінена"],
    5: ["Postponed", "Перенесена"],
    6: ["Expired", "Просрочена"],
    7: ["Filling", "Ведеться набір"],
    8: ["Filled", f"Більше {MIN_AMOUNT_FOR_GROUP_SESSION} учасників"]
}

from cryptography.fernet import Fernet

cipher = Fernet(key)

status_colors = {1: "background-color: #fff",
                 2: "background-color: #ffff99",
                 3: "background-color: #ccffcc",
                 4: "background-color: #ff9999",
                 5: "background-color: #ffcccc",
                 6: "background-color: #ff9999"}

group_status_colors = {1: "background-color: #fff",
                       2: "background-color: #ffff99",
                       3: "background-color: #ccffcc",
                       4: "background-color: #ff9999",
                       5: "background-color: #ffcccc",
                       6: "background-color: #ff9999",
                       7: "background-color: #ffcc99",
                       8: "background-color: #47C677", }
