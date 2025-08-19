from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and scalers
with open('randclf_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('minmax_scaler.pkl', 'rb') as f:
    mx = pickle.load(f)

with open('standard_scaler.pkl', 'rb') as f:
    sc = pickle.load(f)

with open('label_mapping.pkl', 'rb') as f:
    df_dict = pickle.load(f)

# Inverse mapping: label number to crop name
inv_map = {v: k for k, v in df_dict.items()}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[feature]) for feature in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    except Exception:
        error_msg = "Invalid input. Please enter all values correctly."
        return render_template('result.html', prediction=error_msg)

    input_df = pd.DataFrame([features], columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    input_mx = mx.transform(input_df)
    input_scaled = sc.transform(input_mx)

    pred_label = model.predict(input_scaled)[0]
    predicted_crop = inv_map.get(pred_label, "Unknown").capitalize()

    return render_template('result.html', prediction=predicted_crop)

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
