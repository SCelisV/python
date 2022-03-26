"""
@author: Fabrizio Romano
transcript: SCelis

# func.attributes.py

# /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/learn.pp/learnpp/

"""

def multiplication(a, b=1):
    """Return a multiplied by b. """
    return a * b

special_attributes = [
    "__doc__", "__name__", "__qualname__", "__module__",
    "__defaults__", "__code__", "__globals__", "__dict__",
    "__closure__", "__annotations__", "__kwdefaults__",
]

for attribute in special_attributes:
    """ la función incorporada getattr obtiene el valor de los atributos """
    """ getattr(obj, attribute) is equivalent to (obj.attribute) """
    print(attribute, '  ->  ', getattr(multiplication, attribute))

"""

__doc__   ->   Return a multiplied by b. 
__name__   ->   multiplication
__qualname__   ->   multiplication
__module__   ->   __main__
__defaults__   ->   (1,)
__code__   ->   <code object multiplication at 0x7f28ce657450, file "func.attributes.py", line 10>
__globals__   ->   {'__name__': '__main__', '__doc__': '\n@author: Fabrizio Romano\ntranscript: SCelis\n\n# func.attributes.py\n\n# /home/hadoop/SCProjects/learn.pp/learnpp\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f28ce6f7b50>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'func.attributes.py', '__cached__': None, 'multiplication': <function multiplication at 0x7f28ce5a3ee0>, 'special_attributes': ['__doc__', '__name__', '__qualname__', '__module__', '__defaults__', '__code__', '__globals__', '__dict__', '__closure__', '__annotations__', '__kwdefaults__'], 'attribute': '__globals__'}
__dict__   ->   {}
__closure__   ->   None
__annotations__   ->   {}
__kwdefaults__   ->   None

"""