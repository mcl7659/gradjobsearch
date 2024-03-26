from torch.utils.data import Dataset
import torch

class JobDescriptionsDataset(Dataset):
    """
    A PyTorch Dataset class to handle the job descriptions, qualifications, and labels.
    """
    def __init__(self, descriptions, qualifications, labels, tokenizer, max_token_len=512):
        """
        Args:
        descriptions (list of str): The job descriptions.
        qualifications (list of str): The job qualifications.
        labels (list of int): The labels for each description (1 for suitable, 0 for not suitable).
        tokenizer: The BERT tokenizer.
        max_token_len (int): Maximum length of the tokenized input.
        """
        self.descriptions = descriptions
        self.qualifications = qualifications
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_token_len = max_token_len

    def __len__(self):
        """
        Returns the length of the dataset.
        """
        return len(self.descriptions)

    def __getitem__(self, index):
        """
        Returns a single item from the dataset.
        """
        description = str(self.descriptions[index])
        qualification = str(self.qualifications[index])
        label = self.labels[index]
        text = description + " " + qualification  # Combine description and qualification
        
        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,  # Adds '[CLS]' and '[SEP]'
            max_length=self.max_token_len,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt',  # Return PyTorch tensors
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }