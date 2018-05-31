from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'abcdefghijklmnopqrstuvwxyz'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
  session['name'] = request.form['name']
  session['location'] = request.form['location']
  session['lang'] = request.form['lang']
  session['comment'] = request.form['comment']

  validation_error = False

  if len(session['name']) < 2:
    flash('Your name needs to be at least 2 characters')
    validation_error = True
  elif len(session['name']) > 30:
    flash('Your name needs to be shorter than 30 characters')
    validation_error = True    

  if len(session['comment']) > 120:
    flash('Your comment needs to be shorter')
    validation_error = True

  if validation_error == True:
    return redirect('/')
  else:
    return render_template('result.html')

app.run(debug=True)