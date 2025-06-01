from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


dept_map = {'0': 0, '1': 1, '2': 2}  
salary_map = {'0': 0, '1': 1, '2': 2}  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        department = dept_map[request.form['Department']]
        salary = salary_map[request.form['salary']]
        years = float(request.form['time_spend_company'])
        satisfaction = float(request.form['Emp_Satisfaction'])
        rating = float(request.form['last_evaluation'])

        
        final_input = np.array([[department, salary, years, satisfaction, rating]])

       
        prediction = model.predict(final_input)

    
        if prediction[0] == 1:
            result = "The employee is likely to leave the company."
        else:
            result = "The employee is likely to stay in the company."

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
