from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load trained model
model = joblib.load('xgb_rul_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
        return jsonify({'RUL_Prediction': round(float(prediction), 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
