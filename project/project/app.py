import os
import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Path for saving uploaded images
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model
MODEL_PATH = 'models/pneumonia_model.h5'
model = load_model(MODEL_PATH)

print("Model loaded. Ready to process requests.")

# Helper function to preprocess image
def model_predict(img_path, model):
    # Get the model input shape (usually the first layer)
    target_size = model.input_shape[1:3]  # (height, width)
    
    # Load image and resize to model's input shape
    img = image.load_img(img_path, target_size=target_size)  
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Make prediction
    preds = model.predict(img_array)
    return preds

# Routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Save the uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Predict using the model
        preds = model_predict(file_path, model)
        os.remove(file_path)  # Remove the file after prediction

        # Interpret the result
        if preds[0, 0] > 0.5:
            result = "PNEUMONIA DETECTED"
            probability = preds[0, 0]
        else:
            result = "NORMAL"
            probability = 1 - preds[0, 0]

        # Returning both the prediction and the probability
        return jsonify({
            'result': result,
            'probability': float(probability),
            'message': 'Prediction made successfully'
        })

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
