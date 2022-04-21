import calendar
import os
from datetime import datetime
d = datetime.now()
cal = repr(calendar.month(d.year, d.month))
os.system(f"dunstify 'Calander' {cal}")
