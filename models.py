class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.projects = []
    
    def __repr__(self):
        return self.username
    
    def add_project(self, project):
        self.project = project
        self.projects.append(self.project)
    
class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
    
    def add_task(self, task):
        self.task = task
        self.tasks.append(self.task)
    
    def __repr__(self):
        return self.title

class Task:
    def __init__(self, title):
        self.title = title
        self.status = "Incomplete"
        self.assigned_to = []
    
    def __repr__(self):
        return self.task_name

user1 = User("Jamie Bryson", "jamieab98@gmail.com")
user2 = User("Michael Bedford", "pookgoog@yahoo.com")
user3 = User("Bobby Gunshefski", "bobbyg44@gmail.com")

project1 = Project("Build Website")
project2 = Project("Make Jamie Happy")
project3 = Project("Go to Frisbee Nationals")

task1 = Task("Create FrontEnd")
task2 = Task("Create Backend")
task3 = Task("Runs Sprints")
task4 = Task("Make Toro")
task5 = Task("Go to the Bar")
task6 = Task("Get Chipotle")