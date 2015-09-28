from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms.fields import TextField, SelectMultipleField


class ItemForm(Form):
    name = TextField('Name')
    categories = SelectMultipleField('Categories')

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    form = ItemForm()
    form.categories.choices = [
        ('ski', 'Skiing'),
        ('skating', 'Skating'),
        ('snowboarding', 'Snowboarding')
        ]
    if request.method == 'POST':
        print form.name.data
        print form.categories.data
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'SECRET_KEY'
    app.run(host='0.0.0.0', port=5000)
