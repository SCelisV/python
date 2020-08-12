# importar el frameWork, renderiza htmls, 
from flask import  Flask, render_template

# inicializar el frameWork 
# __name__ => con esta variable le indicamos que este es el fichero que arranca la app
# app => crear las rutas del servidor (URL's)
app = Flask(__name__) 
# ruta para la pág principal
@app.route('/')
def home():
    # return "Home Page" # return texto
    return render_template('home.html') # return html

@app.route('/experience')
def experience():
    return render_template('experience.html') # return html

@app.route('/academic')
def academic():
    return render_template('academic.html')

@app.route('/portafolio')
def portafolio():
    return "Portafolio Page"

@app.route('/contact')
def contact():
    return "Contact Page"
    
@app.route('/notes')
def notes():
    return "Manuals and Notes Page"

@app.route('/links')
def links():
    return "Links of Interes Page"

@app.route('/curriculum')
def curriculum():
    return "Curriculum CV"

@app.route('/photos')
def photos():
    return "Photos Page"

@app.route('/EllioT')
def elliot():
    return "EllioT Page"

# comprobar si este es el fichero ppal que ejecuta la aplicación ó un modulo
if  __name__ == '__main__':
    # Ejecuta la aplicación
    # -O-J-O- Don't use in production ONLY on a local development server
    # ref:deployment for WSGI server
    # app.run()
    app.run(debug=True)


