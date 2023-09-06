from datetime import datetime


def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def nearest_time(current_time, time_n, min_x):
    mas_out = []
    x = get_sec(time_n) - get_sec(current_time)
    if x < 0:
        x *= -1
    if x < min_x:
        min_x = x
        mas_out.append(time_n)
        mas_out.append(min_x)
        return mas_out


minx = 100000000
currentTime = datetime.now().strftime("%H:%M:%S")
minTime = ""
masOut = ""
while True:
    time = input()
    if time == "exit":
        break
    else:
        try:
            if nearest_time(currentTime, time, minx):
                masOut = nearest_time(currentTime, time, minx)
                minTime = masOut[0]
                minx = masOut[1]
        except:
            pass
print(masOut[0])



УДАЛИТЬ MINX!!!