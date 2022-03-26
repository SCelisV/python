"""
@author: Fabrizio Romano
transcript: SCelis

# docstrings.py


# /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/learn.pp/learnpp/docstrings.py

"""

""" one-line docstrings """
def square(n):
    """Return the square of a number n. """
    return n ** 2


def get_username(userid):
    """Return the username of a user given their id. """
    return db.get(user_id=userid).username

"""
multiline docstrings.
Los comentarios multilínea se estructuran de forma similar. 
Debe haber una línea que brevemente explique lo esencial del objeto, 
y luego una descripción más detallada. 
- notación Sphinx
"""

def connect(host, port, user, password):
    """Connect to a database.
    Connect to a PostgreSQL database directly, using the given parameters.
    :param host: The host IP.
    :param port: The desired port.
    :param user: The connection username.
    :param password: The connection password.
    :return: The connection object.
    """
    # construir el cuerpo de la función  
    return connection



