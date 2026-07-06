# PawPal+

PawPal+ is a smart pet care management system that helps pet owners organize daily routines such as feedings, walks, medications, and appointments. The project uses Python object-oriented programming to model owners, pets, tasks, and scheduling logic.

---

## Project Overview

This project was built using a CLI-first workflow. The backend logic was developed in `pawpal_system.py` first, then tested through `main.py` and an automated pytest suite.

The main goal of PawPal+ is to help a pet owner manage multiple pets and keep track of important pet care tasks in an organized way.

---

## Core User Actions

A user should be able to:

1. Add pets to an owner profile.
2. Add care tasks for each pet.
3. View a daily schedule of tasks sorted by time.
4. Mark tasks as complete.
5. See warnings when tasks are scheduled at the same time.

---

## Features

- Create an owner profile
- Add multiple pets
- Add tasks for each pet
- Track task descriptions, times, frequency, due dates, and completion status
- View today's schedule
- Sort tasks by scheduled time
- Filter tasks by pet name
- Filter tasks by completion status
- Mark tasks as complete
- Automatically create the next occurrence for daily and weekly recurring tasks
- Detect basic scheduling conflicts

---

## System Architecture

PawPal+ uses four main classes:

### `Task`

Represents a single pet care activity, such as feeding, walking, medication, or an appointment.

**Responsibilities:**

- Store task details
- Track completion status
- Mark a task complete
- Create the next occurrence for recurring tasks

### `Pet`

Represents one pet.

**Responsibilities:**

- Store pet details
- Store that pet's tasks
- Add new tasks

### `Owner`

Represents the pet owner.

**Responsibilities:**

- Store multiple pets
- Add pets
- Retrieve all tasks across all pets

### `Scheduler`

Acts as the main scheduling brain of the system.

**Responsibilities:**

- Sort tasks by time
- Filter tasks by pet
- Filter tasks by completion status
- Mark tasks complete
- Create recurring tasks
- Detect scheduling conflicts
- Return today's schedule

---

## Smarter Scheduling

The `Scheduler` class contains the algorithmic logic for the project.

### Sorting

`Scheduler.sort_by_time()` sorts all tasks by their `time` attribute in chronological order.

### Filtering

`Scheduler.filter_by_pet()` returns tasks for a specific pet.

`Scheduler.filter_by_status()` returns tasks based on whether they are complete or pending.

### Recurring Tasks

`Scheduler.mark_task_complete()` marks a task as complete. If the task has a frequency of `daily` or `weekly`, the system automatically creates the next occurrence.

### Conflict Detection

`Scheduler.detect_conflicts()` checks whether two tasks are scheduled for the exact same time. If a conflict is found, the system returns a warning message instead of crashing.

---

## Demo Walkthrough

A user can create an owner, add pets, assign tasks to those pets, and view a daily schedule. In the CLI demo, the owner has two pets: Buddy and Luna.

**Example workflow:**

1. Create an owner named Cesar.
2. Add Buddy the dog and Luna the cat.
3. Add several tasks with different times.
4. Print today's schedule.
5. Detect conflicts.
6. Mark one task as complete.
7. View the remaining pending tasks.

### Sample CLI Output

```text
Today's Schedule
----------------
07:30 - Buddy: Give heart medication (daily) [Pending]
08:00 - Buddy: Morning walk (daily) [Pending]
08:00 - Luna: Feed breakfast (daily) [Pending]
14:00 - Luna: Vet appointment (once) [Pending]

Conflict Warnings
-----------------
Conflict at 08:00: Buddy has 'Morning walk' and Luna has 'Feed breakfast'.

Pending Tasks After Completing Buddy's Morning Walk
---------------------------------------------------
07:30 - Buddy: Give heart medication (daily) [Pending]
08:00 - Buddy: Morning walk (daily) [Pending]
08:00 - Luna: Feed breakfast (daily) [Pending]
14:00 - Luna: Vet appointment (once) [Pending]
```

---

## Testing PawPal+

To run the automated tests:

```bash
python -m pytest
```

The test suite covers:

- Task completion
- Adding a task to a pet
- Sorting tasks by time
- Daily recurrence logic
- Conflict detection

### Successful Test Output

```text
=============================================================== test session starts ================================================================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\Abraham The Cesar\codepath pawpal-plus
collected 5 items

tests\test_pawpal.py .....                                                                                                                    [100%]

================================================================ 5 passed in 0.02s =================================================================
```

### Confidence Level

★★★★☆

I am confident that the core PawPal+ scheduling system works because the CLI demo runs successfully and all automated tests pass. The system handles the main requirements, including sorting, filtering, recurrence, and conflict detection. A future improvement would be detecting overlapping task durations instead of only checking exact matching times.

---

## How to Run

Run the CLI demo:

```bash
python main.py
```

Run the tests:

```bash
python -m pytest
```
