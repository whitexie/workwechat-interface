import yaml


def load_yaml(yaml_file_path):
    """
    read yaml file
    :param yaml_file_path: str
    :return:
    """
    with open(yaml_file_path, 'r') as f:
        json_object = yaml.load(f.read(), Loader=yaml.FullLoader)
        return json_object
