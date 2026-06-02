## Project: https://roadmap.sh/projects/task-tracker

## Features

This Task Tracker CLI supports all core requirements from the roadmap.sh project, plus advanced file management:

* **Initialize Storage:** Create a fresh `tasks.json` tracking file using `-i` or `--init`.
* **Add Tasks:** Create new tasks with an automatic incremental ID, default `todo` status, and timestamps (`createdAt`, `updatedAt`) using `-a [description]`.
* **Update Tasks:** Modify the description of an existing task by providing its ID and the new text via `-u [ID] [DESCRIPTION]`. This automatically updates the `updatedAt` timestamp.
* **Delete Tasks:** Remove a task completely from the system using `-d [ID]`.
* **Mark Status:** Update task progress to `todo`, `in-progress`, or `done` using `-m [ID] [STATUS]`. This automatically updates the `updatedAt` timestamp.
* **Check Status:** Quickly view the current status of a single task using `-s [ID]`.
* **List & Filter:** View all tasks or filter them by status (`todo`, `in-progress`, `done`) using `-l [filter]`.
* **Merge Files:** Combine an external tasks file into your current tracker with automated ID remapping via `-f [file]`.
* **ASCII Art Welcome:** Displays a clean visual logo and help manual when run without arguments.

## Getting Started

1. Download the repository.
2. To run the application, use:
   ```bash
   poetry run python .\src\task_tracker\main.py [args here]

```

or just:

```bash
python .\src\task_tracker\main.py [args here]

```
