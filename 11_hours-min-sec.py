"""Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The
argument for this parameter will be the number of seconds to be translated into the number of hours,
minutes, and seconds. If the amount for the hours, minutes, or seconds is zero, don’t show it: the
function should return '10m' rather than '0h 10m 0s'. The only exception is that
getHoursMinutesSeconds(0) should return '0s'."""


def getHoursMinutesSeconds(totalseonds):

    # If the toatal seconds is 0 return os
    if totalseonds == 0:
        return '0s'

    # set hours to 0 and then add 1 hr for every 3600 seconds removed in
    # the totalsecons

    days = 0
    while totalseonds >= 86400:
        days += 1
        totalseonds -= 86400

    hours = 0
    while totalseonds >= 3600:
        hours += 1
        totalseonds -= 3600

    # set minutes to 0, and then add a minute for every 60 seconds removed from
    # the totalseconds until the totalseconds is less than 60

    minutes = 0
    while totalseonds >= 60:
        minutes += 1
        totalseonds -= 60

    # set seconds to the remaining totalSecond
    seconds = totalseonds

    # create a string that holds the hrs:min:sec

    hms = []

    # if there is one hr or more, add the amount with an H suffix

    if days > 0:
        hms.append(str(days) + 'D')
    if hours > 0:
        hms.append(str(hours) + 'H')
    if minutes > 0:
        hms.append(str(minutes) + 'M')
    if seconds > 0:
        hms.append(str(seconds) + 'S')

    return '-'.join(hms)


result = getHoursMinutesSeconds(600000)
print(result)
