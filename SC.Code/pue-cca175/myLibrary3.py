import sys
sys.path.append('/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/library')

from MyLibrary2 import loadfile

filename='files/loudacre.log'
lines = loadfile(filename)
for line in lines:
    print("line: ", line)

from MyLibrary2 import userinput
myinput = userinput('Dime Algo: \n')
print("myInput: ", myinput)
