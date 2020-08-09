# define lista
lst=[i for i in range(1, 11)]
print (lst)

# calcula pares
lst=[i for i in range(1, 11)]
print (lst)
lst2=[e for e in lst if e%2==0] 
print (lst2)

# calcula impares
lst=[i for i in range(1, 11)]
print (lst)
lst2=[e for e in lst if e%2==1]
print (lst2)

# cambia valores: pares -> 0, impares -> 1​
lst=[i for i in range(1, 11)]
print (lst)
lst3=[0 if e%2==0 else 1 for e in lst] 
print (lst3)

# suma los datos de una lista
lst=[i for i in range(0,11)]
suma=sum(lst)
print (suma)