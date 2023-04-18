from flask import Flask, render_template


def create_app(flask_name) -> Flask:
    app = Flask(flask_name)

    @app.route("/")
    def display_client():
        return render_template("index.html")

    return app
