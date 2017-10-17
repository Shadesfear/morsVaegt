from flask import Flask, render_template
import datetime
app = Flask(__name__)
@app.route('/')
def index():
    now = datetime.datetime.now()
    file = open("test.txt","r")

    timeString = file.read()
    templateData = {
	'title' : 'HELLO!',
	'time' : timeString
	}
    return render_template('index.html', **templateData)
   
    


@app.route('/cakes')
def cakes():
    return 'yummy ckaes!'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
