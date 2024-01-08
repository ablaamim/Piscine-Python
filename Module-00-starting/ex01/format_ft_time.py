import time  # Import the time module
# Get the current time in seconds since January 1, 1970
current_time_seconds = time.time()

# print('-->',current_time_seconds)

# Format the current time as a stringg
formatted_time = time.strftime("%b %d %Y", time.gmtime(current_time_seconds))

# print('-->',formatted_time)

# Format the current time in regular notation
regular_notation = "{:,.4f}".format(current_time_seconds)

# print('-->', regular_notation)

# Format the current time in scientific notation
scientific_notation = "{:.2e}".format(current_time_seconds)
# print('-->',scientific_notation)

# Print the formatted output
print(f"Seconds since January 1, 1970: {regular_notation} \
or {scientific_notation} in scientific notation$")
print(formatted_time)

# current_time_seconds = 1666355857.362291
# regular_notation = "{:,.4f}".format(current_time_seconds)
# print('EXAMPLE',regular_notation)
