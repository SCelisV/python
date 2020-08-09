# define lista
lst=[1,2,3,4,5,6,7,8,9,10] 
print (lst)

# calcula pares  
lst2=[]
for e in lst:
	if e%2==0: 
		lst2.append(e)
print (lst2)


# calcula impares
lst=[1,2,3,4,5,6,7,8,9,10] 
print (lst)
lst2=[]
for e in lst: 
	if e%2==1: 
		lst2.append(e)
print (lst2)

# cambia valores: pares -> 0, impares -> 1​
lst=[1,2,3,4,5,6,7,8,9,10] 

lst3=[]
for e in lst:
	if e%2==0: 
		lst3.append(0)
	else: 
		lst3.append(1)
print (lst3)

#sumar los datos de la lista
lst=[1,2,3,4,5,6,7,8,9,10] 
suma=0
for e in lst:
	suma+=e
print (suma)