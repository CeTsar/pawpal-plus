# PawPal+ Reflection

---

## System Design

### Three Core Actions

The three main actions a user should be able to perform in PawPal+ are:

1. Add a pet to their owner profile.
2. Schedule care tasks for each pet, such as feeding, walking, medication, or appointments.
3. View today's schedule in an organized way so they know what tasks need to be completed.

---

## 1a. Initial Design

For my initial design, I chose four main classes: `Owner`, `Pet`, `Task`, and `Scheduler`.

The `Owner` class represents the person using the app. It stores a list of pets and provides a way to add pets or retrieve all tasks across all pets.

The `Pet` class represents an individual pet. It stores the pet's name, species, age, and list of tasks.

The `Task` class represents a single pet care activity. It stores the task description, time, frequency, due date, and completion status.

The `Scheduler` class acts as the main logic layer. It organizes tasks, sorts them by time, filters them, marks tasks complete, handles recurring tasks, and detects conflicts.

I chose this structure because each class has a clear responsibility. This made the system easier to build, test, and explain.

---

## 1b. Design Changes

One design change I made was putting most of the scheduling logic inside the `Scheduler` class. This helped keep the `Owner` and `Pet` classes simple. The owner and pet classes mainly store information, while the scheduler handles sorting, filtering, completion, recurrence, and conflict detection.

Another change was adding recurrence behavior to the `Task` class through the `create_next_occurrence()` method. This made sense because each task knows its own frequency. When a daily or weekly task is completed, the system can create the next version of that task.

---

## 2b. Tradeoffs

One tradeoff in my scheduler is that conflict detection only checks for exact time matches. For example, if Buddy has a walk at 8:00 and Luna has breakfast at 8:00, the system flags a conflict. However, it does not check for overlapping time ranges, such as one task from 8:00 to 8:30 and another task from 8:15 to 8:45.

I chose this simpler approach because it keeps the algorithm easy to understand and matches the lightweight scheduling goal of the project. A future version could add task durations and detect overlapping time windows.

---

## Testing Reflection

I tested the main behavior of the system using both a CLI demo and automated pytest tests.

The CLI demo helped me confirm that the classes worked together correctly. It created an owner, added pets, added tasks, printed today's schedule, detected a conflict, and marked a task as complete.

The pytest suite helped verify important behaviors in a repeatable way. The tests covered task completion, adding tasks to a pet, sorting tasks by time, daily recurrence, and conflict detection.

All tests passed, which gave me more confidence that the system works correctly.

---

## AI Strategy Reflection

The most helpful AI coding assistant features were brainstorming the class design, creating a UML diagram, scaffolding the Python classes, and generating tests. AI helped turn the project requirements into smaller steps that were easier to complete.

One AI suggestion I would be careful with is making the system too complex. It would be possible to add advanced features like task durations, reminders, notifications, databases, or user authentication. I chose to keep the project focused on the required OOP and scheduling features so the code stayed clean and understandable.

Using separate phases helped me stay organized. I focused first on design, then implementation, then algorithms, then testing, and finally documentation. This made it easier to check my work at each step.

I learned that being the lead architect means I still need to make the final decisions. AI can suggest code and ideas, but I need to understand the system, verify the results, and take responsibility for the final product.
