# YAML 파일 설정.
import yaml


def get_config():
    with open('config.yaml', encoding='UTF8') as f:
        config_yaml = yaml.load(f, Loader=yaml.FullLoader)
    return config_yaml
