from MyLibrary import loadfile

filename='files/loudacre.log'
lines = loadfile(filename)
for line in lines:
    print("line: ", line)

from MyLibrary import userinput
myinput = userinput('Dime Algo: \n')
print("myInput: ", myinput)
