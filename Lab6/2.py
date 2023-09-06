from threading import Thread
from queue import Queue


class Task:
    def __init__(self, num):
        self.description = "Task " + str(num)
        self.num = num


def process_tasks(q):
    while True:
        next_task = q.get()
        print("Processing task: ", next_task.description)
        q.task_done()


N = 10
q = Queue(N)
for i in range(N):
    q.put(Task(i))
workers = [Thread(target=process_tasks, args=(q,)), Thread(target=process_tasks, args=(q,)), ]
for w in workers:
    w.Daemon = True
    w.start()

q.join()
