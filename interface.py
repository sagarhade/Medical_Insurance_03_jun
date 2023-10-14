from flask import Flask,jsonify,request,render_template
import config

from project_app.utils import MedicalInsurance

app = Flask(__name__)

##########################################################################################
#########################    HOME API     ###############################################
##########################################################################################
@app.route('/') # HOme API
def my_fun():
    print("Hello Flask")
    return render_template('home.html')


@app.route("/predict_charges")

def get_insurance_charges():
    data = request.form
    print("Data Is :",data)

    age = eval(data['age'])  
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    print("age,sex,bmi,children,smoker,region >>",age,sex,bmi,children,smoker,region)

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges  = med_ins.get_predict_chagres()
    return jsonify({"Result" : f"Predicted Medical insurance Charges are {charges}"})



app.run(port = config.PORT_NUMBER,debug = True ) # Server Start