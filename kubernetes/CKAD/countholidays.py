# DD-MM-YYYY
from datetime import date,timedelta

day,month,year = input().split("-")
listOfHolidays = input().split(",")
listOfHolidays = [int(i.split("-")[0])  for i in listOfHolidays]
start_date = date(int(year),int(month),1)
single_day = timedelta(days=1)
holiday = 0
# weekday = start_date.weekday()
# total_sat = [1 for i in calendar.monthcalendar(year,month) if i[5] != 0]
# total_sun = [1 for i in calendar.monthcalendar(year,month) if i[6] != 0]
# strftime("%A") to give day name from date object
#datetime.datetime.strptime(date, '%Y-%m-%d') to get the datetime.datetime object
# datetime.datetime.strptime(date, '%Y-%m-%d').date() to get the datetime.date object
while start_date.month == int(month):
    if start_date.weekday() == 5 or start_date.weekday() == 6 or start_date.day in listOfHolidays:
        holiday += 1
    start_date += single_day
print(holiday,listOfHolidays,[day,month,year])