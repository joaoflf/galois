import os
from typing import Optional

from galois.collection import Collection
from galois.lsmtree import LSMTree


class Database:
    """
    A database is a collection of collections. It is represented by a directory in the filesystem.

    Args:
        name (str): The name of the database.
    """

    def __init__(self, name: str):
        self.name = name
        self.path = f"storage/{name}"
        self.collections = []
        self.storage_engine = LSMTree()

        # if the database directory exists, load the collections, else create the directory
        if os.path.exists(self.path):
            for collection_name in os.listdir(self.path):
                collection = Collection(collection_name, self)
                self.collections.append(collection)
        else:
            if not os.path.exists(self.path):
                os.makedirs(self.path)

    def __iter__(self):
        return iter(self.collections)

    def __len__(self):
        return len(self.collections)

    def __getitem__(self, index):
        return self.collections[index]

    def __repr__(self):
        return f"Database({self.name})"

    def __str__(self):
        return f"Database({self.name})"

    def create_collection(self, name: str):
        """
        Create a new collection in the database.
        Throws an exception if the collection already exists.

        Args:
            name (str): The name of the collection to create.
        """

        if self.get_collection(name) is not None:
            raise Exception(f"Collection '{name}' already exists.")

        collection = Collection(name, self)
        self.collections.append(collection)

        return collection

    def get_collection(self, name: str) -> Optional[Collection]:
        """
        Get a collection from the database.

        Args:
            name (str): The name of the collection to get.

        Returns:
            Collection: The collection with the given name.
        """
        for collection in self.collections:
            if collection.name == name:
                return collection

        return None

    def delete_collection(self, name: str):
        """
        Delete a collection from the database.

        Args:
            name (str): The name of the collection to delete.
        """
        if self.get_collection(name) is None:
            raise Exception(f"Collection '{name}' does not exist.")

        for collection in self.collections:
            if collection.name == name:
                self.collections.remove(collection)
                os.rmdir(collection.path)

        return None
