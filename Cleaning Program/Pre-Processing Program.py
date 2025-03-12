# For parallization
import ray
# For data handling
import pandas as pd
from pandas import DataFrame
import numpy as np
# For text cleaning
import cleantext as clean
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

try:
    english_stopwords = set(stopwords.words('english'))
except:
    import nltk
    nltk.download('stopwords')
    english_stopwords = set(stopwords.words('english'))


################# PROGRAM SPECIFICATIONS #################

UNCLEANED_DATASET_PATH = '995,000_rows.csv' # Has to be a .csv
'''The relative (to the program) or absolute filepath to the csv to be cleaned.'''

COLUMNS_TO_BE_CLEANED = ['content']
'''A list of (text) columns in the csv that will be cleaned.'''

DROP_NAN_VALUES = ['content']
'''A list of the columns were rows with NaN in these columns, will be removed.'''

################# USER INITIALIZATION #################

print(f"""
This cleaning program produces a new file called 'cleaned_dataset_MIN.csv' or 'cleaned_dataset_FULL.csv' in the same directory as this program, from the file '{UNCLEANED_DATASET_PATH}'.
The program assumes that the file is in the same directory as the program.

Rows with missing values in the following columns will be removed before cleaning: {DROP_NAN_VALUES}
The following columns will be cleaned: {COLUMNS_TO_BE_CLEANED}

The following cleaning steps will be peformed:
  1)   Lowercasing everything
  2)   Replacing URLs and Domains with <URL>
  3)   Replacing Emails with <EMAIL>
  4)   Replacing Dates with <DATE>
  5)   Replacing Numbers with <NUM>
  6)   Removing punctuation
  7)   Replacing currency symbols with <CUR>
  8)   Normalizing whitespaces
  9)   Tokenization
  10)  Removing stopwords
  11)  Stemming

The cleaned columns will not contain text, but instead a list of tokens.
  
The program has two modes: [M]inimal and [F]ull.
    The Minimal mode will produce a new csv file with the following columns: {['id']+['cleaned '+ c for c in COLUMNS_TO_BE_CLEANED]}.
    The 'id' columns is for merging with the main dataset.
    The file name will be: 'cleaned_dataset_MIN.csv'

    The Full mode will produce a new csv file with all the columns in the original csv and the following new columns: {['cleaned '+ c for c in COLUMNS_TO_BE_CLEANED]}.
    The file name will be: 'cleaned_dataset_FULL.csv'

Make sure that the libraries in 'requirements.txt' are installed.
This program was made to work with 'Python 3.12'.
""")

MODE = input("""
Press [M] to select the Minimal Mode.
Press [F] to select the Full Mode.

[Press Enter to choose the selected mode]
""").lower()

input("""
[Press Enter to begin the cleaning process]
""")

################# DEFINING CLEANING FUNCTIONS #################
print('Compiling cleaning functions...')

# Converting to lowercase
def lowercase(text:str):
    return text.lower()

url_regex = re.compile(r'(?:http[s]?://)?(?:www\.)?[\w]+\.[a-z]{2,}[\w#-_]*')
# Replacing URLs
def sub_URL(text:str):
    return url_regex.sub(' <URL> ', text)

email_regex = re.compile(r'[\w._-]+@[\w._-]+\.[a-z]{2,}')
# Replacing Emails
def sub_EMAIL(text:str):
    return email_regex.sub(' <EMAIL> ', text)

date1_regex = re.compile(r'(?:\b\d{1,4}[-/\.]\d{1,2}[-/\.]\d{1,4}\b)') # matcher 20-02-2025 og 20/02/2025 og 20.02.2025 og 2-20-2025 og 2/20/2025 og 2025-02-20 og 20/2/25 2/20/25
date2_regex = re.compile(r'(?:(?:(?:the )?(?:[123]\d|\d)(?:st|nd|rd|th)? (?:of )?)?(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|sep|dec|mon|tue|wed|thu|fri|sat|sun)[a-z]*\.?(?: (?:the )?\d{1,4}(?:st|nd|rd|th)?,?))(?: (?:20|19)[\d]{2}s?\b)?')
date3_regex = re.compile(r'(?:(?:(?:the )?(?:[123]\d|\d)(?:st|nd|rd|th)? of )(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|sep|dec|mon|tue|wed|thu|fri|sat|sun)[a-z]*)')
date4_regex = re.compile(r'(?:20|19)[\d]{2}s?\b')
# Replacing Dates
def sub_DATE(text:str):
    return date4_regex.sub(' <DATE> ', date3_regex.sub(' <DATE> ', date2_regex.sub(' <DATE> ', date1_regex.sub(' <DATE> ', text))))

num_regex = re.compile(r'\d(?:\d|\.|\,|st|nd|rd|th)*')
# Replacing Numbers
def sub_NUM(text:str):
    return num_regex.sub(' <NUM> ', text)

punct_regex = re.compile(r'[^\w\s](?=[a-z])')
# Replacing Punctuation in words
def sub_punct(text:str):
    return punct_regex.sub(' ', text)

# rep URL, rep Email, rep tlf.nr., rep Numbers, del punct, rep Valuta
def cleaning_module(text:str):
    return clean.normalize_whitespace(clean.remove_punct(clean.replace_currency_symbols(text)))

# Cleaning function containing the above functions.
def CleanText(text:str) -> str :
    """Returns a cleaned string.
    
    Args:
        text (str) : A (raw) uncleaned text (document).
    Returns:
        str : The same text, but cleaned."""

    return cleaning_module(
        sub_punct(
            sub_NUM(
                sub_DATE(
                    sub_EMAIL(
                        sub_URL(
                            lowercase(
                                text
                            )
                        )
                    )
                )
            )
        )
    )

################# READING FILE #################

# Reading file
print(f"Reading '{UNCLEANED_DATASET_PATH}'...")
if MODE == 'm':
    news_corpus = pd.read_csv(UNCLEANED_DATASET_PATH, usecols=(['id']+COLUMNS_TO_BE_CLEANED)).dropna(subset=DROP_NAN_VALUES)
else:
    news_corpus_FULL = pd.read_csv(UNCLEANED_DATASET_PATH).dropna(subset=DROP_NAN_VALUES).drop(columns=['Unnamed: 0'])
    news_corpus = news_corpus_FULL[['id']+COLUMNS_TO_BE_CLEANED]

################# PREPARING PARALLIZATION #################

print('Preparing parallization...')
ray.shutdown()
ray.init()

# initializes a stemmer and defines pipeline
stemmer = PorterStemmer()
def preprocessing_pipeline(text:str):
    return [stemmer.stem(word, to_lowercase=0) for word in CleanText(text).split() if word not in english_stopwords]

@ray.remote
def apply_parallel(df_chunk:DataFrame):
    for column in COLUMNS_TO_BE_CLEANED:
        df_chunk['cleaned '+column] = df_chunk[column].apply(preprocessing_pipeline)
    print(f'Finished cleaning +1/{num_of_chunks}...')
    return df_chunk

# splitting the dataset for parallization.
num_of_chunks = 24
csv_parts = np.array_split(news_corpus, num_of_chunks)

################# PARALLEL CLEANING #################

print('Cleaning in progress...')
results = ray.get([apply_parallel.remote(split) for split in csv_parts])

################# POST PROCESSING AND FINISH #################

# combining the result
print('Combining results...')
news_corpus = pd.concat(results, ignore_index=True).drop(columns=COLUMNS_TO_BE_CLEANED)

print('Writing to file...')
if MODE == 'm':
    news_corpus.to_csv('cleaned_dataset_MIN.csv', index=False)
else:
    news_corpus_FULL = news_corpus_FULL.merge(news_corpus, on='id')
    news_corpus_FULL.to_csv('cleaned_dataset_FULL.csv', index=False)

print('Done!')


