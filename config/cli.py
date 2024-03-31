# CLI ARG 설정.
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--output_name', type=str, default=argparse.SUPPRESS)
parser.add_argument('--src', type=str, default=argparse.SUPPRESS)


def get_config():
    config_cli_args = parser.parse_args()
    config_cli_args = vars(config_cli_args)
    return config_cli_args
