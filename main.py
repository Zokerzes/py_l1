date = []
task = []
task_list = {}
stop = False
while not stop:
    date_input = input("Введите дату: ")
    task_input = input("Введите задачу: ")
    date.append(date_input)
    task.append(task_input)
    task_list[date_input] = task_input
    for date_key, task_value in task_list.items():
        print(f"{date_key} - {task_value}")
    stop_input = input("Хотите ли добавить еще задачу? (да/нет): ")
    if stop_input.lower() == 'нет':
        stop = True

