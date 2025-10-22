🩺 Pneumonia Detection using CNN and Streamlit

This project demonstrates a deep learning-based approach to detect pneumonia from chest X-ray images using a Convolutional Neural Network (CNN).
The trained model is deployed as an interactive Streamlit web app, allowing users to upload X-ray images and get real-time predictions.

🔗 Live Demo: [Pneumonia Detection App](https://pneumonia-detection-using-cnn-and-flask-j3yxdj7lawzims3ohjyzfi.streamlit.app/)


🚀 Overview

Pneumonia is a critical lung infection that requires early and accurate diagnosis.
This project leverages TensorFlow/Keras CNN models to classify X-ray images as Pneumonia or Normal, and provides an easy-to-use web interface for medical analysis or educational use.

🧠 Features
🧩 Model

Built using Convolutional Neural Network (CNN) architecture.

Trained on a publicly available chest X-ray dataset.

Saved in .keras format for TensorFlow 2.x compatibility.

💻 Web Interface

Built using Streamlit for fast and elegant deployment.

Users can upload X-ray images and get immediate predictions.

Displays prediction probability and class label (Pneumonia / Normal).

📊 Performance (Test Metrics)
Metric	Score
Accuracy	79.37%
Precision	0.8124
Recall	0.7892
F1-Score	0.8006
Loss	1.6562
🧰 Tools and Technologies Used

Programming Language: Python

Deep Learning Framework: TensorFlow / Keras

Web Framework: Streamlit

Data Visualization: Matplotlib, Seaborn

Dataset: Public Chest X-ray Dataset (Kaggle)

⚙️ Methodology

Data Preprocessing

Image resizing (120×120), normalization, and augmentation.

Balanced dataset to prevent model bias.

Model Architecture

Multiple convolutional and pooling layers.

Fully connected dense layers for classification.

Activation: ReLU and Sigmoid for binary output.

Training

Loss Function: Binary Cross-Entropy

Optimizer: Adam

Epochs: Tuned for best validation accuracy.

Evaluation

Metrics: Accuracy, Precision, Recall, and F1-score.

🧪 Installation and Usage
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/pneumonia-detection-using-cnn-and-flask.git
cd pneumonia-detection-using-cnn-and-flask

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

4️⃣ Usage

Upload a chest X-ray image.

View prediction result (Pneumonia / Normal) instantly.

📈 Results

The final CNN model achieved strong classification performance:

Accuracy: 79.37%

F1-Score: 0.80

Loss: 1.65

Model File: models/pneumonia_model.keras

🤝 Contributing

Contributions are always welcome!
Feel free to:

Improve the model or web UI

Add Grad-CAM or explainability visualizations

Optimize inference speed

Submit a pull request or open an issue anytime.

🧾 License

This project is open-source and available under the MIT License.
