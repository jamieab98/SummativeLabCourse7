class User:
    users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
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

class Task:
    tasks = []
    def __init__(self, title):
        self.title = title
        self.assigned_to = []
        self.status = "incomplete"

user1 = User("Jamie", "jamieab98@gmail.com")
User.show_users()