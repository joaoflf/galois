import pytest
import shutil
from galois.database import Database


@pytest.fixture
def test_database():
    db_name = "test_db"
    db = Database(db_name)
    yield db
    shutil.rmtree(f"database/{db_name}")


def test_create_collection(test_database):
    test_database.create_collection("test_collection")
    assert len(test_database) == 1


def test_get_collection(test_database):
    test_database.create_collection("test_collection")
    collection = test_database.get_collection("test_collection")
    assert collection.name == "test_collection"


def test_delete_collection(test_database):
    test_database.create_collection("test_collection")
    test_database.delete_collection("test_collection")
    assert len(test_database) == 0
