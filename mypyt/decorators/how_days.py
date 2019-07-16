from datetime import datetime, date
from functools import wraps

def decor_time(fun):
    
    @wraps(fun)
    def cover(*argc, **argv):
        start = datetime.now()
        res = fun(*argc, **argv)
        finish = datetime.now()
        restime = finish - start
        print(res, finish)
    return cover
    
@decor_time
def my_days(day, month, year):
    birthday = date(year, month, day)
    now_date = date.today()
    all_life_time = now_date - birthday
    return all_life_time.days

my_days(17, 9, 1998)
