from sklearn.model_selection import train_test_split
import mlflow
import mlflow.xgboost

from src.data.ingest import load_data
from src.data.validate import validate_data
from src.features.build_features import build_features
from src.models.train import train_model
from src.models.evaluate import evaluate_model

def run_pipeline():
    df = load_data("data/raw/printer_data.csv")
    
    validate_data(df)
    
    df = build_features(df)

    X = df.drop("failure", axis=1)
    y = df["failure"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    with mlflow.start_run():
        model = train_model(X_train, y_train)

        acc, report = evaluate_model(model, X_test, y_test)

        mlflow.log_metric("accuracy", acc)
        mlflow.xgboost.log_model(model, "model")

        print("Accuracy:", acc)
        print(report)

if __name__ == "__main__":
    run_pipeline()
