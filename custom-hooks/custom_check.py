import pathlib
from typing import Generator, List

def find_todo_comments(directory: str) -> Generator[str, None, None]:
    """指定されたディレクトリ内のPythonファイルからTODOコメントを検索します。

    Args:
        directory (str): Pythonファイルを検索するディレクトリ。

    Yields:
        str: TODOコメントを含むPythonファイルの名前。
    """
    path = pathlib.Path(directory)
    for python_file in path.rglob('*.py'):
        if _contains_todo_comment(python_file):
            yield python_file.name

def _contains_todo_comment(python_file: pathlib.Path) -> bool:
    """指定されたPythonファイルにTODOコメントが含まれているかを確認します。

    Args:
        python_file (pathlib.Path): 確認するPythonファイル。

    Returns:
        bool: TODOコメントが含まれている場合はTrue、それ以外はFalse。
    """
    with python_file.open('r', encoding='utf-8') as f:
        content = f.read()
    return 'TODO' in content

def check_files(directory: str) -> int:
    """指定されたディレクトリ内のPythonファイルからTODOコメントをチェックします。

    Args:
        directory (str): Pythonファイルを検索するディレクトリ。

    Returns:
        int: TODOコメントが見つかった場合は1、見つからなかった場合は0を返します。
    """
    todos: List[str] = list(find_todo_comments(directory))
    for todo in todos:
        print(f"Found TODO in {todo}")
    return 1 if todos else 0

if __name__ == '__main__':
    import sys
    directory = sys.argv[1]
    print(f"directory: {directory}")
    sys.exit(check_files(directory))