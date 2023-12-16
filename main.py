from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/patient" , methods=["GET", "POST"])
def patient():
  if request.method == "POST":
    patient_data ={
      'patient_name' : request.form.get("patient_name"),
      'date_of_birth' : request.form.get("date_of_birth"),
      'gender': request.form.get("gender"),
      'address' : request.form.get("address"),
      'phone_number' : request.form.get("phone_number"),
      'emergency_contact' : request.form.get("emergency_contact")
      
    }
    # Process the data here (e.g., store it in a database)
    
    # You can store this data in a database or use it as needed

  return render_template("patient.html")





if __name__ == "__main__":
  app.run(debug=True)