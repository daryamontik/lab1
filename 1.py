sec = int(input("Введите количество секунд: "))

days: int = sec//86400
hour: int = (sec-days*86400)//3600
min: int = (sec-days*86400-hour*3600)//60
s: int = sec - hour*360-min*60-days*86400

time_formatted = f"{days}:{hour:02}:{min:02}:{s:02}"
print(time_formatted)