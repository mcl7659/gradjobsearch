from transformers import Trainer
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

def evaluate_model(trainer, test_dataset):
    # Make predictions on the test dataset
    predictions, label_ids, metrics = trainer.predict(test_dataset)

    # Flatten predictions and labels
    preds_flat = np.argmax(predictions.logits, axis=1).flatten()
    labels_flat = label_ids.flatten()

    # Calculate and print the classification report
    print(classification_report(labels_flat, preds_flat, target_names=['Not Suitable', 'Suitable']))
    print("Accuracy:", accuracy_score(labels_flat, preds_flat))

    return metrics

if __name__ == "__main__":
    # Load your trained model and test dataset here
    # Example: trained_model = ...
    # Example: test_dataset = ...

    # Initialize the trainer
    trainer = Trainer(model=trained_model)

    # Evaluate the model
    metrics = evaluate_model(trainer, test_dataset)
    print(metrics)