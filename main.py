def bisiesto(year):
    if year % 4 == 0:
        return True
    else:
        return False

print(bisiesto(2012))