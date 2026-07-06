from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(title, schedule):
    """Prints a schedule in a readable format."""
    print(f"\n{title}")
    print("-" * len(title))

    if not schedule:
        print("No tasks found.")
        return

    for pet, task in schedule:
        status = "Done" if task.completed else "Pending"
        print(
            f"{task.time} - {pet.name}: {task.description} ({task.frequency}) [{status}]")


def main():
    """Runs a CLI demo of the PawPal+ system."""
    owner = Owner("Cesar")

    dog = Pet("Buddy", "Dog", 3)
    cat = Pet("Luna", "Cat", 2)

    owner.add_pet(dog)
    owner.add_pet(cat)

    dog.add_task(Task("Morning walk", "08:00", "daily"))
    dog.add_task(Task("Give heart medication", "07:30", "daily"))
    cat.add_task(Task("Feed breakfast", "08:00", "daily"))
    cat.add_task(Task("Vet appointment", "14:00", "once"))

    scheduler = Scheduler(owner)

    print_schedule("Today's Schedule", scheduler.get_today_schedule())

    print("\nConflict Warnings")
    print("-----------------")
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for conflict in conflicts:
            print(conflict)
    else:
        print("No conflicts found.")

    scheduler.mark_task_complete("Buddy", "Morning walk")

    print_schedule("Pending Tasks After Completing Buddy's Morning Walk",
                   scheduler.filter_by_status(False))


if __name__ == "__main__":
    main()
