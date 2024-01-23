from flask import Flask,render_template,request
import pickle
import numpy as np

#Loading the pickle file


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

# Take input value and passing to the predictor
@app.route('/prediction', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        SL = request.form['SL']
        
        SW = request.form['SW']
        
        PL = request.form['PL']
        
        PW = request.form['PW']
        
        arr = np.array([[SL, SW, PL, PW]])

        model = pickle.load(open('ir_model.pkl', 'rb'))
        Classification = model.predict(arr)
        print (Classification)
    return render_template('prediction.html',Classification = Classification)


if __name__ == '__main__':
    app.run()