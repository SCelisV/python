import MyLibrary

filename='files/loudacre.log'
lines = MyLibrary.loadfile(filename)
for line in lines:
    print("line: ", line)

myinput = MyLibrary.userinput('Dime Algo: \n')
print("myInput: ", myinput)
