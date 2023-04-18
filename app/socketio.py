from flask import Flask, request
from flask_socketio import SocketIO

from db import redis_client
from helpers import count_messages_by_event, logger


def createSocketIO(app: Flask):
    socketio = SocketIO(app)

    @socketio.on("connection")
    def connect(data):
        logger.info(f"Client is connected with message : {data}")

    @app.route("/message-events", methods=["POST"])
    def handle_messages():
        data = request.get_json()
        mandrill_events = data.get("mandrill_events", None)
        if mandrill_events:
            # store events in redis
            redis_client.store_messages(mandrill_events)

            # count messages by event and send to client
            count_messages = count_messages_by_event(mandrill_events)
            socketio.emit("notification", count_messages)
            logger.info("Events sent to Client")

        return "Success", 200

    return socketio
