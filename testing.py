from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import DateField, TextAreaField, StringField, SubmitField, EmailField, SelectField, validators
from wtforms.validators import DataRequired, Email
app = Flask(__name__)

#form class
app.config['SECRET_KEY'] = "dsf"

class NamerForm(FlaskForm):
    name = StringField("First name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    return render_template("index.html")


#invalid URL
@app.errorhandler(404)
def page_not_found (e):
    return render_template("404.html"), 404

# Internal Server error
@app.errorhandler(500)
def page_not_found (e):
    return render_template("500.html"), 500

@app.route("/name", methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    render_template("name.html", name = name , form = form)

if __name__ == "__main__":
    app.run()
