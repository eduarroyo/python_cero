from datetime import datetime
def current_date():
    return datetime.now()

def date_diff(date1: str, date2: str):
    d1 = datetime.strptime(date1, "%Y-%m-%dT%H:%M:%S")
    d2 = datetime.strptime(date2, "%Y-%m-%dT%H:%M:%S")
    return d1 - d2;