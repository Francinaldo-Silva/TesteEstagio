def ordenar(a):
    v = len(a)-1
    ordem = False
    while not ordem:
        ordem = True
        for i in range(v):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                ordem = False
                print(a)
    return a
a = [5,3,2,4,7,1,0,6]
ordenar(a)
