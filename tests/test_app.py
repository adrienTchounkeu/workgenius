import mock
from flask.testing import FlaskClient
from flask_socketio import SocketIOTestClient


def test_template_rendering(test_app: FlaskClient):
    response = test_app.get("/")

    assert response.status_code == 200
    assert response.mimetype == "text/html"


def test_socket_connect(test_socketio: SocketIOTestClient):
    assert test_socketio.is_connected()


@mock.patch("db.cache.redis.Redis.mset")
def test_mandrill_events(
    mocker: mock.MagicMock, test_socketio: SocketIOTestClient, test_app
):
    data = dict(
        mandrill_events=[{"event": "send", "_id": "exampleaaaaaaaaaaaaaaaaaaaaaaaaa"}]
    )
    test_socketio.app.test_client().post("/message-events", json=data)

    # test if redis has been called !
    mocker.assert_called_once()

    events = test_socketio.get_received()
    assert len(events) == 1
    curr_event = events[0]
    assert curr_event["name"] == "notification"
    assert curr_event["args"] == [dict(send=1)]
