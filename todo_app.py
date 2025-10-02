from functools import total_ordering

@total_ordering
class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return (self.priority, self.title) < (other.priority, other.title)

    def __hash__(self):
        return hash(self.title)

    def __repr__(self):
        return f"Task({self.title!r}, {self.priority})"

tasks = [
    Task("Write report", 2),
    Task("Email team", 1),
    Task("Write report", 1),   
    Task("Backup files", 3)
]

u_tasks = set(tasks)

s_tasks = sorted(u_tasks)

print(s_tasks)
