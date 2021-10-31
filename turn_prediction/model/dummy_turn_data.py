from model.turn import Turn
from pendulum import datetime

timezone = "America/Santiago"

"""
- Case 1:
    Tuesday 2 -> Thursday 4
    2021/11/02 -> 2021/11/04
    2-> 4 -> 6 
"""
case1_data = [
    # The six turns scheduled by now for next day X
    Turn(datetime(2021, 11, 2, tz=timezone),
         datetime(2021, 11, 4, tz=timezone), False),
    Turn(datetime(2021, 11, 2, tz=timezone),
         datetime(2021, 11, 4, tz=timezone), False),
    Turn(datetime(2021, 11, 2, tz=timezone),
         datetime(2021, 11, 4, tz=timezone), False),
    Turn(datetime(2021, 11, 2, tz=timezone),
         datetime(2021, 11, 4, tz=timezone), False),
    Turn(datetime(2021, 11, 2, tz=timezone),
         datetime(2021, 11, 4, tz=timezone), False),
    Turn(datetime(2021, 11, 2, tz=timezone),
         datetime(2021, 11, 4, tz=timezone), False),

    # 1 week before scheduled between the dates
    Turn(datetime(2021, 10, 26, tz=timezone),
         datetime(2021, 10, 28, tz=timezone), False),
    Turn(datetime(2021, 10, 27, tz=timezone),
         datetime(2021, 10, 28, tz=timezone), False),

    # 2 weeks before scheduled between the dates
    Turn(datetime(2021, 10, 19, tz=timezone),
         datetime(2021, 10, 21, tz=timezone), False),
    Turn(datetime(2021, 10, 20, tz=timezone),
         datetime(2021, 10, 21, tz=timezone), False),

    # 3 weeks before scheduled between the dates
    Turn(datetime(2021, 10, 12, tz=timezone),
         datetime(2021, 10, 14, tz=timezone), False),
    Turn(datetime(2021, 10, 13, tz=timezone),
         datetime(2021, 10, 14, tz=timezone), False),

    # 4 weeks before scheduled between the dates
    Turn(datetime(2021, 10, 5, tz=timezone),
         datetime(2021, 10, 7, tz=timezone), False),
    Turn(datetime(2021, 10, 6, tz=timezone),
         datetime(2021, 10, 7, tz=timezone), False)

]


def get_case1():
    return case1_data
