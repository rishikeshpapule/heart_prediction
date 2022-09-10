
import re
from flask import Flask , request,render_template,url_for,jsonify
import config
from project_app.utils import Medicalinsurance

app = Flask(__name__)

@app.route("/")
def welcome_python():
    return "Hello Python"
@app.route("/predict",methods=["POST","GET"])
#@app.route("/predict",methods=["POST"])
def results():
    if request.method  == "POST":
        data = request.form
        print("DATA is",data)

        age=eval(data["age"])
        sex=eval(data["sex"])
        cp=eval(data["cp"])
        trestbps=eval(data["trestbps"])
        chol=eval(data["chol"])
        fbs=eval(data["fbs"])
        restecg=eval(data["restecg"])
        thalach=eval(data["thalach"])
        exang=eval(data["exang"])
        oldpeak=eval(data["oldpeak"])
        slope=eval(data["slope"])
        ca=eval(data["ca"])
        thal=eval(data["thal"])


        print("age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal",age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        med_ins = Medicalinsurance(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        ans = med_ins.get_prediction()
        return jsonify({"Result is":f"predicted insurance price is: {ans}"})
    # else:
    #     print("work done") 
    #     return jsonify({"Result is":f"predicted insurance price is: {ans}"})
    else:
        # data = request.form   
        # print("DATA is",data)

        age=eval(request.args.get("age"))
        sex=eval(request.args.get("sex"))
        cp=eval(request.args.get("cp"))
        trestbps=eval(request.args.get("trestbps"))
        chol=eval(request.args.get("chol"))
        fbs=eval(request.args.get("fbs"))
        restecg=eval(request.args.get("restecg"))
        thalach=eval(request.args.get("thalach"))
        exang=eval(request.args.get("exang"))
        oldpeak=eval(request.args.get("oldpeak"))
        slope=eval(request.args.get("slope"))
        ca=eval(request.args.get("ca"))
        thal=eval(request.args.get("thal"))

        print("age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal",age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        med_ins = Medicalinsurance(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        ans = med_ins.get_prediction()
        return jsonify({"Result is":f"predicted insurance price is: {ans}"})

if __name__=="__main__":
    app.run(host = "localhost",port=config.PORT_NUMBER)