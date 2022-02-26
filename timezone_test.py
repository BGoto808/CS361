#####################################################
# Timezone_test.py: Converts time from one timezone
#     to another (supports 16 time zones)
#
# Author: Bryson Goto, 2/21/2022
#####################################################

import pytz
import datetime
import getopt
import sys

def get_timezone(num):
    if num == 1: # WAT
        timezone = 'Africa/Bangui'
    if num == 2: # AT
        timezone = 'America/Puerto_Rico'
    if num == 3: # ET
        timezone = 'America/Detroit'
    if num == 4: # CT
        timezone = 'America/Costa_Rica'
    if num == 5: # MT
        timezone = 'America/Boise'
    if num == 6: # PT
        timezone = 'America/Los_Angeles'
    if num == 7: # AKST
        timezone = 'America/Juneau'
    if num == 8: # HST
        timezone = 'Pacific/Honolulu'
    if num == 9: # SST
        timezone = 'Pacific/Pago_Pago'
    if num == 10: # GMT
        timezone = 'Europe/London'
    if num == 11: # CET
        timezone = 'Europe/Berlin'
    if num == 12: # EET
        timezone = 'Europe/Riga'
    if num == 13: # MSK 
        timezone = 'Europe/Minsk'
    if num == 14: # AWST
        timezone = 'Australia/Perth'
    if num == 15: # ACST
        timezone = 'Australia/Darwin'
    if num == 16: # AEST
        timezone = 'Australia/Brisbane'

    return timezone  

# Command line arguments: python <file_name> <original_timezone> <timezone_to_convert_to>
given_date = datetime.datetime.now()

#given_date = sys.argv[0]
original_tz = (sys.argv[1])
converted_tz = (sys.argv[2])

# This is the timezone where the date/time was recorded
source_ianatimezone = get_timezone(int(original_tz))

tz_from = pytz.timezone(source_ianatimezone)

# This is the timezone to which I want to convert the above date/time
target_ianatimezone = get_timezone(int(converted_tz))

to_tz = pytz.timezone(target_ianatimezone)

print("Converting given date: ", given_date, " from: ",source_ianatimezone, " to: ", target_ianatimezone)

# Localizing the given_date with the source timezone
localize_with_from_tz = tz_from.localize(given_date, is_dst=True)

# Localizing and converting the given_date to the target timezone
convert_with_to_tz = tz_from.localize(given_date, is_dst=True).astimezone(to_tz)

print("Localized value: ", localize_with_from_tz)
print("After converting: ", convert_with_to_tz)

# Writing the converted time to .txt file
file = open("converted_time.txt", "w")
file.write(convert_with_to_tz.strftime("%m/%d/%y %I:%M:%S %p"))
file.close()