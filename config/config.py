from config.cli import get_config as get_cli_config
from config.yaml import get_config as get_yaml_config


CONFIG = dict()

# 우선 순위가 높을 수록 나중에 업데이트
CONFIG.update(get_yaml_config())
CONFIG.update(get_cli_config())
