def divisores(n):
    lista=[]
    for i in range(1,n+1):
        if n%i==0:
            lista.append(i)
    return lista

n=20
print(divisores(n))