from datetime import date, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler

# Automated test suite for PawPal+ system


def test_task_completion():
    task = Task("Feed breakfast", "08:00")

    task.mark_complete()

    assert task.completed is True


def test_task_addition_to_pet():
    pet = Pet("Buddy", "Dog", 3)
    task = Task("Morning walk", "08:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_sorting_correctness():
    owner = Owner("Cesar")
    pet = Pet("Buddy", "Dog", 3)

    pet.add_task(Task("Evening walk", "18:00"))
    pet.add_task(Task("Breakfast", "07:00"))
    pet.add_task(Task("Medication", "12:00"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    times = [task.time for pet, task in sorted_tasks]

    assert times == ["07:00", "12:00", "18:00"]


def test_daily_recurrence_creates_next_task():
    owner = Owner("Cesar")
    pet = Pet("Buddy", "Dog", 3)

    task = Task("Morning walk", "08:00", "daily", due_date=date.today())
    pet.add_task(task)
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    scheduler.mark_task_complete("Buddy", "Morning walk")

    assert len(pet.tasks) == 2
    assert pet.tasks[1].due_date == date.today() + timedelta(days=1)
    assert pet.tasks[1].completed is False


def test_conflict_detection():
    owner = Owner("Cesar")

    dog = Pet("Buddy", "Dog", 3)
    cat = Pet("Luna", "Cat", 2)

    dog.add_task(Task("Morning walk", "08:00"))
    cat.add_task(Task("Feed breakfast", "08:00"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "Conflict at 08:00" in conflicts[0]
