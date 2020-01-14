import pytest


@pytest.fixture(scope="module")
def db_connection():
    return {"host": "localhost", "user": "root"}


@pytest.fixture(scope="module")
def populate_tables():
    # create object in DDBB:
    objects = {"object1": "user1", "object2": "user2"}
    yield objects
    del objects["object1"]
    del objects["object2"]
