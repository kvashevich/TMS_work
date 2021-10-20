from classforTODO import OperationFileTxt


# def exit_end():
#     answer = input('Do you want save new task? ')
#     if answer == "ss":
#         with open('taski.txt', 'w') as file_taskes:
#             filetask = ''
#         for task in taskes:
#             filetask += f'{task}\n'
#             file_taskes.write(filetask)
#             print('end.')
#             break


def ask_continue(func):
    def wrapper(*args, **kwargs):
        print(func())
        while True:
            ask_con = input('Do you want did again?(y/n) ')
            if ask_con == 'y':
                print(func())
            else:
                break

    return wrapper


def show():
    return print(task.show_task())


@ask_continue
def add():
    return task.add_task()


@ask_continue
def edit():
    return task.edit_task()


@ask_continue
def delete():
    return task.delete_task()


@ask_continue
def _filter():
    return task.filter_task()


@ask_continue
def erase():
    return task.erase_task()


def all_done():
    return task.all_done_task()


def save():
    return task.save_task()


menu = """
_____________________________
|1| Show task                |
|2| Add task                 |
|3| Edit task                |
|4| Delete task              |
|5| Erase task               |
|6| Filter task              |
|7| Mark all done            |
|8| Save                     |
| |                          |
| |                          |
|____________________________|
\n """



menu_list = {
    '1': show,
    '2': add,
    '3': edit,
    '4': delete,
    '5': erase,
    '6': _filter,
    '7': all_done,
    '8': save,
}

task = Save()
while True:
    print(menu)
    ent = input('Do you want did? ')
    menu_list[ent]()
