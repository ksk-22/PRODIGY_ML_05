# PRODIGY_ML_05

## Food Recognition and Calorie Estimation Model

This project was completed as part of the Prodigy InfoTech Machine Learning Internship.

The objective of this task is to develop a machine learning model capable of recognizing food items from images and estimating their calorie content.

### Food Classes
- Pizza
- Burger
- Sushi
- Salad

### Technologies Used
- Python
- OpenCV
- NumPy
- Scikit-learn

### Model
A Support Vector Machine (SVM) classifier was trained on image data. Images were resized, converted to grayscale, flattened into feature vectors, and used to train the model.

### Dataset
Custom image dataset containing 41 images distributed across four food categories.

### Results
Accuracy: 11%

Classification Report:

```text
              precision    recall  f1-score   support

Pizza          0.00      0.00      0.00         2
Burger         0.00      0.00      0.00         2
Sushi          0.00      0.00      0.00         3
Salad          0.25      0.50      0.33         2

accuracy                            0.11         9
macro avg       0.06      0.12      0.08         9
weighted avg    0.06      0.11      0.07         9
```

### Calorie Reference
| Food | Calories (Approx.) |
|------|-------------------|
| Pizza | 285 kcal |
| Burger | 295 kcal |
| Sushi | 130 kcal |
| Salad | 150 kcal |

### How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

### Repository Structure

```text
PRODIGY_ML_05/
├── Pizza/
├── Burger/
├── Sushi/
├── Salad/
├── main.py
├── requirements.txt
└── README.md
```

### Learning Outcomes
- Image preprocessing using OpenCV
- Feature extraction from images
- Multi-class classification using SVM
- Performance evaluation using classification metrics
- Basic calorie estimation mapping
