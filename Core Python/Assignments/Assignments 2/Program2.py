#Convert the entered time in seconds

h = int(input('Enter the hours:'))

m = int(input('Enter the minutes:'))
s = int(input('Enter the seconds'))

tt = (h*3600)+(m*60)+s
print(f'For time {h}:{m}:{s} the Total Seconds are {tt}')