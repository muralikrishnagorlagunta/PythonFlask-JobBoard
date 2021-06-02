import sqlite3
from flask import Flask, render_template, g

app=Flask(__name__)

PATH='db/jobs.sqlite'


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
