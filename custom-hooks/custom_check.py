import subprocess
import sys


def check_todo_comments(filename):
    result = subprocess.run(
        ["grep", "-n", "TODO", filename], capture_output=True, text=True
    )
    if result.stdout:
        print(f"Found TODO comments in {filename}:")
        print(result.stdout)
        return 1
    return 0


def main():
    failed = False
    for filename in sys.argv[1:]:
        if filename.endswith(".py"):
            if check_todo_comments(filename) != 0:
                failed = True

    if failed:
        print("Commit rejected: Please resolve TODO comments before committing.")
        sys.exit(1)


if __name__ == "__main__":
    main()
