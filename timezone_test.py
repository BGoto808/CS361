#####################################################
# Timezone_test.py: Converts time from one timezone
#     to another (supports 16 time zones)
#
# Author: Bryson Goto, 2/21/2022
#####################################################

import pytz
import datetime

def get_timezone(num):
    if num == 1: # WAT
        source_ianatimezone = 'Africa/Bangui'
    if num == 2: # AT
        source_ianatimezone = 'America/Puerto_Rico'
    if num == 3: # ET
        source_ianatimezone = 'America/Detroit'
    if num == 4: # CT
        source_ianatimezone = 'America/Costa_Rica'
    if num == 5: # MT
        source_ianatimezone = 'America/Boise'
    if num == 6: # PT
        source_ianatimezone = 'America/Los_Angeles'
    if num == 7: # AKST
        source_ianatimezone = 'America/Juneau'
    if num == 8: # HST
        source_ianatimezone = 'Pacific/Honolulu'
    if num == 9: # SST
        source_ianatimezone = 'Pacific/Pago_Pago'
    if num == 10: # GMT
        source_ianatimezone = 'Europe/London'
    if num == 11: # CET
        source_ianatimezone = 'Europe/Berlin'
    if num == 12: # EET
        source_ianatimezone = 'Europe/Riga'
    if num == 13: # MSK 
        source_ianatimezone = 'Europe/Minsk'
    if num == 14: # AWST
        source_ianatimezone = 'Australia/Perth'
    if num == 15: # ACST
        source_ianatimezone = 'Australia/Darwin'
    if num == 16: # AEST
        source_ianatimezone = 'Australia/Brisbane'

    return source_ianatimezone

given_date = datetime.datetime.now()

# This is the timezone where the date/time was recorded
# Change parameter depending on time zone:
source_ianatimezone = get_timezone(1)
tz_from = pytz.timezone(source_ianatimezone)

# This is the timezone to which I want to convert the above date/time
# Change parameter depending on time zone: 
target_ianatimezone = get_timezone(6)
to_tz = pytz.timezone(target_ianatimezone)

print("Converting given date: ", given_date, " from: ",source_ianatimezone, " to: ", target_ianatimezone)

# Localizing the given_date with the source timezone
localize_with_from_tz = tz_from.localize(given_date, is_dst=True)

# Localizing and converting the given_date to the target timezone
convert_with_to_tz = tz_from.localize(given_date, is_dst=True).astimezone(to_tz)

print("Localized value: ", localize_with_from_tz)
print("After converting: ", convert_with_to_tz)