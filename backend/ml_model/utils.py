import numpy as np
import datetime
import torch
from sklearn.metrics import accuracy_score, f1_score
from transformers import BertForSequenceClassification, BertTokenizer

def compute_metrics(preds, labels):
    """
    Calculate accuracy and F1 score from predictions and labels.

    Args:
        preds (np.ndarray): The raw model predictions (logits).
        labels (np.ndarray): The true labels.

    Returns:
        dict: A dictionary with accuracy and F1 score.
    """
    preds_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()
    acc = accuracy_score(labels_flat, preds_flat)
    f1 = f1_score(labels_flat, preds_flat, average='weighted')
    return {
        'accuracy': acc,
        'f1': f1
    }

def format_time(elapsed):
    """
    Format elapsed seconds into a string hh:mm:ss.

    Args:
        elapsed (float): Time in seconds.

    Returns:
        str: Time in hours, minutes, and seconds.
    """
    # Round to the nearest second.
    elapsed_rounded = int(round((elapsed)))
    
    # Format as hh:mm:ss
    return str(datetime.timedelta(seconds=elapsed_rounded))

def save_checkpoint(model, tokenizer, save_path):
    """
    Save a model and tokenizer to the specified path.

    Args:
        model (PreTrainedModel): A Hugging Face model to be saved.
        tokenizer (PreTrainedTokenizer): A Hugging Face tokenizer to be saved.
        save_path (str): The path to save the model and tokenizer.
    """
    model.save_pretrained(save_path)
    tokenizer.save_pretrained(save_path)

def load_checkpoint(save_path):
    """
    Load a model and tokenizer from the specified path.

    Args:
        save_path (str): The path to load the model and tokenizer from.

    Returns:
        tuple: A tuple of the model and tokenizer.
    """
    model = BertForSequenceClassification.from_pretrained(save_path)
    tokenizer = BertTokenizer.from_pretrained(save_path)
    return model, tokenizer

def set_seed(seed_value=42):
    """
    Set seed for reproducibility.

    Args:
        seed_value (int, optional): Seed value. Defaults to 42.
    """
    np.random.seed(seed_value)
    torch.manual_seed(seed_value)
    torch.cuda.manual_seed_all(seed_value)  # if you are using GPU