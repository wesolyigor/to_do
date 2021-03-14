import os


def find_project_root():
    return os.path.join(os.path.dirname(__file__), "..")


def load_envs():
    project_root = find_project_root()
    os.environ["ROOT_DIR"] = project_root
    file_path = os.path.join(project_root, '.env')
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                lista = line.replace("\n", "").split(": ")
                os.environ[lista[0]] = lista[1]
    else:
        raise ValueError('Wrong app configuration. Check environment variables')


def save_env(key, value):
    project_root = find_project_root()
    file_path = os.path.join(project_root, '.env')
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
