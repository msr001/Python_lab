import datetime 
today=datetime.datetime.now().date()
print("Current date:",today)

day=int(input("Enter days to add :\n"))

print("Days after adding: ",today + datetime.timedelta(day))