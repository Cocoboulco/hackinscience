import datetime
n = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
m = datetime.datetime.strftime(datetime.datetime.now(), '%X')
print("Today is " + n + " and it is " + m)
