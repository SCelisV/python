"""
@author: Fabrizio Romano
transcript: SCelis

# /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/learn.pp/learnpp/data.science.example.py

# data.science.example.py

"""
"""
Dividir una tarea compleja
Las funciones también son muy útiles para dividir tareas largas o complejas en otras más pequeñas. 
El resultado final es que el código se beneficia de varias maneras, por ejemplo, la legibilidad, la comprobabilidad y reutilización. 
Para poner un ejemplo sencillo, imagina que estás preparando un informe. 
Su código necesita obtener datos de una fuente de datos, analizarlos, filtrarlos, pulirlos y, a continuación, ejecutar toda una serie de algoritmos para producir los resultados que alimentarán la clase de informe. 
No es raro leer procedimientos como éste que son sólo un gran función do_report(data_source). 
Hay decenas o cientos de líneas de código que terminan con return report .

Estas situaciones son algo más comunes en el código científico, 
que suele ser brillante desde el punto de vista algorítmico, 
pero a veces carecen del toque de los programadores experimentados cuando se trata del estilo en el que están escritos. 
Ahora, imagínese unos cuantos cientos de líneas de código. 
Es muy difícil seguirlo, encontrar los lugares donde las cosas están cambian de contexto (como terminar una tarea y empezar la siguiente). 
¿Tienes la imagen en tu mente? Bien. No lo hagas. En su lugar, mira este código:

"""

def do_report(data_source):
    # fetch and prepare data
    data = fetch_data(data_source)
    parsed_data = parse_data(data)
    filtered_data = filter_data(parsed_data)
    polished_data = polish_data(filtered_data)
    
    # run algorithms on data
    final_data = analyse(polished_data)

    # create and return report
    report = Report(final_data)
    return report


"""

El ejemplo anterior es ficticio, por supuesto, pero ¿es muy fácil que sería recorrer
a través del código? 
Si el resultado final se ve mal, sería muy fácil depurar cada una de las
salidas de datos individuales en la función do_report. 
Además, es incluso más fácil excluir parte de el proceso temporalmente de todo el procedimiento (sólo tiene que comentar las partes que necesita suspender). 
Un código así es más fácil de manejar.
Ocultar los detalles de la implementación
Sigamos con el ejemplo anterior para hablar también de este punto. 
Puedes ver que, al el código de la función do_report, 
se puede entender bastante bien comprensión sin leer una sola línea de implementación. 
Esto se debe a que las funciones ocultan los detalles de la implementación. 
Esta característica significa que, si no necesitas profundizar en los detalles, 
no se ve forzado a hacerlo, de la forma en que lo haría si do_report fuera sólo una función grande y gorda.  función. Para entender lo que está pasando, tendría que leer cada línea de código.
línea de código. Con las funciones, no es necesario. Esto reduce el tiempo que pasas leyendo el
código y como, en un entorno profesional, leer el código lleva mucho más tiempo que
que escribirlo, es muy importante reducirlo tanto como podamos.

"""