from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)

app.secret_key="22"

@app.route('/')
def index():
    import random
    session ['number'] = random.randrange(0,101)
    print "THIS IS THE NUMBER" , session ['number']
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hint():
    guess = int(request.form['guess'])
    if guess > session['number']:
        session ['hint']= "Too High"
    if guess < session ['number']:
        session ['hint']= "Too Low"
    if guess == session ['number']:
        session ['hint']= "winner, play again!"
        return redirect('/')


    return redirect('/result')


@app.route('/result')
def result():
    return render_template('index.html')





app.run(debug=True)