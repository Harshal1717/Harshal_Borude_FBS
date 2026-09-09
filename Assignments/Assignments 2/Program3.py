#Convert distance given in feet and inches into m and cm 
f = int(input('Enter distance in Feet:'))
i = int(input('Enter distance in an Inches:'))

ti = (f*12)+i
cm = ti*2.54
m = cm/100

print(f'The distance in {f}f.{i}inch is {m}meter and {cm}cm')