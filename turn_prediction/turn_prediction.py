from pendulum import datetime
from model import dummy_turn_data as get_data
from functools import reduce

"""
+++ Explanation
+ I'll assume:
    - I don't have to mount an entire Django to use a Django model, is not part of the algorithm
    - I can change the solution for what i think is the best
    - This part of the challenge hasn't just a script as output
+ Notes:
    - I won't build the projected_sameday_turns because is the same as projected_turns
"""

"""
+ Algorithm
"""

# This method can be called after query the database


def is_valid_date(original_start, original_end, turn, weeks, iterator):
    iterator += 1
    created_at = turn.created_at
    scheduled_for = turn.scheduled_for
    start = original_start.subtract(weeks=1)
    end = original_end.subtract(weeks=1)

    if(created_at >= start and created_at <= end and scheduled_for == end):
        return True
    elif(iterator < weeks):
        return is_valid_date(start, end, turn, weeks, iterator)
    else:
        return False


def projected_turns(datasource, start, end, weeks):

    if datasource is None:
        return []

    history_schedule = reduce(lambda total, turn: total + 1 if is_valid_date(
        start, end, turn, weeks, 0) else total, datasource, 0)

    current_schedule = reduce(lambda total, turn: total + 1 if turn.created_at ==
                              start and turn.scheduled_for == end else total, datasource, 0)

    average_schedule = history_schedule // (weeks - 1)
    return average_schedule + current_schedule


"""
+ Main
"""
timezone = "America/Santiago"
data = get_data.get_case1()

# Test data
created_at = datetime(2021, 11, 2, tz=timezone)
schedule_date = datetime(2021, 11, 4, tz=timezone)
weeks = 4

response = projected_turns(data, created_at, schedule_date, weeks)

print(f"The projected turn is: {response}")
