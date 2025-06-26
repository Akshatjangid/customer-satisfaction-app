from flask import Flask, render_template, request
import pickle
import numpy as np
import os  # Added for Render compatibility

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Input features in the exact same order as training
    feature_order = [
        'Age',
        'Flight Distance',
        'Inflight entertainment',
        'Baggage handling',
        'Cleanliness',
        'Departure Delay in Minutes',
        'Arrival Delay in Minutes',
        'Gender',
        'Customer Type_disloyal Customer',
        'Type of Travel_Personal Travel',
        'Class_Eco',
        'Class_Eco Plus'
    ]

    try:
        features = [float(request.form[feature]) for feature in feature_order]
        final_input = np.array([features])
        prediction = model.predict(final_input)
        output = "Satisfied" if prediction[0] == 1 else "Not Satisfied"
        return render_template('index.html', prediction_text=f'Prediction: {output}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    # Use port from environment variable for Render (default 5000 for local dev)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# from flask import Flask, render_template, request
# import pickle
# import numpy as np

# app = Flask(__name__)

# # Load the trained model
# model = pickle.load(open('model.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Input features in the exact same order as training
#     feature_order = [
#         'Age',
#         'Flight Distance',
#         'Inflight entertainment',
#         'Baggage handling',
#         'Cleanliness',
#         'Departure Delay in Minutes',
#         'Arrival Delay in Minutes',
#         'Gender',
#         'Customer Type_disloyal Customer',
#         'Type of Travel_Personal Travel',
#         'Class_Eco',
#         'Class_Eco Plus'
#     ]

#     try:
#         features = [float(request.form[feature]) for feature in feature_order]
#         final_input = np.array([features])
#         prediction = model.predict(final_input)
#         output = "Satisfied" if prediction[0] == 1 else "Not Satisfied"
#         return render_template('index.html', prediction_text=f'Prediction: {output}')
#     except Exception as e:
#         return render_template('index.html', prediction_text=f'Error: {str(e)}')

# if __name__ == '__main__':
#     app.run(debug=True)











# from flask import Flask, render_template, request
# import pickle
# import numpy as np

# app = Flask(__name__)rediction_text=f'Error: {str(e)}')

# if __name__ == '__main__

# # Load model
# model = pickle.load(open('model.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     features = [float(x) for x in request.form.values()]
#     final_input = np.array([features])
#     prediction = model.predict(final_input)
#     return render_template('index.html', prediction_text=f'Prediction: {prediction[0]}')

# if __name__ == '__main__':
#     app.run(debug=True)