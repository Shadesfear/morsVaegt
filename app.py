from flask import Flask, render_template
import datetime
app = Flask(__name__)


def isInbed(weight, threshold):
	
	try:
		weight = int(weight)
	except Exception as e:
		weight = 0

	if weight > threshold:
		return True
	else:
		return False

file = open("values.txt","r")

threshold = 10
weight = file.read()
print(weight)

@app.route('/')
def index():
	inBed = isInbed(weight, threshold)
	if inBed:
		templateData = {
		'title' : 'You are in bed',	} 

	elif not inBed:
		templateData = {
		'title' : 'You are not in bed',}
	return render_template('index.html', **templateData)

   
@app.route('/cakes')
def cakes():
    return 'yummy ckaes!'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
