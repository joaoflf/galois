import pytest
import shutil
from galois.database import Database
from galois.collection import Collection


@pytest.fixture
def test_collection():
    db_name = "test_db"
    db = Database(db_name)
    collection = db.create_collection("test_collection")
    yield collection
    shutil.rmtree(f"storage/{db_name}")


def test_insert_document(test_collection):
    document = {"name": "test_document"}
    test_collection._insert_document(document)
    assert len(test_collection) == 1


def test_get_document(test_collection):
    document = {"name": "test_document"}
    test_collection._insert_document(document)
    assert test_collection._get_document(document["_id"]) == document


def test_delete(test_collection):
    document = {"name": "test_document"}
    test_collection._insert_document(document)
    test_collection._delete_document(document["_id"])
    assert len(test_collection) == 0


def test_update_document(test_collection):
    document = {"name": "test_document"}
    test_collection._insert_document(document)
    document["name"] = "update_documentd_document"
    test_collection._update_document(document["_id"], document)
    assert test_collection._get_document(document["_id"]) == document


def test_generate_id(test_collection):
    document = {"name": "test_document"}
    test_collection._insert_document(document)
    assert len(document["_id"]) == 24
