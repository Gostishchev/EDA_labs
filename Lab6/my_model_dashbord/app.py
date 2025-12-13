#app.py
from flask import Flask, request, jsonify
import pandas as pd
from catboost import CatBoostClassifier

app = Flask(__name__)

# Загружаем модель
model = CatBoostClassifier()
model.load_model('/app/models/trained_model.cbm')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        content = request.json
        # Создаём DataFrame
        df = pd.DataFrame([content])  

        # Предсказываем вероятность класса 1 (Revenue = 1)
        proba = model.predict_proba(df)
        revenue_prob = proba[0][1]  # вероятность покупки

        return jsonify({
            'Revenue_Probability': float(revenue_prob)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)