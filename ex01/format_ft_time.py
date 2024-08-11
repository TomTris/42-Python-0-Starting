import time

timestamp = time.time()
local_time = time.localtime(timestamp)
# formattedday = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
formattedday = time.strftime("%b %d %Y", local_time)

# print(timestamp)
formatted_number = "{:,.4f}".format(timestamp)
to_power_number = "{:.2e}".format(timestamp)

print("Seconds since January 1, 1970:", formatted_number, "or ", to_power_number, " in scientific notation")
print(formattedday)