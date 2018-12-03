# -*- coding: utf-8 -*-
"""
@author: Hidde
"""


from flask import Flask, jsonify, request, redirect, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/opdracht1/', methods=['GET', 'POST'])
def opdracht_1():
    # Check if valid answer
    if request.method == 'POST':
        if request.form['answer'] != '-9':
            error = 'Fout antwoord! Probeer opnieuw.'
        else:
            return redirect(url_for('opdracht_2'))
        return render_template('opdracht_1.html', error=error)

    return  render_template('opdracht_1.html')

@app.route('/opdracht2/')
def opdracht_2():
    return render_template('opdracht_2.html')

@app.route('/opdracht2a/', methods=['GET', 'POST'])
def opdracht_2a():
    # Check if valid answer
    if request.method == 'POST':
        if request.form['answer2'].lower() != 'madrid':
            error = 'Fout antwoord! Probeer opnieuw.'
        else:
            return redirect(url_for('gapminder'))
        return render_template('opdracht_2a.html', error=error)

    return render_template('opdracht_2a.html')

@app.route('/gapminder/')
def gapminder():
    return render_template('gapminder.html')

@app.route('/opdracht3/', methods=['GET', 'POST'])
def opdracht_3():
    # Check if valid answer
    if request.method == 'POST':
        if request.form['answer3'].lower() != 'japan':
            error = 'Fout antwoord! Probeer opnieuw.'
        else:
            return redirect(url_for('finish'))
        return render_template('opdracht_3.html', error=error)

    return render_template('opdracht_3.html')

@app.route('/finish/')
def finish():
    return render_template('finish_123hidde.html')

@app.route('/cadeau/')
def cadeau():
    return render_template('cadeau.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
