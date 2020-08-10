from datetime import date
today = date.today()
print("fecha actual =", today)
# print(type(today))
year = today.year
month = today.month
day = today.day
# print(year, month, day)

# tuplas inmutables
meses = (i for i in range(1,12))
dias = (i for i in range(1, 32))

# print(meses, dias)
# print(dir(meses))

['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

def aEntero(sString):
    nameFunction = "aEntero"
    # 0 (for false)
    # 1 (for true)
    # print(f"Hello, from {nameFunction}!, el parámetro es: %s"%(sString))
    iInt = 0
    try:

        iInt = int(sString)
        
    except Exception as e:

        print(f"Exception on function: {nameFunction, e}")
    
    return(iInt)

sBirthday = input("Insert your birthday: yyyy-mm-dd: ")
# print(type(sBirthday))
print(f"you was write: {sBirthday} ")

long = len(sBirthday)

if long == 10:
    listBirthday = sBirthday.split('-')
    llist = listBirthday.__len__()
    if llist == 3:
        # print(f"la lista contiene: {llist} elementos")
        sYearBirthday = listBirthday[0]
        sMonthBirthday = listBirthday[1]
        sDayBirthday = listBirthday[2]
        if sYearBirthday.isnumeric() and sMonthBirthday.isnumeric() and sDayBirthday.isnumeric():
            print(f"your are {year - int(sYearBirthday)} years old")
        else:
            iYearBirthday = aEntero(sYearBirthday)
            iMonthBirthday = aEntero(sMonthBirthday)
            iDayBirthday = aEntero(sDayBirthday)

            if iYearBirthday != 0:
                print(f"your are {year - iYearBirthday} years old")
            
            if iMonthBirthday in meses:
                print("ok el mes")

            if iDayBirthday in dias:
                    print("ok el día")
            else:
                print(f"Intentelo de nuevo, {sBirthday} no cumple con el formato solicitado: yyyy-mm-dd ")
             


        # print(long, listBirthday, sYearBirthday, sMontBirthday, sDayBirthday)
    else:
        print(f"Intentelo de nuevo, {sBirthday} no cumple con el formato solicitado: yyyy-mm-dd ")
else:
    print(f"Intentelo de nuevo, {sBirthday} no cumple con el formato solicitado: yyyy-mm-dd ")






# print(dir(listBirthday) - métodos de una lista





# print("birthday :", sBirthday)
# print(type(sBirthday))
# new_age = int(age) + 5 #cast
# print(new_age)

# ---------------------------------------- #



