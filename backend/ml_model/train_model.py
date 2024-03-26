from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from job_dataset import JobDescriptionsDataset  # Make sure this import matches your dataset class
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    # Load and prepare the dataset
    df = pd.read_csv('/workspaces/gradsearch/ml_model/data/labeled_data.csv')
    train_df, eval_df = train_test_split(df, test_size=0.1)  # Splitting the data

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    train_dataset = JobDescriptionsDataset(
    descriptions=train_df['description'].to_numpy(),
    qualifications=train_df['qualifications'].to_numpy(),
    labels=train_df['is_suitable'].to_numpy(),
    tokenizer=tokenizer,
    max_token_len=128  # Adjust as needed
)

    eval_dataset = JobDescriptionsDataset(
        descriptions=eval_df['description'].to_numpy(),
        qualifications=eval_df['qualifications'].to_numpy(),
        labels=eval_df['is_suitable'].to_numpy(),
        tokenizer=tokenizer,
        max_token_len=128  # Adjust as needed
    )

    # Load the pre-trained BERT model for sequence classification
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir='model',          # Output directory for model and stats
        num_train_epochs=3,              # Number of training epochs
        per_device_train_batch_size=8,   # Batch size for training
        per_device_eval_batch_size=8,    # Batch size for evaluation
        warmup_steps=500,                # Number of warmup steps for learning rate scheduler
        evaluation_strategy='epoch',     # Evaluation strategy to adopt during training
        save_strategy="epoch",
        load_best_model_at_end=True,
    )

    # Initialize the Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset
    )

    # Train the model
    trainer.train()

    # Save the model
    model.save_pretrained('model')

if __name__ == "__main__":
    main()