from app import create_app, createSocketIO

app = create_app(__name__)

socketio = createSocketIO(app)

if __name__ == "__main__":
    socketio.run(app)
