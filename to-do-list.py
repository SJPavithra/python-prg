to_do_list = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(to_do_list, 1):
        print(f"{i}. {task}")

    action = input("\nEnter 'add' to add a task, 'remove' to remove a task, or 'quit' to exit: ").lower()

    if action == 'add':
        task = input("Enter a task: ")
        to_do_list.append(task)
    elif action == 'remove':
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(to_do_list):
            to_do_list.pop(task_num - 1)
        else:
            print("Invalid task number!")
    elif action == 'quit':
        break
    else:
        print("Invalid action!")
