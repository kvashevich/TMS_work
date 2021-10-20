class Tasklist:
    def __init__(self):
        self.taskes = []

    def show_task(self):
        return self.taskes

    def add_task(self):
        name_task = str(input('What do you want to do? '))
        time_task = str(input('Time for task: '))
        count = len(self.taskes)
        self.taskes.append(f"{count + 1}.{name_task} - {time_task}")
        return 'task adds!'

    def edit_task(self):
        name_task = str(input('which task to edit: '))
        task = [task for task in self.taskes if task.startswith(name_task)][0]
        index_task = self.taskes.index(task)
        etask = input("new name: ")
        time_task = str(input('new time: '))
        self.taskes[index_task] = f"{task.split('.')[0]}.{etask} - {time_task}"
        return 'task edited!'

    def delete_task(self):
        name_task = str(input('which task for delete: '))
        task = [task for task in self.taskes if task.startswith(name_task)][0]
        index_task = self.taskes.index(task)
        self.taskes.pop(index_task)
        return 'Task deleted!'

    def filter_task(self):
        task_filter = str(input('what word to search for? '))
        out_filter = list(filter(lambda x: task_filter in x, self.taskes))
        return "Result for your request: ", out_filter

    def erase_task(self):
        name_task = str(input('which task is done? '))
        task = [task for task in self.taskes if task.startswith(name_task)][0]
        index_task = self.taskes.index(task)
        self.taskes[index_task] = f"{task} (done)"
        return 'task complited'

    def all_done_task(self):
        name_task = str(input('you completed all the tasks? n/y '))
        if name_task == "n":
            pass
        elif name_task == "y":
            for i in range(len(self.taskes)):
                self.taskes[i] += ' (done)'
        return 'task complited'


class Save(Tasklist):
    def __init__(self,taskes):
        super().__init__()

    def save_task(self):
        answer = input('Do you want save new task? ')
        if answer == "ss":
            with open('taski.txt', 'w') as file_taskes:
                filetask = ''
            for task in self.taskes:
                filetask += f'{task}\n'
                file_taskes.write(filetask)
                print('end.')
                break
