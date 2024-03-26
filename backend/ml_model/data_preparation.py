import pandas as pd
import re

def load_data(file_path):
    """
    Load data from a CSV file into a Pandas DataFrame.
    
    Parameters:
    - file_path: The path to the CSV file to be loaded.
    
    Returns:
    - A Pandas DataFrame containing the loaded data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise Exception(f"The file at {file_path} was not found.")

def clean_text(text):
    """
    Clean the text data using regex to remove unwanted characters and whitespace.
    
    Parameters:
    - text: The raw string of text to be cleaned.
    
    Returns:
    - The cleaned text as a string.
    """
    # Remove HTML tags and lowercase text
    text = re.sub(r'<.*?>', '', text).lower()
    # Remove punctuations and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_data(df, text_columns):
    """
    Preprocess the job listing data by cleaning specified text columns.
    
    Parameters:
    - df: The DataFrame with the job listing data.
    - text_columns: A list of column names in the DataFrame to clean.
    
    Returns:
    - The DataFrame with the text data cleaned.
    """
    for column in text_columns:
        df[column] = df[column].astype(str).apply(clean_text)
    return df

if __name__ == "__main__":
    # Path to your CSV file with labeled data
    file_path = 'ml_model/data/labeled_data.csv'
    try:
        df = load_data(file_path)

        # Preprocess the text data; specify the names of the columns that contain text
        text_columns = ['description', 'qualifications']
        df = preprocess_data(df, text_columns)

        # Save the preprocessed data back to a CSV
        preprocessed_file_path = 'ml_model/data/Preprocessed_Labeled_Data.csv'
        df.to_csv(preprocessed_file_path, index=False)
        print(f"Preprocessed data saved to {preprocessed_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")