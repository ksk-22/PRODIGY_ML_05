import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

DATASET_PATH = 'dataset'
classes = ['Pizza', 'Burger', 'Sushi', 'Salad']

X = []
y = []

for label, food in enumerate(classes):
    folder = os.path.join(DATASET_PATH, food)
    if not os.path.exists(folder):
        continue

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        img = cv2.imread(path)
        if img is None:
            continue

        img = cv2.resize(img, (64, 64))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        X.append(img.flatten())
        y.append(label)

X = np.array(X) / 255.0
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = SVC(kernel='rbf')
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions, target_names=classes))

calories = {
    'Pizza': 285,
    'Burger': 295,
    'Sushi': 130,
    'Salad': 150
}

print('\nFood Calorie Reference:')
for food, kcal in calories.items():
    print(f'{food}: {kcal} kcal per serving')
