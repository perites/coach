import sys

sys.path.append("/home/perite/coach")

from peewee import fn
from .models import Client, Coach, Session, GroupSessionToClients, GroupSession


def get_coach_by_id(coach_id):
    coach = Coach.get_by_id(coach_id)
    return coach


def get_client_by_id(client_id):
    client = Client.get_by_id(client_id)
    return client


def get_all_clients():
    clients = Client.select()

    return clients


def get_all_coaches():
    coaches = Coach.select()

    return coaches


def session_delete_client(session, client):
    session_to_client = GroupSessionToClients.get(
        GroupSessionToClients.group_session == session,
        GroupSessionToClients.client == client
    )

    # web_app_logger.info(f'Deleting client with id {client.id} from group session with id {session.id}')

    session_to_client.delete_instance()
    session_to_client.save()

    return


def get_session_by_week(week_number, groups=False):
    if groups:
        sessions_and_clients = list()
        sessions = GroupSession.select().where(fn.DATE_PART('week', GroupSession.date) == week_number).order_by(
            GroupSession.date,
            GroupSession.starting_time)

        for session in sessions:
            clients = GroupSessionToClients.select().where(GroupSessionToClients.group_session == session)
            clients = map(lambda n: n.client, clients)

            sessions_and_clients.append((session, clients))

        return sessions_and_clients

    sessions = Session.select().where(fn.DATE_PART('week', Session.date) == week_number).order_by(Session.date,
                                                                                                  Session.starting_time)
    return sessions
