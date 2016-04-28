MAX_FLOOR_NUMBER = 100
CURRENT_FLOOR = 1
UP_FROM = [0]*MAX_FLOOR_NUMBER
UP_TO = [0]*MAX_FLOOR_NUMBER
DOWN_FROM = [0]*MAX_FLOOR_NUMBER
DOWN_TO = [0]*MAX_FLOOR_NUMBER
MAX_FROM, MAX_TO = 0, 0
UP, DOWN, IDLE = 0, 1, 2
DIRECTION = IDLE


def go_up():
    global CURRENT_FLOOR
    max_floor = max(MAX_FROM, MAX_TO)

    if CURRENT_FLOOR >= max_floor:
        return False
    else:
        CURRENT_FLOOR += 1
        return True


def go_down():
    global CURRENT_FLOOR
    CURRENT_FLOOR -= 1

    if CURRENT_FLOOR == 1:
        return False
    else:
        CURRENT_FLOOR -= 1
        return True


def call(_from, _to):
    global MAX_FROM, MAX_TO
    if DIRECTION == UP:
        UP_TO[_to], UP_FROM[_from] = True, True
    else:
        DOWN_TO[_to], DOWN_FROM[_from] = True, True

    MAX_FROM, MAX_TO = max(MAX_FROM, _from), max(MAX_TO, _to)


def run():
    while go_up():
        pass
    while go_down():
        pass
