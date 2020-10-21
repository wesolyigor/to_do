import os


def load_envs():
    file_path = os.path.join('.env')
    os.environ["ROOT_DIR"] = os.path.abspath(".")
    # TODO create implementation which is not dependent on execution path
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                lista = line.replace("\n", "").split(": ")
                os.environ[lista[0]] = lista[1]
    else:
        print('Wrong app configuration. Check environment variables')


def save_env(key, value):
    file_path = os.path.join('..', '.env')
    with open(file_path, 'r') as file:
        data = file.readlines()

    new_data = []

    for line in data:
        if key == line.split(':')[0]:
            new_data.append(f'{key}: {value}\n')
        else:
            new_data.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_data)

    print(data)


save_env("DB_PATH", "db_test")
