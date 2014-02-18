from datetime import time
from datetime import date
from datetime import datetime

#Try to import pytz. If not present on system, set equal to 'None' to prevent NameError
try:
    import pytz
except ImportError, e:
    print e
    pytz = None
# This is a Date object for 1/1/2014
print "datetime.date(2014,1,1):", date(2014,1,1)
# This is a Time object for 5:30:30.5 PM, no time zone or date set
print "datetime.time(17,30,30,50):", time(17,30,30,500)
# This is a Datetime object for date and time and the moment it is created
print "datetime.datetime.now():", datetime.now()
# This is a Datetime object for slightly later. Will not change as 'now' changes.
print "datetime.datetime.now():", datetime.now()

#These are some formatting examples.
print "ctime formatting:", datetime.now().ctime()
print "strftime('Hour %H on a %A in %Y'):", datetime.now().strftime('Hour %H on a %A in %Y')

# Check if pytz exists first.
if pytz:
    utc = pytz.utc()
    central = pytz.timezone('US/Central')
    central = pytz.timezone('US/Eastern')
    print "Central time zone now()", central.localize(datetime.now())
    print "Eastern time zone now()", eastern.localize(datetime.now())

    #Display Central time as Eastern time
    dt_cst = central.localize(datetime.now())
    print "Current time in Central time zone:", dt_cst
    print "Current time in Eastern time zone:", dt_cst.astimezone(eastern)
