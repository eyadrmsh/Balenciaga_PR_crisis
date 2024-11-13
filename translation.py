import os
import pandas as pd
from tqdm.auto import tqdm
from deep_translator import GoogleTranslator
import logging
import multiprocessing as mp
import time


LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, 'translation_log.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

BATCH_SIZE = 1000
PARTS_FOLDER = "data_parts"
TRANSLATED_FOLDER = "translated_parts"
os.makedirs(PARTS_FOLDER, exist_ok=True)
os.makedirs(TRANSLATED_FOLDER, exist_ok=True)


def translate_row(row):
    """Translate a single row with a delay to avoid rate limits."""
    text, lang = row['text'], row['lang']
    try:
        time.sleep(0.25) 
        return GoogleTranslator(source=lang, target='en').translate(text)
    except Exception as e:
        logging.error(f"Translation failed for lang={lang}: {e}")
        return 'not_translated'


def split_data(input_file, num_parts=100):
    """Split the data into `num_parts` and save as separate files."""
    data = pd.read_pickle(input_file)
    non_eng_tweets = data[data['lang'] != 'en']
    non_eng_tweets = non_eng_tweets.reset_index(drop=True)

    part_size = len(non_eng_tweets) // num_parts + 1


    for i in tqdm(range(0, len(non_eng_tweets), part_size), desc="Splitting Data"):
        part = non_eng_tweets.iloc[i:i + part_size].reset_index(drop=True)
        part_file = os.path.join(PARTS_FOLDER, f'part_{i // part_size}.pkl')
        part.to_pickle(part_file)
        logging.info(f"Saved part: {part_file}")


def process_part(part_file):
    """Process a single part and save translated results."""
    part = pd.read_pickle(part_file)


    if 'translated' not in part.columns:
        part['translated'] = ''


    with mp.Pool(mp.cpu_count()) as pool:
        translated_texts = pool.map(translate_row, part.to_dict('records'))


    part['translated'] = translated_texts
    translated_file = os.path.join(TRANSLATED_FOLDER, os.path.basename(part_file))
    part.to_pickle(translated_file)
    logging.info(f"Translated part saved: {translated_file}")


def process_all_parts():

    part_files = [os.path.join(PARTS_FOLDER, f) for f in os.listdir(PARTS_FOLDER) if f.endswith('.pkl')]

    for part_file in tqdm(part_files, desc="Processing Parts"):
        process_part(part_file)

    logging.info("All parts translated and saved.")


if __name__ == "__main__":
    INPUT_FILE = '/Users/deryadurmush/Desktop/Jobs /balenciaga/balenciaga_scarped.pkl'
    split_data(INPUT_FILE, num_parts=100)
    process_all_parts()


