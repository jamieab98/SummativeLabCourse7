import argparse

parser = argparse.ArgumentParser(description = "Module 7 Summative Lab CLI")
subparsers = parser.add_subparsers(dest="command")

add_user = subparsers.add_parser("add_user", help = "add new user")
add_user.add_argument("username")

list_projects = subparsers.add_parser("list_projects", help = "list projects")
list_projects.add_argument("username")

complete_task = subparsers.add_parser("complete_task", help = "mark task as complete")
complete_task.add_argument("username")
complete_task.add_argument("task")

args = parser.parse_args()

if args.command == "add_user":
    print(f"Adding {args.username}")
elif args.command == "list_projects":
    print("List of projects")
elif args.command == "complete_task":
    print(f"{args.task} was completed by {args.username}")