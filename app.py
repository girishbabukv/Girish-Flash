from flask import Flask,render_template,request
import pickle


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/classification', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        SL = request.form['SL']
        print SL

        SW = request.form['SW']
        print SW

        PL = request.form['PL']
        print PL

        PW = request.form['PW']
        print PW
        
        model = pickle.load(open('ir_model.pkl', 'rb'))
        Classification  =  model.predict([[str(Classification)]])
        print(Classification)
    return render_template('prediction.html', Classification = Classification)


if __name__ == '__main__':
    app.run()