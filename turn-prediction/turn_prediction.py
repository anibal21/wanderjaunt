from datetime import datetime

class Turn:
    created_at = DateField()
    scheduled_for = DateField()
    is_same_day = BooleanField()

    def projected_sameday_turns(date):
        pass

    def projected_turns(date):
        pass
