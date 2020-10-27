import os


def get_env():
    with open('.env', 'r') as file:
        for l in file:
            arr = l.replace('\n', '').split(': ')
            print(arr)
            os.environ[arr[0]] = arr[1]
    a = os.environ.get('DB_PATH')
    print(a)


get_env()


def abs_path():
    print(os.path.abspath(__file__))
    print(os.path.abspath('./singleton/singleton.py'))


abs_path()
