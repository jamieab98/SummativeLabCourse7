class User:
    users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects=[]
        User.users.append(self)

    def __repr__(self):
        return self.name
    
    def show_users():
        for user in User.users:
            print(user)

class Project:
    projects = []
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        Project.projects.append(self)
    
    def __repr__(self):
        return self.title

class Task:
    tasks = []
    def __init__(self, title):
        self.title = title
        self.assigned_to = []
        self.status = "incomplete"
        Task.tasks.append(self)
    
    def __repr__(self):
        return self.title

user1 = User("Jamie", "jamieab98@gmail.com")

project1 = Project("Classwork", "Complete Summative Lab", "09/09/1998")