import inspect

from dbs.db_connection import DbConnection


class Model:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @staticmethod
    def add(obj):
        cols_list = [name for name in dir(obj)
                     if not inspect.getattr_static(obj, name) and not name.startswith('__')]
        # wyciąga pola statyczne
        cols = ', '.join(cols_list)
        # print(cols)
        table = obj.__class__.__name__
        # wyciągamy nazwę klasy

        query = f'INSERT INTO {table} ({cols}) VALUES ({", ".join(["?" for _ in cols_list])})'
        # zapytanie gdzie pofajemy table i cols, a w miejsce znaków zapytania dajemy tyle pytajników ile elementów
        # print(query)
        #
        # print(vars(obj))
        task_dict = vars(obj)

        list_keys = list(task_dict['kwargs'].keys())
        list_keys.sort()
        print(list_keys)
        task_val = tuple(task_dict['kwargs'][x] for x in list_keys)
        # TODO remove spaghetti code
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
        print(query)
        db = DbConnection().db
        c = db.cursor()
        c.execute(query, filter_values)
        return c.fetchall()

    @staticmethod
    def update(obj, id_task, status):
        status_name = [name for name in dir(obj) if name == 'status'][0]
        # wyciąga pola statyczne
        table = obj.__class__.__name__
        # wyciągamy nazwę klasy

        query = f"UPDATE {table} SET {status_name}={status} WHERE id = {id_task}"

        # zapytanie gdzie pofajemy table i cols, a w miejsce znaków zapytania dajemy tyle pytajników ile elementów
        # print(query)
        # print(vars(obj))

        db = DbConnection().db
        c = db.cursor()

        c.execute(query)
        db.commit()

    @staticmethod
    def delete(obj, id_task):
        table = obj.__class__.__name__

        query = f"DELETE FROM {table} WHERE id = {id_task}"

        print(query)
        print(vars(obj))

        db = DbConnection().db
        c = db.cursor()

        c.execute(query)
        db.commit()
