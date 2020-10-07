class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        """
        sprawdzane jest czy ta klasa istnieje, jeżeli nie to jest dodawana do słownika instance
        Nie da się dzięki temu więcej niż jednego obiektu danej klasy
        :param args:
        :param kwargs:
        """
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
