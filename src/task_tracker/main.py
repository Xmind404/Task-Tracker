import argparse
import actions

def draw_ascii():
    return """
████████╗ █████╗ ███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗███████╗██████╗ 
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
   ██║   ███████║███████╗█████╔╝    ██║   ██████╔╝███████║██║     █████╗  ██████╔╝
   ██║   ██╔══██║╚════██║██╔═██╗    ██║   ██╔══██╗██╔══██║██║     ██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████║██║  ██╗   ██║   ██║  ██║██║  ██║╚██████╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
    """

def main():
    parser = argparse.ArgumentParser(
        description="Task Tracker CLI - Manage your daily tasks efficiently.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("-i", "--init", action="store_true", help="initialize tasks")
    parser.add_argument("-a", "--add", type=str, help="add new task")
    parser.add_argument("-u", "--update", nargs=2, metavar=('ID', 'NAME'), help="update task: provide ID and new name")
    parser.add_argument("-d", "--delete", type=int, help="delete task")
    parser.add_argument("-m", "--mark", nargs=2, metavar=('ID', 'STATUS'), help="mark task: provide ID and status")
    parser.add_argument("-s", "--status", type=int, help="show task status")
    parser.add_argument("-l", "--list", nargs='?', const='all', help="show task list (optional filter: todo, in_progress, done)")
    parser.add_argument("-f", "--file", type=str, help="join tasks file")
    parser.add_argument("-e", "--export", type=str, help="export tasks file")
    args = parser.parse_args()

    if args.init:
        actions.init()

    elif args.add is not None:
        actions.add(args.add)

    elif args.update is not None:
        actions.update(int(args.update[0]), args.update[1])

    elif args.delete is not None:
        actions.delete(args.delete)

    elif args.mark is not None:
        actions.mark(int(args.mark[0]), args.mark[1])

    elif args.status is not None:
        actions.status(args.status)

    elif args.list is not None:
        actions.list_tasks(args.list)

    elif args.file is not None:
        actions.join_file(args.file)

    else:
        print(draw_ascii())
        parser.print_help()

if __name__ == "__main__":
    main()