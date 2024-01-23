from flask import Flask,render_template,request
import pickle
import numpy as np

#Loading the pickle file
model = pickle.load(open('ir_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

# Take input values and passing to the predictor
@app.route('/predict', methods = ['POST'])
def index():
        SL = request.form['SL']
        SW = request.form['SW']
        PL = request.form['PL']
        PW = request.form['PW']
        arr = ([[SL, SW, PL, PW]])
        pred = model.predict(arr)
        return render_template('result.html', pred=pred)

if __name__ == "__main__":
    app.run(debug=True)