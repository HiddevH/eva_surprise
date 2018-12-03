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
        if request.form['answer'] != '5':
            error = 'Fout antwoord! Probeer opnieuw.'
        else:
            return redirect(url_for('opdracht_2'))
        return render_template('opdracht_1.html', error=error)
            
    return  render_template('opdracht_1.html')

@app.route('/opdracht2/')
def opdracht_2():
    return render_template('opdracht_2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
