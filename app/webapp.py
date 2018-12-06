from flask import Flask, jsonify
from app.taskscontroller import tasks_blueprint

app = Flask(__name__)

app.register_blueprint(tasks_blueprint)

if __name__ == '__main__':
    app.run()