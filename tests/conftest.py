import os
import tempfile

import pytest
from blare import create_app


with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")

@pytest.fixture
def app():
    db_fd = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()