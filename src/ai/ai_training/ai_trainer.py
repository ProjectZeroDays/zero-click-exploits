import logging
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

logging.basicConfig(level=logging.ERROR)

def train_model(training_data, model_path="src/ai/models/model_path", config=None):
    logging.info("Starting AI model training")
    if not training_data:
        logging.error("Training data is empty.")
        return
    learning_rate = config['ai']['learning_rate'] if config else 0.001
    # Load data and preprocess
    X, y = preprocess_data(training_data)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define model architecture
    model = create_model(learning_rate, X_train.shape[1], config)

    # Train the model
    model.fit(X_train, y_train, epochs=100, validation_data=(X_val, y_val))

    # Evaluate the model
    y_pred = model.predict(X_val)
    y_pred = (y_pred > 0.5).astype(int)
    accuracy = accuracy_score(y_val, y_pred)
    precision = precision_score(y_val, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_val, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_val, y_pred, average='weighted', zero_division=0)
    logging.info(f"Model Evaluation: Accuracy={accuracy:.4f}, Precision={precision:.4f}, Recall={recall:.4f}, F1-Score={f1:.4f}")

    # Save the model
    model.save(model_path)
    logging.info("AI model training completed")

def preprocess_data(training_data):
    logging.info("Preprocessing training data")
    # Example data: [target_ip, target_port, exploit_type, outcome]
    X = np.array([[item[0], item[1], item[2]] for item in training_data])
    y = np.array([item[3] for item in training_data])

    # One-hot encode exploit_type
    encoder = OneHotEncoder(handle_unknown='ignore')
    X_encoded = encoder.fit_transform(X[:, [2]]).toarray()

    # Scale numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X[:, :2])

    # Combine encoded and scaled features
    X_processed = np.concatenate((X_scaled, X_encoded), axis=1)
    return X_processed, y

def create_model(learning_rate, input_shape, config):
    logging.info("Creating AI model")
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(config['ai']['dense_layer_1'] if config else 64, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dense(config['ai']['dense_layer_2'] if config else 32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    return model

def integrate_with_new_components(new_component_data, config):
    logging.info("Integrating with new components")
    # Placeholder for integration logic with new components
    integrated_data = {
        "new_component_training_data": new_component_data.get("training_data", []),
        "new_component_model_config": new_component_data.get("model_config", {})
    }
    return integrated_data

def ensure_compatibility(existing_data, new_component_data, config):
    logging.info("Ensuring compatibility with existing AI training logic")
    # Placeholder for compatibility logic
    compatible_data = {
        "existing_training_data": existing_data.get("training_data", []),
        "existing_model_config": existing_data.get("model_config", {}),
        "new_component_training_data": new_component_data.get("training_data", []),
        "new_component_model_config": new_component_data.get("model_config", {})
    }
    return compatible_data
