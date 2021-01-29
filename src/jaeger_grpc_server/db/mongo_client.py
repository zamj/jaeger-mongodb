"""Module to control access to data stored in MongoDB."""
from __future__ import annotations

from pymongo import MongoClient
from pymongo.database import Database

from jaeger_grpc_server.db.span_collection import SpanCollection

_DB_NAME = "jaeger"


class MongoWrapper:
    """A wrapper around a pymongo client with some helper methods."""

    def __init__(self, db: Database) -> None:
        """Create a new MongoWrapper for the given db."""
        self.db = db
        self.span_collection = SpanCollection(self.db)

    @classmethod
    def from_uri(cls, mongo_uri: str) -> MongoWrapper:
        """
        Create a MongoWrapper from a Mongo connection uri.

        :param mongo_uri: The uri that points to a mongodb instance.
        :return: An instance of the MongoWrapper class
        """
        return cls(MongoClient(mongo_uri).get_database(_DB_NAME))
