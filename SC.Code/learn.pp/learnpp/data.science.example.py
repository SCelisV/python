"""
@author: Fabrizio Romano
transcript: SCelis

# /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/learn.pp/learnpp/data.science.example.py

# data.science.example.py

"""
"""
Dividir una tarea compleja
Las funciones tambi�n son muy �tiles para dividir tareas largas o complejas en otras m�s peque�as. 
El resultado final es que el c�digo se beneficia de varias maneras, por ejemplo, la legibilidad, la comprobabilidad y reutilizaci�n. 
Para poner un ejemplo sencillo, imagina que est�s preparando un informe. 
Su c�digo necesita obtener datos de una fuente de datos, analizarlos, filtrarlos, pulirlos y, a continuaci�n, ejecutar toda una serie de algoritmos para producir los resultados que alimentar�n la clase de informe. 
No es raro leer procedimientos como �ste que son s�lo un gran funci�n do_report(data_source). 
Hay decenas o cientos de l�neas de c�digo que terminan con return report .

Estas situaciones son algo m�s comunes en el c�digo cient�fico, 
que suele ser brillante desde el punto de vista algor�tmico, 
pero a veces carecen del toque de los programadores experimentados cuando se trata del estilo en el que est�n escritos. 
Ahora, imag�nese unos cuantos cientos de l�neas de c�digo. 
Es muy dif�cil seguirlo, encontrar los lugares donde las cosas est�n cambian de contexto (como terminar una tarea y empezar la siguiente). 
�Tienes la imagen en tu mente? Bien. No lo hagas. En su lugar, mira este c�digo:

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

El ejemplo anterior es ficticio, por supuesto, pero �es muy f�cil que ser�a recorrer
a trav�s del c�digo? 
Si el resultado final se ve mal, ser�a muy f�cil depurar cada una de las
salidas de datos individuales en la funci�n do_report. 
Adem�s, es incluso m�s f�cil excluir parte de el proceso temporalmente de todo el procedimiento (s�lo tiene que comentar las partes que necesita suspender). 
Un c�digo as� es m�s f�cil de manejar.
Ocultar los detalles de la implementaci�n
Sigamos con el ejemplo anterior para hablar tambi�n de este punto. 
Puedes ver que, al el c�digo de la funci�n do_report, 
se puede entender bastante bien comprensi�n sin leer una sola l�nea de implementaci�n. 
Esto se debe a que las funciones ocultan los detalles de la implementaci�n. 
Esta caracter�stica significa que, si no necesitas profundizar en los detalles, 
no se ve forzado a hacerlo, de la forma en que lo har�a si do_report fuera s�lo una funci�n grande y gorda.  funci�n. Para entender lo que est� pasando, tendr�a que leer cada l�nea de c�digo.
l�nea de c�digo. Con las funciones, no es necesario. Esto reduce el tiempo que pasas leyendo el
c�digo y como, en un entorno profesional, leer el c�digo lleva mucho m�s tiempo que
que escribirlo, es muy importante reducirlo tanto como podamos.

"""