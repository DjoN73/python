MINUTE = 60
HOUR = 60 ** 2
DAY = HOUR * 24

time = [53, 153, 4153, 400153, 90061]

for duration in time:
    if duration // MINUTE <= 1:
        print(duration, 'сек')
    elif MINUTE < duration < HOUR:
        minute = duration // MINUTE
        second = duration - (minute * MINUTE)
        print(minute, 'мин', second, 'сек')
    elif HOUR < duration < DAY:
        hour = duration // HOUR
        duration = duration % HOUR
        minute = duration // MINUTE
        second = duration - (minute * MINUTE)
        print(hour, 'час', minute, 'мин', second, 'сек')
    else:
        day = duration // DAY
        duration = duration % DAY
        hour = duration // HOUR
        duration = duration % HOUR
        minute = duration // MINUTE
        second = duration - (minute * MINUTE)
        print(day, 'день', hour, 'час', minute, 'мин', second, 'сек')
