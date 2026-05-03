from typing import List

def read_integers() -> List[int]:
    line = input().split(',')
    return [int(value) for value in line]


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
