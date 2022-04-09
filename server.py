from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '?'

@app.route('/2')
def sessionCounter():
    session['count'] += 1
    return redirect('/')

@app.route('/')
def counter():
    if 'count' not in session: 
        session['count'] = 0
    session['count'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)