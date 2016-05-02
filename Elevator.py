MAX_FLOOR_NUMBER = 100
CURRENT_FLOOR = 1
UP_FROM = [0]*MAX_FLOOR_NUMBER
UP_TO = [0]*MAX_FLOOR_NUMBER
DOWN_FROM = [0]*MAX_FLOOR_NUMBER
DOWN_TO = [0]*MAX_FLOOR_NUMBER
MAX_FROM, MAX_TO = 0, 0
UP, DOWN, IDLE = 0, 1, 2
DIRECTION = IDLE
REQUESTS = []
IN_ELEVATOR = []

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


def has_from_request_from_upper_floor():
    _from_list = [req[0] for req in REQUESTS]

    if any(i > CURRENT_FLOOR for i in _from_list):
        return True

    return False


def has_to_request_from_upper_floor():
    _to_list = [req[1] for req in IN_ELEVATOR]

    if any(i > CURRENT_FLOOR for i in _to_list):
            return True

    return False


def has_from_request_from_lower_floor():
    _from_list = [req[0] for req in REQUESTS]

    if any(i < CURRENT_FLOOR for i in _from_list):
        return True

    return False


def has_to_request_from_lower_floor():
    _to_list = [req[1] for req in IN_ELEVATOR]

    if any(i < CURRENT_FLOOR for i in _to_list):
        return True

    return False

def move():
    if DIRECTION == UP:
        go_up()
    elif DIRECTION == DOWN:
        go_down()
