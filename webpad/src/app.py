from flask import Flask, render_template, request, redirect, url_for
from src.common.database import Database
from src.models.note import Note


app = Flask(__name__)
app.secret_key = '123'


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def index():
    notes = Note.all()
    return render_template('index.html', notes=notes)


@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form['title']
    description = request.form['content']

    note = Note(title=title, description=description)
    note.save_to_mongo()

    return redirect(url_for('index'))


@app.route('/delete')
def remove_all():
    Database.purge()
    return redirect(url_for('index'))


@app.route('/add')
def add():
    return render_template('add.html')


app.run(debug=False)
