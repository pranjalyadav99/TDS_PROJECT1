from app.tasks import phase_a, phase_b
from app.utils.helpers import parse_task_with_llm

class Agent:
    def __init__(self):
        self.task_handlers = {
            **phase_a.tasks,
            **phase_b.tasks
        }

    def execute_task(self, task_description):
        parsed_task = parse_task_with_llm(task_description)
        task_handler = self.task_handlers.get(parsed_task["type"])
        
        if not task_handler:
            raise ValueError(f"Unknown task type: {parsed_task['type']}")
        
        return task_handler(parsed_task["params"])
