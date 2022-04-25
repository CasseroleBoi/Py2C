from typing import List
from readFile import readFile

def prepFile(path) -> List[str]:
    unprepared = readFile(path).copy()
    prepared = []
    for line in unprepared:
        #removing trailing newlines
        if line[-1] == '\n':
            line = line[:-1]

        #split lines with semicolons
        lines = line.split(';')
        
        for l in lines:
            if not l.isspace() and len(l) > 0:
                prepared.append(l)

    return prepared
