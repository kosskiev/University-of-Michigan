#Implement the calculator for the date of Easter.

#The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.


while True:
    year = int(input('Enter a year between 1900 to 2099 '))
    if 1900 <= year <= 2099:
        break

    else:
        print('This wrong')
        continue

a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dateofeaster = 22 + d + e
if year == 1954 or year == 1981 or year == 2049 or year == 2076:
    y = dateofeaster - 7
    if dateofeaster > 31:
        z = dateofeaster - 31
        print(z, 'April')

    else:
        print(dateofeaster, 'March')

elif dateofeaster > 31:
    z = dateofeaster - 31
    print(z, 'April')

else:
    print(dateofeaster, 'March')
