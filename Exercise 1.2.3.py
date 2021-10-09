#10 km in 42 minutes and 42 seconds
# pace = time per mile / (minutes) and (seconds) and (hours)

distance = 10 / 1.61
minutes = 42
seconds = 42
time_seconds = minutes * 60 + 42
time_minutes = time_seconds / 60
time_hours = time_minutes / 60

pace_seconds = distance / time_seconds
pace_minutes = distance / time_minutes
pace_hours = distance / time_hours

print("Time in Seconds:",time_seconds)
print("Time in Minutes:",time_minutes)
print("Time in Hours:",time_hours)

print("Pace in Seconds:",pace_seconds)
print("Pace in Minutes:",pace_minutes)
print("Pace in Hours:",pace_hours)