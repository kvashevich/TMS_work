menu = """
1. Show task     2. Add task     3. Edit task  4. Delete task
5. Erase task    6. Filter task  7. Mark all done

8. Exit and save taskes
\n """

taskes = []


def ask_continue(func):
    def wrapper(*args, **kwargs):
        func()
        ask_con = input('Do you want did again?(y/n) ')
        while True:
            if ask_con == 'y':
                wrapper()
            else:
                return ''

    return wrapper


def check():
    for task in taskes:
        print(task)
    return


@ask_continue
def add():
    name_task = str(input('What do you want to do? '))
    if name_task == 'menu':
        answer = ''
    time_task = str(input('Time for task: '))
    if time_task == "menu":
        answer = ''
    else:
        count = len(taskes)
        taskes.append(f"{count + 1}.{name_task} - {time_task}")
        answer = 'task adds!'
    return answer


@ask_continue
def edit():
    name_task = str(input('which task to edit? '))
    if name_task == "menu":
        answer = ''
    else:
        task = [task for task in taskes if task.startswith(name_task)][0]
        index_task = taskes.index(task)
        etask = input("new name: ")
        time_task = str(input('new time: '))
        taskes[index_task] = f"{task.split('.')[0]}.{etask} - {time_task}"
        answer = 'task edited!'
    return answer


@ask_continue
def delete():
    name_task = str(input('which task to delete? '))
    if name_task == "menu":
        answer = ''
    else:
        task = [task for task in taskes if task.startswith(name_task)][0]
        index_task = taskes.index(task)
        taskes.pop(index_task)
        answer = 'Task deleted!'
    return answer


@ask_continue
def filter_task():
    task_filter = str(input('what word to search for? '))
    out_filter = list(filter(lambda x: task_filter in x, taskes))
    return print("Result for your request: ", out_filter)


@ask_continue
def erase():
    name_task = str(input('which task is done? '))
    if name_task == "menu":
        answer = ''
    else:
        task = [task for task in taskes if task.startswith(name_task)][0]
        index_task = taskes.index(task)
        taskes[index_task] = f"{task} (done)"
        answer = 'task complited'
    return answer


@ask_continue
def all_done():
    name_task = str(input('you completed all the tasks? n/y '))
    answer = ''
    if name_task == "n" or name_task == "menu":
        pass
    elif name_task == "y":
        for i in range(len(taskes)):
            taskes[i] += ' (done)'
            answer = 'task complited'
    return answer


def exit_end():
    answer = input('Do you want save new task? ')
    if answer == "ss":
        with open('taski.txt', 'w') as file_taskes:
            filetask = ''
        for task in taskes:
            filetask += f'{task}\n'
            file_taskes.write(filetask)
            print('end.')
            break


menu_list = {
    '1': check,
    '2': add,
    '3': edit,
    '4': delete,
    '5': erase,
    '6': filter_task,
    '7': all_done,
    '8': exit_end,
}

while True:
    if not taskes:
        with open('taski.txt') as file_task:
            for task in file_task.readlines():
                taskes.append(task.strip())
    print(menu)
    ent = input('Do you want did? ')
    menu_list[ent]()