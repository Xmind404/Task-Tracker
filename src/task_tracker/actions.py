from Question import Question
import json
import os

SAFE_FILE = "tasks.json"


def _load_tasks(file_name=SAFE_FILE):
    if not os.path.exists(file_name):
        return {}

    with open(file_name, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            tasks = {}
            for task_id, task_data in data.items():
                tasks[int(task_id)] = Question(
                    task_data["description"],
                    task_data["status"],
                    task_data.get("createdAt"),
                    task_data.get("updatedAt")
                )
            return tasks
        except json.decoder.JSONDecodeError:
            return {}


def _save_tasks(tasks, file_name=SAFE_FILE):
    data = {}
    for task_id, task in tasks.items():
        data[task_id] = {
            "id": int(task_id),
            "description": task.description,
            "status": task.status,
            "createdAt": task.created_at,
            "updatedAt": task.updated_at,
        }

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def init(file_name=SAFE_FILE):
    print(f"Initializing tasks file: {file_name}")
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump({}, f)


def add(description):
    print(f"Adding task: {description}")
    tasks = _load_tasks()
    next_id = max(tasks.keys()) + 1 if tasks else 1

    new_task = Question(description, "todo")
    tasks[next_id] = new_task
    _save_tasks(tasks)


def update(task_id, new_description):
    print(f"Updating task ID {task_id} with description: {new_description}")
    tasks = _load_tasks()

    if task_id in tasks:
        tasks[task_id].update(new_description)
        _save_tasks(tasks)
    else:
        print(f"Task {task_id} not found")


def delete(task_id):
    print(f"Deleting task ID: {task_id}")
    tasks = _load_tasks()

    if task_id in tasks:
        tasks.pop(task_id)
        _save_tasks(tasks)
    else:
        print(f"Task {task_id} not found")


def mark(task_id, new_status):
    print(f"Marking task ID {task_id} as: {new_status}")
    tasks = _load_tasks()

    if task_id in tasks:
        tasks[task_id].change_status(new_status)
        _save_tasks(tasks)
    else:
        print(f"Task {task_id} not found")


def status(task_id):
    tasks = _load_tasks()
    if task_id in tasks:
        task = tasks[task_id]
        print(f"Task ID {task_id} status: {task.status}")
    else:
        print(f"Task {task_id} not found")


def list_tasks(filter_status='all'):
    tasks = _load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\nTASK LIST:")
    print("-" * 50)

    found_any = False
    for task_id, task in tasks.items():
        if filter_status and filter_status != 'all' and task.status.lower() != filter_status.lower():
            continue

        print(f"[{task_id}] {task.description:<30} | Status: {task.status}")
        found_any = True

    if not found_any:
        print(f"No tasks found with status: {filter_status}")

    print("-" * 50)


def join_file(file_name):
    print(f"Joining tasks file: {file_name}")
    if not os.path.exists(file_name):
        print(f"File {file_name} does not exist.")
        return

    current_tasks = _load_tasks()
    external_tasks = _load_tasks(file_name)

    for ext_task in external_tasks.values():
        next_id = max(current_tasks.keys()) + 1 if current_tasks else 1
        current_tasks[next_id] = ext_task

    _save_tasks(current_tasks)