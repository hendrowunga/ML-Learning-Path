from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics import accuracy_score
import numpy as np
import neurolab as nl

def load_and_preprocess_data():
    iris = datasets.load_iris()
    X_raw = iris.data
    y_raw = iris.target

    # Normalisasi fitur
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X_raw)

    # One-hot encoding label (untuk sklearn >= 1.4)
    encoder = OneHotEncoder(sparse_output=False)
    Y = encoder.fit_transform(y_raw.reshape(-1, 1))

    return X, Y, scaler

def split_data(X, Y, test_size=0.3):
    return train_test_split(X, Y, test_size=test_size, random_state=42)

def build_network(X_train, hidden_neurons=4, learning_rate=0.1):
    minmax = [[min(col), max(col)] for col in X_train.T]
    net = nl.net.newff(minmax, [hidden_neurons, 3], transf=[nl.trans.TanSig(), nl.trans.PureLin()])
    net.trainf.lr = learning_rate
    return net

def train_network(net, X_train, y_train, epochs=1000, goal=0.1, show=25):
    error = net.train(X_train, y_train, epochs=epochs, show=show, goal=goal)
    return error

def evaluate_network(net, X_test, y_test):
    output = net.sim(X_test)
    predict = np.argmax(output, axis=1)
    y_true = np.argmax(y_test, axis=1)
    acc = accuracy_score(y_true, predict)
    return predict, y_true, acc

def predict_new_data(net, scaler, new_data):
    new_data_scaled = scaler.transform([new_data])
    output = net.sim(new_data_scaled)
    class_id = np.argmax(output, axis=1)[0]
    return class_id
