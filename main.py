import argparse

parser = argparse.ArgumentParser(description="Manage Users and Projects")

subparsers = parser.add_subparsers(dest="command")

add_user = subparsers.add_parser("add_user")
add_user.add_argument("user", type=str)

list_projects = subparsers.add_parser("list_projects")
list_projects.add_argument("user", type=str)

complete_task = subparsers.add_parser("complete_task")
complete_task.add_argument("user", type=str)
complete_task.add_argument("task", type=str)

args = parser.parse_args()

if args.command == "add_user":
    print(f"adding {args.user} to the database")

if args.command == "list_projects":
    print(f"listing {args.user}'s projects")

if args.command == "complete_task":
    print(f"{args.user} completed the following task: {args.task}")