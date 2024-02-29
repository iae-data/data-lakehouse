from omegaconf import OmegaConf, DictConfig
from typing import Dict, List
import os


class Config:
    """
    Configuration class to load all the configuration from the config.yaml file
    """

    @staticmethod
    def load_config():
        config_file_path = "./app/conf/config.yaml"
        with open(config_file_path, "r") as f:
            config = OmegaConf.load(f)

        return Config.check_default_config(config)

    @staticmethod
    def check_default_config(config: DictConfig):
        if 'defaults' in config:
            primitive: List = OmegaConf.to_container(config.defaults)
            for yamls in primitive:
                category, filename = next(iter(yamls.items()))

                yaml_file_path = os.path.join("./app/conf", category, f"{filename}.yaml")

                if os.path.exists(yaml_file_path):
                    additional_config = OmegaConf.load(yaml_file_path)
                    config = OmegaConf.merge(config, additional_config)
        return config

    def __init__(self):
        self.config = self.load_config()

    def print_config(self):
        print(OmegaConf.to_yaml(self.config))

    def get(self, key):
        return OmegaConf.select(self.config, key)
