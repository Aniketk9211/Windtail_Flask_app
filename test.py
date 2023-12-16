from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/patient', methods=['GET', 'POST'])
def doctor():
    if request.method == 'POST':
        # Process form data for the doctor here
        doctor_data = {
            'name': request.form.get('name'),
            'specialization': request.form.get('specialization'),
            # Add more fields as needed
        }
        # You can store this data in a database or use it as needed

    return render_template('patient.html')

@app.route('/patient', methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        # Process form data for the patient here
        patient_data = {
            'name': request.form.get('name'),
            'symptoms': request.form.get('symptoms'),
            # Add more fields as needed
        }
        # You can store this data in a database or use it as needed

    return render_template('patient.html')

if __name__ == '__main__':
    app.run(debug=True)
