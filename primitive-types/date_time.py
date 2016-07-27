"""
All datetime objects are immutable.
datetime type modles: year, month, day, hour, minute, second, microsecond
date : year, month, day
time : hour, minute, second, microsecond; it has a naive/aware mode for tzinfo (timezone)
timedelta: days, seconds, seconds 
"""
from datetime import date, time, timedelta, timezone, datetime as dt # compound type 

################### date type ##################
d1 = date(1983, 10, 5)
print(d1)
print(type(d1))

print(date.today())
print(date.fromtimestamp(1000000000)) # from number of seconds
print(date.fromordinal(700000)) # from number of days

# useful instance methods on date 
print(d1.month) # also has year, day 
print(d1.weekday()) # 0 based 0 = Monday, 6 = Sunday
print(d1.isoweekday()) # 1 based; 1 = Monday, 7 = Sunday
d2 = date(1983, 3, 28)
print(d2.isoweekday())
print(d1.isoformat()) # iso format 

# these two are not portable as it depends on each underlying os version
print(d1.strftime('%A %d %B %Y'))
print("{:%A %d %B %Y}".format(d2))

# this is more pythonic and portable by choosing date-specific formatting operators and date attribute access for each component
# note that there cannot be white space betweeen the variable and formatter.
print("{date:%A} {date.day} {date:%B} {date:%Y}".format(date = d1))

# min, max, and interval of date
print(date.min, date.max)
print(date.resolution) # this returns a type of timedelta


################ time type ###################
#ctor order is hour, minute, sec and microsecond
t1 = time(22, 35, 45, 4494)
print(t1)
print(t1.minute) # other attributes are also available
print(t1.isoformat()) # iso format of time 

# similarly separate component formatting is better
print("{t.hour}h{t.minute}m{t.second}s".format(t = t1))

# min, max, and resolution
print(time.min, time.max, time.resolution)


############# datetime compund type ##############
print(dt(1983, 10, 5, 8, 30, 23, 49248))
print(dt.now()) # also has today()
print(dt.utcnow()) # this is naive utc time without knowing the timezone 
print(dt.fromordinal(513456)) # from number of days
print(dt.fromtimestamp(123456789)) # from number of seconds
print(dt.utcfromtimestamp(123456789)) # navid utc datetime

# combine a date with a time
d = dt.today()
t = time(8, 30)
d3 = dt.combine(d, t)
print(d3)
d4 = dt.strptime("Monday 28 March 1983, 2:30:48", "%A %d %B %Y, %H:%M:%S") # string-parse-time 
print(d4)
print(d4.isoformat()) # iso 8601 datetimes

# date() and time(), day on datetime compound type 
print(d4.date())
print(d4.time())
print(d4.day) # attribute 


############## timedelta type ################
td = timedelta(microseconds = 1000, seconds = 39, minutes = 42) # strongly recommend use keyword argument in ctor 
print(td) 
print(td.days) # other attributes exist too
# no format methods on timedelta; use str or repr 
print(repr(td))

##### Arithmetic on datetime results timedelta; arithmetic is not supported on time type!
ddiff = d1 - d2
print(ddiff)
print(ddiff.total_seconds()) # convert timedelta into seconds 
print(d3 - d4)
# 3 weeks later
print(date.today() + timedelta(weeks = 1) * 3)




################ timezone ###############
# normally better use 3rd party pytz or dateutil modules. native support of timezone is relatively limited.


########## floating point vs rational numbers ###########
def sign(x):
    '''Determine the sign of a given number
    
    Args:
        x : The number to be decided the sign on
    Returns:
        1 if x is positive
        0 if x is 0
        -1 if x is negative 
    '''
    return (x > 0) - (x < 0) # this uses False = 0, True = 1