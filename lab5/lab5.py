SUCCESSFUL_OPERATION = "GET"
WATCHED_PRESENTATION = "presentations"
BEGIN_DATE = "17/May/2015:10"
END_DATE = "17/May/2015:21:00"

log_file = open("apache_logs.txt", "r")

line_counter = 0
is_in_timeline = False

for line in log_file:
    if END_DATE in line:
        is_in_timeline = False
        break
    if BEGIN_DATE in line:
        is_in_timeline = True
    if is_in_timeline and SUCCESSFUL_OPERATION in line and WATCHED_PRESENTATION in line:
        line_counter += 1
        
print(line_counter)
