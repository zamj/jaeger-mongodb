"""Configuration for the plugin."""
from __future__ import annotations

from typing import Dict

import yaml
from pydantic import BaseSettings


def read_file(filepath: str) -> str:
    """Read a file and return the content."""
    with open(filepath, "r") as filep:
        return filep.read()


def read_yaml_file(filepath: str) -> Dict:
    """Read a yaml file and return the parsed content."""
    return yaml.safe_load(read_file(filepath))


class Config(BaseSettings):
    """Config settings for the plugin server."""

    grpc_port: int = 1234
    mongo_url: str = "mongodb://localhost:27017"

    @classmethod
    def from_yaml_file(cls, file_path: str) -> Config:
        """
        Read the config from the given file path.

        :param file_path: Path to config file.
        :return: config object.
        """
        return cls(**read_yaml_file(file_path))
