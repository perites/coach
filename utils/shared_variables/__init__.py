import telebot
import confg
import utils.session_types as session_types

bot = telebot.TeleBot(confg.BOT_TOKEN, threaded=False)

SESSIONS_TYPE_FOR_WEEK = list()
for session_type_str in confg.SESSIONS_TYPE_FOR_WEEK:
    session_type = session_types.ALL_SESSIONS_TYPES[session_type_str['name']]
    SESSIONS_TYPE_FOR_WEEK.append(
        session_type(session_type_str['start_date'], session_type_str['end_date'])
    )
