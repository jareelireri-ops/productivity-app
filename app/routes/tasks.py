from flask import Blueprint, request, session, jsonify
from app import db
from app.models.task import Task
from app.schemas.task_schema import task_schema, tasks_schema

# Blueprint for task routes
tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET', 'POST'])
def index_create():
    user_id = session.get('user_id')
    if not user_id:
        return {"error": "Unauthorized"}, 401

    if request.method == 'GET':
        # GET: Fetch only the tasks belonging to the logged-in user
        tasks = Task.query.filter_by(user_id=user_id).all()
        return tasks_schema.dump(tasks), 200

    elif request.method == 'POST':
        # POST: Create a new task for the logged-in user
        data = request.get_json()
        try:
            new_task = Task(
                title=data.get('title'),
                description=data.get('description'),
                importance_level=data.get('importance_level', 1),
                user_id=user_id
            )
            db.session.add(new_task)
            db.session.commit()
            return task_schema.dump(new_task), 201
        except Exception as e:
            return {"error": str(e)}, 400

@tasks_bp.route('/tasks/<int:id>', methods=['PATCH', 'DELETE'])
def update_delete(id):
    user_id = session.get('user_id')
    task = Task.query.filter_by(id=id, user_id=user_id).first()

    if not task:
        return {"error": "Task not found"}, 404

    if request.method == 'PATCH':
        data = request.get_json()
        for attr in data:
            setattr(task, attr, data[attr])
        db.session.commit()
        return task_schema.dump(task), 200

    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return {}, 204