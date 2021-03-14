from enviroment.env import load_envs
from model_adapter import Model

load_envs()


class Task(Model):
    name = 'TEXT'
    status = 'INTEGER'
    created = "TEXT default (datetime('now', 'localtime'))"
    dashboard_id = 'INTEGER'
    foreign_key = 'INTEGER'

