import datetime
n = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
m = datetime.datetime.strftime(datetime.datetime.now(), '%H-%M-%S')
print("Today is " +  n + " and it is " + m)
