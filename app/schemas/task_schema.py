from app import ma
from app.models.task import Task

# SCHEMA FOR TASK MODEL
class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True
        include_fk = True  # Includes the user_id in the JSON

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)