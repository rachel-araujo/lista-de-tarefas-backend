from flask import request, jsonify, Blueprint
from flask_restful import Api
from config import app, db
from models import Task

task_routes = Blueprint('task_routes', __name__)
api = Api(app)

@task_routes.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@task_routes.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@task_routes.route('/api/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    task.completed = True
    db.session.commit()
    return jsonify(task.to_dict())

@task_routes.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return '', 204


app.register_blueprint(task_routes)
