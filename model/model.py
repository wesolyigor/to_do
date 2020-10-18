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
        print(cols)
        table = obj.__class__.__name__
        # wyciągamy nazwę klasy

        query = f'INSERT INTO {table} ({cols}) VALUES ({", ".join(["?" for _ in cols_list])})'
        # zapytanie gdzie pofajemy table i cols, a w miejsce znaków zapytania dajemy tyle pytajników ile elementów
        print(query)

        print(vars(obj))
        # db = DbConnection().db
        # c = db.cursor()
        #
        # c.execute(query, (0, 'zupa była za słona', 0))
        # db.commit()

    @staticmethod
    def query():
        pass

    @staticmethod
    def update(obj, id_task, status):
        status_name = [name for name in dir(obj) if name == 'status'][0]
        # wyciąga pola statyczne
        table = obj.__class__.__name__
        # wyciągamy nazwę klasy

        query = f"UPDATE {table} SET {status_name}={status} WHERE id = {id_task}"

        # zapytanie gdzie pofajemy table i cols, a w miejsce znaków zapytania dajemy tyle pytajników ile elementów
        print(query)
        print(vars(obj))

        # db = DbConnection().db
        # c = db.cursor()
        #
        # c.execute(query)
        # db.commit()

    @staticmethod
    def delete(obj, id_task):
        table = obj.__class__.__name__

        query = f"DELETE FROM {table} WHERE id = {id_task}"

        # print(query)
        # print(vars(obj))

        db = DbConnection().db
        c = db.cursor()

        c.execute(query)
        db.commit()