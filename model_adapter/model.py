from dbs.db_connection import DbConnection


class Model:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @staticmethod
    def execute_query(query, params=()):
        db = DbConnection().db
        c = db.cursor()

        c.execute(query, params)
        db.commit()

    @staticmethod
    def add(obj):
        table = obj.__class__.__name__
        task_dict = vars(obj)
        dict_keys = list(task_dict['kwargs'].keys())
        cols = ', '.join([x for x in dict_keys])
        query = f'INSERT INTO {table} ({cols}) VALUES ({", ".join(["?" for _ in dict_keys])})'
        task_val = tuple([task_dict['kwargs'][x] for x in dict_keys])
        db = DbConnection().db
        c = db.cursor()
        c.execute(query, task_val)
        db.commit()

    @classmethod
    def query(cls, **kwargs):
        table = cls.__name__  # żebyśmy wiedzieli jaką reprezentuje tabelę
        filter_options = "WHERE " + " AND ".join([f'{k}=?' for k, v in kwargs.items()])

        query = f"SELECT * FROM {table} {filter_options if kwargs else ''}"
        filter_values = tuple(kwargs.values())
        db = DbConnection().db
        c = db.cursor()
        c.execute(query, filter_values)
        return c.fetchall()

    @staticmethod
    def update(obj, id_task, status):
        status_name = [name for name in dir(obj) if name == 'status'][0]
        table = obj.__class__.__name__
        query = f"UPDATE {table} SET {status_name}={status} WHERE id = {id_task}"
        obj.execute_query(query)

    @staticmethod
    def delete(obj, id_task):
        table = obj.__class__.__name__

        query = f"DELETE FROM Task WHERE id = {id_task}"

        db = DbConnection().db
        c = db.cursor()
        c.execute(query)
        db.commit()
