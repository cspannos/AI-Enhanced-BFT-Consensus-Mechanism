import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model():
    """Train and return an AI model using data from dataset.csv."""
    # Load the dataset
    dataset_path = "data/dataset.csv"
    dataset = pd.read_csv(dataset_path)

    # Split into features and labels
    features = dataset[["uptime", "past_faults", "response_time", "stake"]].values
    labels = dataset["label"].values

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)

    # Print accuracy
    print(f"Training complete. Model accuracy: {model.score(X_test, y_test) * 100:.2f}%")
    return model
