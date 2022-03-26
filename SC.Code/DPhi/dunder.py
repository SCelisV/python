"""
Dunder methods or Magic methods __method__ - double underscores.

Magic methods are functions that belong to a class. 
pueden ser: instances and class methods. 

esto es correcto.. PERO NO LO HAGAS!!
The probably most important thing is that magic methods are not meant to be called directly by you! YourClass().__actual_name__()

Se invocan a partir de ciertas acciones que aplicas a tu clase o instancia de tu clase.
ex: llamar a str(TuClase()) invocaría el método mágico __str__ o 
ex: TuClase() + TuClase() invocaría __add__ si esta implementado.

permiten escribir clases que se pueden utilizar junto con los métodos incorporados de python.
código más legible y menos verboso.

Example: Custom Datetime Range is something similar to the built-in range function
Este ejemplo tiene algo más de funcionalidad que range y creará rangos datetime en lugar de rangos numéricos (se puede hacer también con pandas..)
"""

from datetime import datetime, timedelta
from typing import Iterable
from math import ceil


class DateTimeRange:
    """
    este método inicializa los atributos de instancia de clase. 
    inicio y final y tamaño del step, similar a range function.
    """
    def __init__(self, start: datetime, end_:datetime, step:timedelta = timedelta(seconds=1)):
        self._start = start
        self._end = end_
        self._step = step

    """
    genera todos los elementos que forman parte del rango datetime.
    función generadora ( yield ), que crea un elemento a la vez, lo cede a quien lo llama y permite que éste lo procese hasta que llega al final del rango
    Esta declaración pone en pausa la función guardando todos sus estados y luego continúa a partir de ahí en sucesivas llamadas. 
    permite consumir un elemento a la vez y trabajar con él sin necesidad de tener todos los elementos en memoria.
    Es práctico cuando cada elemento ocupa mucha memoria o cuando se tiene un gran número de elementos. 
    """
    def __iter__(self) -> Iterable[datetime]:
        point = self._start
        while point < self._end:
            yield point
            point += self._step

    """
    devuelve el número de elementos que forman parte de un rango
    para saber cuántos elementos ya has procesado de todos los disponibles. 
    len(my_range)
    """
    def __len__(self) -> int:
        return ceil((self._end - self._start) / self._step)

    """
    para comprobar si un elemento forma parte de su rango no se  compara el elemento dado con todos los elementos del rango
    """
    def __contains__(self, item: datetime) -> bool:
        mod = divmod(item - self._start, self._step)
        return item >= self._start and item < self._end and mod[1] == timedelta(0)

    """
    para recuperar entradas de los objetos.
    obtener el último elemento: my_range[-1]
    """
    def __getitem__(self, item: int) -> datetime:
        n_steps = item if item >= 0 else len(self) + item
        return_value = self._start + n_steps * self._step
        if return_value not in self:
            raise IndexError()

        return return_value
    """
    permiten convertir una instancia de su clase en una cadena: print(my_range)

    """
    def __str__(self):
        return f"Datetime Range [{self._start}, {self._end}) with step {self._step}"

# examples para probar

my_range = DateTimeRange(datetime(2021,1,1), datetime(2021,12,1), timedelta(days=12))
print(my_range)
assert len(my_range) == len(list(my_range))
my_range[-2] in my_range
my_range[2] + timedelta(seconds=12) in my_range
for r in my_range:
    do_something(r)


# ?? npi si funciona así
(2021,11,1) in my_range 
"""
muy grande, crea una lista con 3184617600 entradas datetime --> list(DateTimeRange(datetime(1900,1,1), datetime(2000,1,1)).
no es una lista o tupla
"""
list(DateTimeRange(datetime(2021,11,1), datetime(2021,11,26)))
