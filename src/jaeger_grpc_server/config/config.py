"""Configuration for the plugin."""
from pydantic import BaseSettings


class Config(BaseSettings):
    """Config settings for the plugin server."""

    grpc_port: int = 1234
    mongo_url: str = "mongodb://localhost:27017"
