seconds = input("Enter time on seconds: ")
seconds = int(seconds)
minutes = seconds / 60
hours = minutes / 60
round_hours = round(hours, 2)

print("Seconds: ", seconds)
print("Minutes: ", minutes)
print("Hours: ", round_hours)

