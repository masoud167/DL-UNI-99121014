from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load the handwritten digits dataset
digits = load_digits()

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2, random_state=42
)

# Define a list of hyperparameter sets to test
configs = [
    {"hidden_layer_sizes": (50,), "activation": "relu", "learning_rate_init": 0.001},
    {"hidden_layer_sizes": (100,), "activation": "relu", "learning_rate_init": 0.001},
    {"hidden_layer_sizes": (50, 50), "activation": "tanh", "learning_rate_init": 0.01},
    {"hidden_layer_sizes": (100, 100), "activation": "logistic", "learning_rate_init": 0.005},
]

# Evaluate different configurations
results = []

for i, params in enumerate(configs):
    clf = MLPClassifier(
        hidden_layer_sizes=params["hidden_layer_sizes"],
        activation=params["activation"],
        learning_rate_init=params["learning_rate_init"],
        max_iter=300,
        random_state=42
    )
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results.append((params, acc))
    
    print(f"\n🧪 Config {i+1}: {params}")
    print(f"✅ Accuracy: {acc:.4f}")
    print("🔍 Classification Report:")
    print(classification_report(y_test, y_pred))
    print("📊 Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# Plot accuracy for each config
labels = [f"{c['hidden_layer_sizes']}-{c['activation']}-{c['learning_rate_init']}" for c, _ in results]
accuracies = [acc for _, acc in results]

plt.figure(figsize=(10, 5))
plt.bar(labels, accuracies, color='skyblue')
plt.xticks(rotation=45)
plt.ylabel("Accuracy")
plt.title("Evaluation of Hyperparameter Configurations")
plt.tight_layout()
plt.show()
