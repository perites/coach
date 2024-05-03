import sys

sys.path.append("/home/perite/coach")

from utils.tools_for_db import get_session_of_type_amount, get_free_session_amount
import confg


class SessionType:
    type_name = "name"
    info_text = "info_text"
    _button_text = "button_text"
    ukr_name = "ukr_name"
    # no_session_text = "no_session_text"
    no_session_text = "Зараз нажаль немає вільних слотів на індивідуальні коуч сесії. Чекайте анонсів в чаті проєкту!"

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def button_text(self):
        free_session_amount = get_free_session_amount()
        if free_session_amount > 0:
            return self._button_text, True
        elif free_session_amount == 0:
            return self._button_text, False

        # free_session_amount, session_of_type_amount = get_session_of_type_amount(self.type_name, self.start_date,
        #                                                                          self.end_date)
        #
        # available_sessions_of_type_amount = confg.MAX_SESSIONS_OF_ONE_TYPE - session_of_type_amount
        # available_sessions_amount = min(free_session_amount, available_sessions_of_type_amount)
        # if available_sessions_amount <= 0:
        #     return f"{self._button_text}", False
        #
        # return f"{self._button_text} | Доступно {available_sessions_amount} з {confg.MAX_SESSIONS_OF_ONE_TYPE}", True


class Career(SessionType):
    type_name = "Career"
    info_text = """
*Карʼєрний коучинг* 
Буде корисним якщо ти хочеш:
✅ Прийняти рішення - в якому напрямку кар'єри рухатись
✅ Скласти план подальших дій при пошуку першої роботи в ІТ
✅ Зрозуміти, як краще використати свій попередній досвід,
"""

    _button_text = "Карʼєрний коучинг"
    ukr_name = "Кар'єрний коучинг"

    # no_session_text = ("Нажаль зараз всі місця на кар'єрний коучинг закінчились, "
    #                    "перейдіть за посиланням якщо ви хочете забронювати сесію саме цього типу\n"
    #                    f"[посилання]({confg.BOOK_SESSION_LINK})")

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)


class Leadership(SessionType):
    type_name = "Leadership"
    info_text = """
*Коучинг лідерства* 
Сесія в коучингу лідерства буде корисна, якщо ти хочеш навчитися:
✅ як підтримувати себе на шляху змін
✅ як досягати своїх цілей
✅ як зміцнити впевненість і віру в себе
    """
    _button_text = "Коучинг лідерства"
    ukr_name = "Коучинг лідерства"

    # no_session_text = ("Нажаль зараз всі місця на коучинг лідерства закінчились, "
    #                    "перейдіть за посиланням якщо ви хочете забронювати сесію саме цього типу\n"
    #                    f"[посилання]({confg.BOOK_SESSION_LINK})")

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)


class Relationship(SessionType):
    type_name = "Relationship"
    info_text = '''
*Коучинг стосунків* ❤️
Буде корисним, якщо ти хочеш:
✅ Покращити спілкування і розуміння з партнером
✅ Розуміти свої емоції і емоції оточуючих
✅ Навчитися керувати конфліктами
'''
    _button_text = "Коучинг стосунків"
    ukr_name = "Коучинг стосунків"

    # no_session_text = ("Нажаль зараз всі місця на коучинг стосунків закінчились, "
    #                    "перейдіть за посиланням якщо ви хочете забронювати сесію саме цього типу\n"
    #                    f"[посилання]({confg.BOOK_SESSION_LINK})")

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)


class LifeCouching(SessionType):
    type_name = "LifeCouching"
    info_text = '''
*Life коучинг*
Буде корисним, якщо ти хочеш:
✅ зрозуміти, які в тебе є сильні сторони і як можна на них спиратися в житті
✅ навчитися наповнювати свій ресурс
✅ нарешті почати впроваджувати зміни в життя
    '''
    _button_text = "Life коучинг"
    ukr_name = "Life коучинг"

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)


ALL_SESSIONS_TYPES = {
    Career.type_name: Career,
    Leadership.type_name: Leadership,
    Relationship.type_name: Relationship,
    LifeCouching.type_name: LifeCouching
}
