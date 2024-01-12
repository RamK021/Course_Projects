import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
aqi_model = pickle.load(open('aqi_model.pkl', 'rb'))
dic = pickle.load(open('dic.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    city = int(request.form.get('City'))
    pm25 = float(request.form.get('PM2.5'))
    pm10 = float(request.form.get('PM10'))
    no   = float(request.form.get('NO'))
    no2  = float(request.form.get('NO2'))
    nox  = float(request.form.get('NOx'))
    nh3  = float(request.form.get('NH3'))
    co   = float(request.form.get('CO'))
    so2  = float(request.form.get('SO2'))
    o3   = float(request.form.get('O3'))
    benz = float(request.form.get('Benzene'))
    tol  = float(request.form.get('Toluene'))
    xyl  = float(request.form.get('Xylene'))
    prediction = aqi_model.predict([[city, pm25, pm10, no, no2, nox, nh3, co, so2, o3, benz, tol, xyl]])
    city_name = dic[city]
    output = round(prediction[0][0],4)
    return render_template('index.html', pred_aqi=output, cityname=city_name)
    


if __name__ == '__main__':
    app.run(debug=True)