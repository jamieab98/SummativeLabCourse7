class User:
    users = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects=[]
        User.users.append(self)

    '''def __repr__(self):
        return self.name'''
    
    def assign_project(self, project):
        self.projects.append(project)

class Project:
    projects = []
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
        Project.projects.append(self)
    
    '''def __repr__(self):
        return self.title'''
    
    def assign_task(self, task):
        self.tasks.append(task)

class Task:
    tasks = []
    def __init__(self, title, project):
        self.title = title
        self.status = "incomplete"
        project.tasks.append(self)
        Task.tasks.append(self)
    
    '''def __repr__(self):
        return self.title'''


user1 = User("Jamie", "jamieab98@gmail.com")

project1 = Project("Classwork", "Complete Summative Lab", "09/09/1998")
project2 = Project("Career", "Get a new Job", "1/1/2027")

task1 = Task("Create the Models", project1)
task2 = Task("Create the logic for the script", project1)
task3 = Task("Complete Flatiron Software Development Bootcamp", project2)
task4 = Task("Apply for coding classes at work", project2)
task5 = Task("Make more money", project2)

user1.assign_project(project1)
user1.assign_project(project2)
