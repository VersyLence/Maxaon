def Distance(Acceleration):
    def wrapper(V0,t,V):
        Acceleration(V0, V, t)
        S=V0*t+(a*t)/2
        print('Расстояние =', S)
    return wrapper

@Distance
def Acceleration(V0, V, t):
    global a
    a=(V-V0)/t
    print('Ускорение равно = ',a)



try:
    test=Acceleration(V0=int(input()), V=int(input()), t=int(input()))
except ZeroDivisionError:
        print('0 Вводить нельзя')
except ValueError:
        print('Неверный формат')
