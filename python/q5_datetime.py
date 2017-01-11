# Hint:  use Google to find python function
import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'
change = datetime.datetime(2015,7,28)-datetime.datetime(2013,1,1)

day_a = change.days
print("(a) difference: ", day_a)

####b)  
date_start = '12312013'  
date_stop = '05282015'

from datetime import datetime
date_format = "%m%d%Y"
a = datetime.strptime(date_start, date_format)
b = datetime.strptime(date_stop, date_format)
delta = b - a
print('(b) difference: ',delta.days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

from datetime import datetime
date_format = "%d-%b-%Y"
a = datetime.strptime(date_start, date_format)
b = datetime.strptime(date_stop, date_format)
delta = b - a
print('(c) difference: ',delta.days)
##ideally I'd write a function to do this generally or use the timedelta module
