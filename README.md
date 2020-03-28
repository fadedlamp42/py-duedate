# py-duedate
Python tool for tracking tasks and due dates

# Usage
`python3 duedate.py`: assumes input file of ~/hw.txt for convenience of students

`python3 duedate.py file_1.txt file_2.txt file_n.txt`: allow passing arbitrary number of files for parsing

# Input file format
py-duedate leverages `pandas.read_csv` to parse data. Briefly, delimeter is `|` (ASCII 124) and leading spaces are ignored.

Columns are expected in order: `task name | Weekday Month/day | RequiredDays`

Year is currently assumed to be current year.

# Example (ran on Saturday 03/28)
Input: `python3 duedate.py example.txt`

Output:
```
1 day until Chinese homework (4 needed)
3 days until Calculus homework (4 needed)
3 days until Biology test 10:30am (4 needed)
```
