def sucin(zoznam):
    sum=1 #nie 0 lebo pri empty zoz musi dat 1
    for i in zoznam:
        sum*=i #1*digits of zoz
    return sum

c = [2, 3, 5, 7, 11]
print(sucin(c))#2*3*5*7*11=2310
print(sucin(list(range(1,11))))#10 fakt=3628800
print(sucin([2]*20)) #2**20=1048576
print(sucin([])) #empty zoz=1
