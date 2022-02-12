#####################################################
# Timezone_test.py: Converts time from one timezone
#     to another
#
# Author: Bryson Goto, 2/12/2022
#####################################################

import pytz
import datetime

given_date = datetime.datetime.now()

#this is the timezone where the date/time was recorded
source_ianatimezone = 'Asia/Kolkata'
tz_from = pytz.timezone(source_ianatimezone)

#this is the timezone to which I want to convert the above date/time
target_ianatimezone = 'America/Los_Angeles' 
to_tz = pytz.timezone(target_ianatimezone)

print("Converting given date: ",given_date," from: ",source_ianatimezone," to: ",target_ianatimezone)

#Localizing the given_date with the source timezone
localize_with_from_tz = tz_from.localize(given_date, is_dst=True)

#Localizing and converting the given_date to the target timezone
convert_with_to_tz = tz_from.localize(given_date, is_dst=True).astimezone(to_tz)

print("Localized value: ",localize_with_from_tz)
print("After converting: ",convert_with_to_tz)