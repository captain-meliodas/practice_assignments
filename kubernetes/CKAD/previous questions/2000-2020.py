from datetime import datetime
inpdate = input()
day = datetime.strptime(inpdate, '%d-%m-%Y')
print(day.strftime('%A'),day.weekday())