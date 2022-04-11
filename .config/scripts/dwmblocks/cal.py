import calendar
import os
from datetime import datetime
d = datetime.now()
cal = repr(calendar.month(d.year, d.month))
if os.getenv('BUTTON') == '1':
    os.system(f"dunstify 'Calander' {cal}")
print(d.strftime("%b %d (%a) %I:%M:%S %p "))
