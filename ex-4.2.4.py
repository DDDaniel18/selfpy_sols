import calendar

input_date = input("Enter a date: ") #dd/mm/yyyy

year = int(input_date[6:])
month = int(input_date[3:5])
day = int(input_date[:2])

day = calendar.weekday(year, month, day)

day_word =''
if(day == 1):
    day_word = 'Sunday'
elif(day == 2):
    day_word = 'Monday'
elif(day == 3):
    day_word = 'Tuesday'
elif(day == 4):
    day_word = 'Wednesday'
elif(day == 5):
    day_word = 'Thursday'
elif(day == 6):
    day_word = 'Friday'
elif(day == 7):
    day_word = 'Saturday'  
    
print(day_word)
