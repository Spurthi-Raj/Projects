from datetime import datetime

TIME_FORMAT = "%H:%M:%S"

def now():
    return datetime.now()
    
def validate_time(s):
    try:
        datetime.strptime(s,TIME_FORMAT)
        return True
    except ValueError:
        return False


def parse_time(s):
    t= datetime.strptime(s,TIME_FORMAT)
    n = now()
    return n.replace(hour = t.hour,minute=t.minute,second=t.second,microsecond=0)

def is_future_time(time_str):
    return parse_time(time_str) > now()