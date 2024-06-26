import sys

sys.path.append("/home/perite/coach")

import time
import schedule

import confg
from bot.bot_logging import bot_logger

import utils.shared_variables as shared_variables

from utils.tools_for_db import get_filling_sessions


def run_scheduler():
    schedule.clear()
    schedule.every().day.at("18:00", confg.KYIV_TZ).do(check_group_session_status)
    schedule.every().day.at("20:00", confg.KYIV_TZ).do(check_group_session_status)

    while True:
        schedule.run_pending()
        time.sleep(5)


def check_group_session_status():
    sessions = get_filling_sessions()
    for session in sessions:
        notify_session_canceled(session.coach, session, coach=True)

        for client in session.clients:
            client = client.client
            notify_session_canceled(client, session)

        bot_logger.warning(
            f"Session with id: {session.id} was canceled due to not enough clients or due to expiring, session coach {session.coach} "
            f"and clients {list(map(lambda n: n.client.id, list(session.clients)))} were notified")
        session.status = 4
        session.save()


def notify_session_canceled(who_to_notify, session, coach=False):
    text = (f"На жаль сесія була відмінена через недостатнью кількість учасників\n"
            f"Детальніша інформація про сесію")

    text += shared_variables.tx.group_session_representation_for_client(
        session) if not coach else shared_variables.tx.group_session_representation_for_coach(session)
    if who_to_notify.chat_id:
        shared_variables.bot.send_message(who_to_notify.chat_id, text=text)
        bot_logger.info(
            f"{who_to_notify} | {who_to_notify.full_name} | {who_to_notify.username} | Was notified about session canceling")
    else:
        bot_logger.warning(
            f"Couldnt notify {who_to_notify} | {who_to_notify.full_name} | {who_to_notify.username}, because chat id misssing")
