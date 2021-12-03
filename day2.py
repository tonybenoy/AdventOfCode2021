from typing import List
def get_position(commands: List[str]) -> int:
    horizontal = 0
    aim = 0
    vertical=0
    for cmd in commands:
        to_move, value = cmd.split(" ")
        if to_move == "forward":
            horizontal = horizontal + int(value)
            if aim:
              vertical=vertical+(aim*int(value))
            continue
        if to_move == "down":
            aim = aim + int(value)
            continue
        if to_move == "up":
            aim = aim - int(value)
            continue
    return horizontal * vertical
