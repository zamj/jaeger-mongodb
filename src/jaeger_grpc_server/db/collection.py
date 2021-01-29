"""Interface for working with database collections."""
from pymongo.database import Database


class Collection(object):
    """Base class for database collections."""

    def __init__(self, db: Database, collection_name: str) -> None:
        """Create a pointer to the specified collection."""
        self.db = db
        self.collection = self.db[collection_name]

    def create_indexes(self) -> None:
        """Create indexes required for the given collection."""
        pass
