# from flask import Blueprint, jsonify, request
# from app import db
# from sqlalchemy import desc
# from .routes_helper import validate_id, validate_input
# import datetime, os,requests
# from app.models.task import Task

# task_bp= Blueprint("task_bp", __name__, url_prefix="/tasks")

# @task_bp.route("",methods=["GET"])
# def get_all_tasks():
#     sort_query= request.args.get("sort")
    
#     if sort_query:
#         if sort_query == "desc":
#             tasks = Task.query.order_by(desc(Task.title))
#         else:
#             tasks = Task.query.order_by(Task.title)
#     else:
#         tasks = Task.query.all()

#     all_tasks = []
#     for task in tasks:
#         all_tasks.append(task.to_dict())
#     return jsonify(all_tasks), 200

# @task_bp.route("/<task_id>", methods=["GET"])
# def get_one_task_by_id(task_id):
#     task = validate_id(Task, task_id)
#     if task.goal_id:
#         return jsonify({"task": task.to_dict_goal_id()}), 200
#     return jsonify({"task": task.to_dict()}), 200

# @task_bp.route("<task_id>", methods=["PUT"])
# def update_one_task(task_id):
#     task = validate_id(Task, task_id)

#     request_body = request.get_json()
#     task.title = request_body["title"]
#     task.description= request_body["description"]
    
#     db.session.commit()

#     return jsonify({"task": task.to_dict()}), 200

# @task_bp.route("", methods=["POST"])
# def create_new_task():
#     request_body = request.get_json()
#     validate_input(Task, request_body)
#     task = Task.from_dict(request_body)

#     db.session.add(task)
#     db.session.commit()

#     return jsonify({"task": task.to_dict()}), 201

# @task_bp.route("<task_id>", methods=["DELETE"])
# def delete_one_task(task_id):
#     task=validate_id(Task, task_id)

#     db.session.delete(task)
#     db.session.commit()

#     return jsonify({"details": f'Task {task.task_id} "{task.title}" successfully deleted'})

# @task_bp.route("/<task_id>/mark_complete", methods=["PATCH"])
# def mark_complete(task_id):
#     task = validate_id(Task, task_id)
#     task.completed_at = datetime.datetime.today()
#     task.is_complete = True

#     db.session.commit()
#     query_params={
#         "channel": "task-list-notifications",
#         "text": f"Someone just completed the task {task.title}"
#     }
#     header = {"Authorization": f"Bearer {os.environ.get('SLACK_TASK_BOT_KEY')}"}
#     requests.get(os.environ.get("SLACK_POST_MESSAGE_PATH"), params=query_params, headers=header)

#     return jsonify({"task": task.to_dict()}), 200

# @task_bp.route("/<task_id>/mark_incomplete", methods=["PATCH"])
# def mark_incomplete(task_id):
#     task = validate_id(Task, task_id)
#     task.completed_at = None
#     task.is_complete = False

#     db.session.commit()

#     return jsonify({"task": task.to_dict()}), 200