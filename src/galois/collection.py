import json
import os
import time
from functools import lru_cache


class Collection:
    """
    A collection of documents. It contains a hashmap of document ids to document paths.

    Args:
        name (str): The name of the collection.
        database (Database): The database the collection belongs to.
    """

    def __init__(self, name: str, database):
        self.name = name
        self.path = f"{database.path}/{name}"

        # create the collection directory if it doesn't exist
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            self.documents = dict()
        else:
            # get the ids of all documents in the collection
            self.documents = {
                file[:-5]: f"{self.path}/{file}"
                for file in os.listdir(self.path)
                if file.endswith(".json")
            }

        self.current_process = os.getpid()
        self.id_process_counter = os.urandom(3)

    @lru_cache(maxsize=128)
    def __getitem__(self, key):
        """
        Read a document from the collection from the filesystem, using lru_cache to cache the result.
        """
        with open(self.documents[key], "r") as file:
            return json.loads(file.read())

    def __iter__(self):
        return iter(self.documents)

    def __len__(self):
        return len(self.documents)

    def __repr__(self):
        return f"Collection({self.name})"

    def __str__(self):
        return f"Collection({self.name})"

    def _insert(self, document: dict):
        """
        Insert a document into the collection and write it to the filesystem.
        generate a unique id for the document.

        Args:
            document (dict): The document to insert.
        """

        document_id = self.__generate_document_id()
        document["_id"] = document_id

        with open(f"{self.path}/{document_id}.json", "w") as file:
            file.write(json.dumps(document))

        self.documents[document_id] = f"{self.path}/{document_id}.json"

    def _update(self, document_id: str, new_document: dict):
        """
        Update a document in the collection and write it to the filesystem.
        Raises an exception if the document does not exist.

        Args:
            document_id (str): The id of the document to update.
            new_document (dict): The new document to replace the old one with.
        """

        if document_id not in self.documents:
            raise Exception(f"Document with id '{document_id}' does not exist.")

        new_document["_id"] = document_id
        with open(self.documents[document_id], "w+") as file:
            file.write(json.dumps(new_document))

    def __generate_document_id(self) -> str:
        """
        Generate a unique ID similar to MongoDB ObjectId, consisting of 4-byte timestamp,
        5-byte random value, and 3-byte incrementing counter.

        The generated ID is represented as a 24-character hexadecimal string.

        Returns:
            str: The generated unique ID as a 24-character hexadecimal string.
        """
        # if the process id has changed, reset the counter
        if self.current_process != os.getpid():
            self.current_process = os.getpid()
            self.id_process_counter = os.urandom(3)

        # incrmement the counter
        self.id_process_counter = (
            int.from_bytes(self.id_process_counter, "big") + 1
        ).to_bytes(3, "big")

        # get current time in bytes
        current_time = int(time.time()).to_bytes(4, "big")

        # return the id as string
        # 4 bytes for time, 5 bytes for random, 3 bytes for counter
        return (current_time + os.urandom(5) + self.id_process_counter).hex()
