from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'

class InscripcionForm(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[DataRequired(), Length(min=4, max=50)])
    email = EmailField('Correo Electrónico', validators=[DataRequired(), Email()])
    telefono = TelField('Teléfono', validators=[DataRequired(), Length(min=10, max=15)])
    intereses = SelectField('Intereses en IoT', validators=[DataRequired()], choices=[
        ('domotica', 'Domótica'),
        ('salud', 'Salud'),
        ('industrial', 'Industrial'),
        ('ciudades', 'Ciudades Inteligentes'),
        ('otros', 'Otros')
    ])
    mensaje = TextAreaField('Mensaje Adicional')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prosycont')
def prosycont():
    return render_template('prosycont.html')

@app.route('/empresas')
def empresas():
    return render_template('empresas.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = InscripcionForm()
    if form.validate_on_submit():
        # Guardar los datos del formulario en un archivo de texto
        with open('form_data.txt', 'a') as f:
            f.write(f"Nombre: {form.nombre.data}\n")
            f.write(f"Email: {form.email.data}\n")
            f.write(f"Teléfono: {form.telefono.data}\n")
            f.write(f"Intereses: {form.intereses.data}\n")
            f.write(f"Mensaje: {form.mensaje.data}\n\n")

        # Renderizar la página de éxito
        return render_template('success.html')

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
