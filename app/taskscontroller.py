from flask import Blueprint, jsonify

tasks_blueprint = Blueprint('random', __name__, url_prefix='/tasks')

tasks = [
            {
                "id": 1,
                "title": "Groceries"
            },
            {
                "id": 2,
                "title": "Book movie tickets"
            },
            {
                "id": 3,
                "title": "Bills"
            }
        ]


@tasks_blueprint.route('/')
def get_all_tasks():
    return jsonify(tasks)