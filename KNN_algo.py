import numpy as np
from collections import Counter

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((np.array(p1) - np.array(p2)) ** 2))

def knn_predict(X_train, y_train, test_point, k=3):
    distances = []
    for i in range(len(X_train)):
        dist = euclidean_distance(test_point, X_train[i])
        distances.append((dist, y_train[i]))
    distances.sort(key=lambda x: x[0])
    k_nearest = [label for _, label in distances[:k]]
    return Counter(k_nearest).most_common(1)[0][0]

X_train = [
    [18, 12000], [19, 15000], [20, 13000], [21, 16000], [22, 17000],
    [23, 18000], [24, 20000], [25, 22000], [26, 25000], [27, 27000],
    [28, 30000], [29, 32000], [30, 35000], [31, 37000], [32, 39000],
    [33, 41000], [34, 43000], [35, 45000], [36, 47000], [37, 49000]
]

y_train = [
    'Skinny', 'Skinny', 'Skinny', 'Skinny', 'Skinny',
    'Regular', 'Regular', 'Regular', 'Regular', 'Regular',
    'Baggy', 'Baggy', 'Baggy', 'Baggy', 'Baggy',
    'Baggy', 'Baggy', 'Baggy', 'Baggy', 'Baggy'
]

try:
    age = int(input("Enter age: "))
    income = int(input("Enter monthly income in NPR: "))
    test_point = [age, income]
    k = 3
    prediction = knn_predict(X_train, y_train, test_point, k)
    print(f"\nFor Age: {age} and Income: NPR {income}, recommended jeans type is: {prediction}")
except ValueError:
    print("Please enter valid numbers for age and income.")
