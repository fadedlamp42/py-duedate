import pandas as pd
import sys, os
from datetime import date, datetime

file = os.path.expanduser("~/hw.txt")
if os.stat(file).st_size != 0:
    data = pd.read_csv(
        file,
        sep='|',
        skip_blank_lines=True,
        skipinitialspace=True,
        parse_dates=[1])
else:
    print("hw.txt is empty!")
    sys.exit(0)

datetime.today()

def days_until(due):
    return (due - datetime.today()).days + 1

for _, r in data.iterrows():
    task=r[0]
    required = r[2]
    due=datetime.strptime(r[1], "%A %m/%d ")
    due = due.replace(year=date.today().year)
    days = days_until(due)
    if(days<=required):
        print(f"{days} day{'' if days==1 else 's'} until {task}({required} needed)")
