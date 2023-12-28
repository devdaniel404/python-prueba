from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos.db'
db = SQLAlchemy(app)

class Datos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    telefono = db.Column(db.Integer)
    fecha_nacimiento = db.Column(db.Date)

@app.route('/')
def index():
    datos = Datos.query.all()
    return render_template('index.html', datos=datos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        telefono = request.form['telefono']
        fecha_nacimiento = request.form['fecha_nacimiento']
        dato = Datos(nombre=nombre, apellido=apellido, edad=edad, telefono=telefono, fecha_nacimiento=fecha_nacimiento)
        db.session.add(dato)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('agregar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    dato = Datos.query.get(id)
    if request.method == 'POST':
        dato.nombre = request.form['nombre']
        dato.apellido = request.form['apellido']
        dato.edad = request.form['edad']
        dato.telefono = request.form['telefono']
        dato.fecha_nacimiento = request.form['fecha_nacimiento']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar.html', dato=dato)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    dato = Datos.query.get(id)
    db.session.delete(dato)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
