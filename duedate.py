import pandas as pd
import sys, os
from datetime import date, datetime

if len(sys.argv) == 1:
    raw = [os.path.expanduser("~/hw.txt")] #default for convenient school use 
else:
    raw = sys.argv[1:]

def days_until(due):
    return (due - datetime.today()).days + 1

for f in raw:
    if os.path.isfile(f): #guard for file existence
        if os.stat(f).st_size != 0: #check if file is non-empty
            data = pd.read_csv(
                f,
                sep='|',
                skip_blank_lines=True,
                skipinitialspace=True,
                parse_dates=[1],
                names=['task', 'due date', 'required'])
            skip = False
        else:
            print(f"{f} is empty!")
            skip = True
    else:
        print(f"{f} isn't a file!")
        skip = True

    if not skip:
        for _, r in data.iterrows():
            task = r[0]
            required = r[2]
            due = datetime.strptime(r[1], "%A %m/%d ")
            due = due.replace(year=date.today().year)
            until = days_until(due)

            if until<=required and until>0:
                print(f"{until} day{'' if until==1 else 's'} until {task}({required} needed)")
            elif until == 0:
                print(f"{task} due today!")
            elif until < 0:
                print(f"{task} is {-until} day{'' if -until==1 else 's'} late!!")
