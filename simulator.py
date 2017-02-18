import time
import math

DOOR_OPENING_TIME = 1.6
DOOR_CLOSING_TIME = 2.5
DOOR_OPEN_TIME = 2
FLOOR_HEIGHT = 3.9
FLOOR_COUNT = 10
CAR_SPEED = 1.9
TIME_TO_HALT = 0.5
UP = 1
DOWN = -1
STOP = 0


def set_motion(motion,floor_max,floor_min,curr_floor):
        if motion == UP and floor_max < curr_floor:
            motion = DOWN
        elif motion == DOWN and floor_min > curr_floor:
            motion = UP
        elif motion == STOP:
            if math.fabs(floor_max-curr_floor) > math.fabs(curr_floor-floor_min):
                motion = DOWN
            else:
                motion = UP
        return motion


def lift_simulator(starting_floor, curr_floor, floor_list):
    motion = UP

    if curr_floor < starting_floor:
        motion = DOWN

    while floor_list.__len__() != 0:

        if curr_floor in floor_list:
            print(2*TIME_TO_HALT+DOOR_OPENING_TIME+DOOR_OPEN_TIME+DOOR_CLOSING_TIME)
            time.sleep(TIME_TO_HALT)
            print(curr_floor)
            floor_list.pop(floor_list.index(curr_floor))

            time.sleep(DOOR_OPENING_TIME+DOOR_OPEN_TIME+TIME_TO_HALT+DOOR_CLOSING_TIME)
        else:
            print(curr_floor)
        time.sleep(FLOOR_HEIGHT/CAR_SPEED)

        if floor_list.__len__() != 0:
            motion = set_motion(motion,max(floor_list),min(floor_list),curr_floor)
        curr_floor += motion


def estimated_time_of_arrival(curr_lift_floor, motion, floor_list, display_floor):
    lst = []
    estimated_time = 0
    if motion == UP:
        if curr_lift_floor < display_floor:
            lst.extend([x for x in floor_list if x < display_floor and x >= curr_lift_floor])
            cnt_in_btwn_floors = display_floor - curr_lift_floor
        else:
            lst.extend([x for x in floor_list if x > display_floor ])
            cnt_in_btwn_floors = 2*(max(floor_list) - curr_lift_floor) + curr_lift_floor - display_floor

    elif motion == DOWN:
        if curr_lift_floor > display_floor:
            lst.extend([x for x in floor_list if x > display_floor and x <= curr_lift_floor])
            cnt_in_btwn_floors = curr_lift_floor - display_floor
        else:
            lst.extend([x for x in floor_list if x < display_floor])
            cnt_in_btwn_floors = 2 * (curr_lift_floor - min(floor_list)) + curr_lift_floor - display_floor

    else:
        cnt_in_btwn_floors = math.fabs(curr_lift_floor-display_floor)
        estimated_time += TIME_TO_HALT

    no_stops = len(lst)

    estimated_time += cnt_in_btwn_floors*(FLOOR_HEIGHT/CAR_SPEED)
    estimated_time += no_stops * (2 * TIME_TO_HALT + DOOR_OPENING_TIME + DOOR_OPEN_TIME + DOOR_CLOSING_TIME)
    return estimated_time

# lift_simulator(0, 3, [1, 5, 6, 7])
print(estimated_time_of_arrival(3, STOP, [], 8))
