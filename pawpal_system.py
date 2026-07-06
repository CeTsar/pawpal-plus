from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional


@dataclass
class Task:
    # PawPal+ system logic: Owner, Pet, Task, Scheduler
    # Core classes fully implemented with dataclasses
    """Represents a pet care task such as feeding, walking, or medication."""
    description: str
    time: str
    frequency: str = "once"
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def create_next_occurrence(self) -> Optional["Task"]:
        """Creates the next task if this task repeats daily or weekly."""
        frequency_lower = self.frequency.lower()

        if frequency_lower == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif frequency_lower == "weekly":
            next_date = self.due_date + timedelta(weeks=1)
        else:
            return None

        return Task(
            description=self.description,
            time=self.time,
            frequency=self.frequency,
            due_date=next_date,
            completed=False,
        )

    def __str__(self) -> str:
        """Returns a readable task summary."""
        status = "Done" if self.completed else "Pending"
        return f"{self.time} | {self.description} | {self.frequency} | {self.due_date} | {status}"


@dataclass
class Pet:
    """Represents a pet and stores all tasks assigned to that pet."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Returns all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Represents a pet owner who manages multiple pets."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Adds a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[tuple[Pet, Task]]:
        """Returns all tasks across all pets."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))

        return all_tasks


class Scheduler:
    """Organizes, filters, completes, and checks pet care tasks."""
    # Algorithmic layer: sorting, filtering, conflict detection, recurrence

    def __init__(self, owner: Owner):
        """Initializes the scheduler with an owner."""
        self.owner = owner

    def sort_by_time(self) -> List[tuple[Pet, Task]]:
        """Returns all tasks sorted by time."""
        return sorted(self.owner.get_all_tasks(), key=lambda item: item[1].time)

    def filter_by_pet(self, pet_name: str) -> List[tuple[Pet, Task]]:
        """Returns tasks for one pet by name."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if pet.name.lower() == pet_name.lower()
        ]

    def filter_by_status(self, completed: bool) -> List[tuple[Pet, Task]]:
        """Returns tasks based on completion status."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if task.completed == completed
        ]

    def mark_task_complete(self, pet_name: str, task_description: str) -> Optional[Task]:
        """Marks a task complete and creates the next recurring task if needed."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                for task in pet.tasks:
                    if task.description.lower() == task_description.lower() and not task.completed:
                        task.mark_complete()
                        next_task = task.create_next_occurrence()

                        if next_task:
                            pet.add_task(next_task)

                        return task

        return None

    def detect_conflicts(self) -> List[str]:
        """Detects tasks scheduled at the same time."""
        conflicts = []
        seen_times = {}

        for pet, task in self.owner.get_all_tasks():
            key = task.time

            if key in seen_times:
                other_pet, other_task = seen_times[key]
                conflicts.append(
                    f"Conflict at {task.time}: {other_pet.name} has '{other_task.description}' "
                    f"and {pet.name} has '{task.description}'."
                )
            else:
                seen_times[key] = (pet, task)

        return conflicts

    def get_today_schedule(self) -> List[tuple[Pet, Task]]:
        """Returns today's tasks sorted by time."""
        today = date.today()

        todays_tasks = [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if task.due_date == today
        ]

        return sorted(todays_tasks, key=lambda item: item[1].time)
