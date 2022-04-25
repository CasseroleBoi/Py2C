import ast
from typing import List


def read(path) -> ast.Module:
    return ast.parse(raw(path))

def write(path, value: List[str]):
    with open("test_sources\\"+path, 'r') as file:
        file.writelines(value)

def raw(path) -> List[str]:
    with open("test_sources\\"+path, 'r') as file:
        return file.read()
