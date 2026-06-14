# Given data
total_degrees = 360
total_hours = 24

# Time taken for 1 degree in hours
hours_per_degree = total_hours / total_degrees

# Convert to minutes
minutes_per_degree = hours_per_degree * 60

# Time for 2 degrees
time_for_2_degrees = minutes_per_degree * 5

print(f"{hours_per_degree=}")
print(f"{minutes_per_degree=}")
print(f"{time_for_2_degrees=}")