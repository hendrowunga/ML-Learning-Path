import iris_classifier as ic

# Load & preprocess data
X, Y, scaler = ic.load_and_preprocess_data()

# Split data
X_train, X_test, y_train, y_test = ic.split_data(X, Y)

# Build network
net = ic.build_network(X_train)

# Train network
error = ic.train_network(net, X_train, y_train)
print(f"Training selesai. Epochs: {len(error)}, MSE terakhir: {error[-1]}")

# Evaluate model
predict, y_true, acc = ic.evaluate_network(net, X_test, y_test)
print(f"Predicted: {predict}")
print(f"True     : {y_true}")
print(f"Accuracy : {acc:.2f}")

# Predict data baru
irisBaru = [6.7, 3.3, 5.7, 2.5]
kelas = ic.predict_new_data(net, scaler, irisBaru)
print(f"Hasil klasifikasi data baru {irisBaru}: Kelas {kelas}")
