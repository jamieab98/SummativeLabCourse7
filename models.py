class User:
    def __init__(self, username):
        self.username = username
        self.projects = []
    
    def __repr__(self):
        return self.username
    
    def add_project(self, project):
        self.project = project
        self.projects.append(self.project)
    
class Project:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = []
    
    def add_task(self, task):
        self.task = task
        self.tasks.append(self.task)
    
    def __repr__(self):
        return self.project_name

class Task:
    def __init__(self, task_name):
        self.task_name = task_name
        self.complete = False
    
    def __repr__(self):
        return self.task_name

user1 = User("Jamie Bryson")
user2 = User("Michael Bedford")
user3 = User("Bobby Gunshefski")

project1 = Project("Build Website")
project2 = Project("Make Jamie Happy")
project3 = Project("Go to Frisbee Nationals")

task1 = Task("Create FrontEnd")
task2 = Task("Create Backend")
task3 = Task("Runs Sprints")
task4 = Task("Make Toro")
task5 = Task("Go to the Bar")
task6 = Task("Get Chipotle")