class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.p=PrioritizedItem()
        for t in tasks:
            self.p.add_task(t[0], t[1], t[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.p.add_task(userId, taskId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.p.entry_finder[taskId][3]
        self.p.add_task(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        self.p.remove_task(taskId)

    def execTop(self) -> int:
        return self.p.pop_task()



class PrioritizedItem:

    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = '<removed-task>'      # placeholder for a removed task
        self.counter = itertools.count()     # unique sequence count

    def add_task(self, user, task, priority):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [-priority, count, task, user]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[2] = self.REMOVED

    def pop_task(self):
        'Remove and return the highest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task, user = heappop(self.pq)
            if task != self.REMOVED:
                del self.entry_finder[task]
                return user
        raise KeyError('pop from an empty priority queue')



# Example usage:
# obj = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
# obj.add(4, 104, 25)
# obj.edit(102, 5)
# obj.rmv(103)
# user_id = obj.execTop()  # Returns userId of highest priority task
# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()