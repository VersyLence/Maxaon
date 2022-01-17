with open('mat_dv.txt') as f:
    m=[]
    m1=[]
    m2=[]
    max=0
    max1=0
    for i in f:
        L=i.split()
        if int(L[4])>max:
            max=int(L[4])
            m=[]
            test=L[0]+' ',L[1]+ ' ',L[4]
            m.append(test)
        elif (int(L[4])==max):
            max=int(L[4])
            test=L[0]+' ',L[1]+ ' ',L[4]
            m1.append(test)

        if int(L[3])>max1:
            max1=int(L[3])
            m1=[]
            test=L[0]+' ',L[1]+ ' ',L[3]
            m1.append(test)
        elif (int(L[3])==max1):
            max1=int(L[3])
            test=L[0]+' ',L[1]+ ' ',L[3]
            m1.append(test)

print('Геометрия ',m)
print('Алгебра ',m1)