import os
import sys
from typing import Generator

import pytest
from flask.testing import FlaskClient
from flask_socketio import SocketIOTestClient

sys.path.insert(0, os.path.abspath("."))
from run import app, create_app, socketio


@pytest.fixture(scope="module")
def test_app() -> Generator[FlaskClient, None, None]:
    flask_app = create_app("testing")
    with flask_app.test_client() as test_client:
        with flask_app.app_context():
            yield test_client


@pytest.fixture(scope="module")
def test_socketio() -> Generator[SocketIOTestClient, None, None]:
    yield SocketIOTestClient(app=app, socketio=socketio)
