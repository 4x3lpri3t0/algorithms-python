import calendar

m, d, y = map(int, input().split())

weekday_idx = calendar.weekday(y, m, d)
weekday = calendar.day_name[weekday_idx]

print(weekday.upper())