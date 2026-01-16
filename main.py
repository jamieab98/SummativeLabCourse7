import argparse
import json
from models import User, Project, Task

parser = argparse.ArgumentParser(description="Manage Users and Projects")

subparsers = parser.add_subparsers(dest="command")

add_user = subparsers.add_parser("add_user")
add_user.add_argument("name", type=str)
add_user.add_argument("email", type=str)

list_projects = subparsers.add_parser("list_projects")
list_projects.add_argument("user", type=str)

complete_task = subparsers.add_parser("complete_task")
complete_task.add_argument("user", type=str)
complete_task.add_argument("task", type=str)

args = parser.parse_args()

if args.command == "add_user":
    u = User(args.name, args.email)
    dict = {"name": u.name, "email": u.email, "projects": []}
    with open("data/userdata.json", "r") as f:
        data = json.load(f)
    data.append(dict)
    with open("data/userdata.json", "w") as f:
        json.dump(data, f, indent=2)

if args.command == "list_projects":
    print(f"listing {args.user}'s projects")

if args.command == "complete_task":
    print(f"{args.user} completed the following task: {args.task}")