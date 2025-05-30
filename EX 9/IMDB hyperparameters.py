import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.metrics import classification_report
import numpy as np

# Load and preprocess IMDB dataset
vocab_size = 10000  # Use top 10,000 words
maxlen = 200  # Max sequence length

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# Hyperparameter configurations to try
configs = [
    {"embedding_dim": 32, "lstm_units": 32, "dropout": 0.2, "epochs": 3},
    {"embedding_dim": 64, "lstm_units": 64, "dropout": 0.3, "epochs": 3},
    {"embedding_dim": 128, "lstm_units": 128, "dropout": 0.5, "epochs": 3},
]

# Run experiments
for i, config in enumerate(configs):
    print(f"\n🧪 Config {i+1}: {config}")
    
    # Build model
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=config["embedding_dim"], input_length=maxlen),
        LSTM(config["lstm_units"], dropout=config["dropout"]),
        Dense(1, activation='sigmoid')
    ])

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train model
    model.fit(x_train, y_train, epochs=config["epochs"], batch_size=128, validation_split=0.2, verbose=0)

    # Evaluate
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"✅ Test Accuracy: {accuracy:.4f}")

    # Predictions and classification report
    y_pred = (model.predict(x_test) > 0.5).astype("int32")
    print("🔍 Classification Report:")
    print(classification_report(y_test, y_pred, digits=4))
