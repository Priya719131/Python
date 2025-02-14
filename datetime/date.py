import datetime as dt
day = dt.date(2016,7,24)
print(day)

today=dt.date.today()
print(today)

print(today.year,today.day,today.weekday(),today.isoweekday())

#today.isoweekday() ----- monday-1 , sun-7
#today.weekday() ----- monday-0 , sun-6

tdelta = dt.timedelta(days=7)
print(today+tdelta)

bday = dt.date(2025,4,26)
tillbday=bday-today
print(tillbday)
print(tillbday.days,tillbday.total_seconds())

t=dt.time(9,30,45,60000)
print(t)

tp=dt.datetime(2016,7,26,9,30,45,60000)
print(tp)

print(dt.datetime.today())
print(dt.datetime.now())
print(dt.datetime.utcnow())