from datetime import date, timedelta
import easygui

holidays = [date(2020, 9, 7), date(2020, 9, 4)
           ]
vacation = []#date(2020, 1, 31),]

def daterange(date1, date2):
    for n in range( int((date2 - date1).days) + 1):
        if n not in holidays:
            yield date1 + timedelta(n)

def return_day(y, z):
    x = y + timedelta(days=z)
    if x.weekday() in range(0, 6):
        return x
    elif x.weekday() == 5:
        return return_day(y + timedelta(days=2), z)
    else:
        return return_day(y + timedelta(days=1), z)

def vaca(return_date):
    return len([x for x in daterange(date.today(), return_date) if x not in holidays and x.weekday() < 5 and x not in vacation])

easygui.msgbox(msg=str(vaca(date(2020, 9, 28))) + " work days until return (Sept 28)")
