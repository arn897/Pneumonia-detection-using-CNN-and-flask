# Pneumonia-detection-using-CNN-and-flask
This project demonstrates a machine learning-based approach to detect pneumonia from chest X-ray images using a Convolutional Neural Network (CNN). The application is built with Flask for deploying the model as a web service.

Overview

Pneumonia is a severe respiratory condition that requires timely detection and treatment. This project leverages deep learning techniques to classify chest X-rays into pneumonia-positive or pneumonia-negative categories.

Features

Model:
Trained using a Convolutional Neural Network (CNN) architecture.

Web Interface:
Built using Flask to allow users to upload X-ray images and view predictions.

Performance:
Accuracy: 0.7937
Loss: 1.6562
Precision: 0.8124
Recall: 0.7892
F1-Score: 0.8006

Tools and Technologies Used

Programming Language: Python
Deep Learning Framework: TensorFlow/Keras
Web Framework: Flask
Data Visualization: Matplotlib, Seaborn
Dataset: Publicly available chest X-ray dataset

Methodology

Data Preprocessing:
Image resizing, normalization, and augmentation techniques applied to improve generalization.

Model Architecture:

A custom CNN model designed with multiple convolutional layers, pooling layers, and dense layers.
Training:
The model was trained using a binary cross-entropy loss function and optimized using Adam optimizer.
Evaluation:
Metrics such as accuracy, precision, recall, and F1-score were calculated on the test dataset.
Installation
 
Run the Flask app:
bash
Copy
Edit
python app.py  
Usage
Launch the web app by navigating to http://127.0.0.1:5000/ in your browser.
Upload a chest X-ray image.
View the prediction result (Pneumonia or Normal).
Results
The model achieved an accuracy of 79.37% on the test dataset, with the following metrics:
Precision: 0.8124
Recall: 0.7892
F1-Score: 0.8006
Loss during testing: 1.6562
Contributing
Contributions are welcome! If you have any suggestions or want to improve this project, please feel free to open a pull request or issue.

