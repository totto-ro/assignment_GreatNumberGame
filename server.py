from flask import Flask, app, render_template, redirect, session, request

import random

app = Flask( __name__ )
app.secret_key = "verySecret"

@app.route( '/', methods=['GET'] )
def displayPage():
    if "num" not in session:
        session['num'] = random.randint(1, 100)
    return render_template("index.html")

@app.route( '/results', methods=['POST'] )
def guessNum():
    numInput= request.form['numbers']
    session['numResults'] = int(numInput)
    return redirect('/')


if __name__ == "__main__":
    app.run ( debug = True )