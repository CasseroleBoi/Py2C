from typing import List


def readFile(path) -> List[str]:
    with open(path, 'r') as file:
        lines = file.readlines()
        return lines