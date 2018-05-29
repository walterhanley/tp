import time

time = time.time()

days_since = int(time // 86400)

print('It has been {} days since the epoch.'.format(days_since))

hours = (time % 86400) // 3600
minutes = ((time % 86400) // 60) - hours * 60
seconds = (time % 86400) - minutes * 60 - hours * 3600

print("Today there have been {} hours, {} minutes, and {} seconds.".format(hours, minutes, seconds))
