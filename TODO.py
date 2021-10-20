from classforTODO import Tasklist, OperationFileTxt, OperationFileJson

# декоратор на повторение функции
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
    task = Tasklist()
    return print(task.show_task())


@ask_continue
def add():
    task = Tasklist()
    return task.add_task()


@ask_continue
def edit():
    task = Tasklist()
    return task.edit_task()


@ask_continue
def delete():
    task = Tasklist()
    return task.delete_task()


@ask_continue
def _filter():
    task = Tasklist()
    return task.filter_task()


@ask_continue
def erase():
    task = Tasklist()
    return task.erase_task()


def all_done():
    task = Tasklist()
    return task.all_done_task()


def save():

    format = input('Write format\n 1.Txt \n 2.Json')

    if format == '1':
        a = OperationFileTxt()
        return a.save_task()
    elif format == '2':
        a = OperationFileJson()
        return a.save_task()
    return 'task saved'


def open():
    pass

menu =  """
_____________________________
|1| Show task                |
|2| Add task                 |
|3| Edit task                |
|4| Delete task              |
|5| Erase task               |
|6| Filter task              |
|7| Mark all done            |
|8| Save                     |
|9| Open                     |
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
    '9': open,
}


while True:
    print(menu)
    ent = input('Do you want did? ')
    menu_list[ent]()
