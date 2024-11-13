import os
import pandas as pd
from tqdm.auto import tqdm

TRANSLATED_FOLDER = "translated_parts"
OUTPUT_FILE = "merged_translated.pkl"

def merge_translated_parts(translated_folder, output_file):
    part_files = [os.path.join(translated_folder, f) for f in os.listdir(translated_folder) if f.endswith('.pkl')]
    merged_data = []

    for part_file in tqdm(part_files, desc="Merging translated parts"):
        df = pd.read_pickle(part_file)
        merged_data.append(df)

    merged_df = pd.concat(merged_data, axis=0).reset_index(drop=True)

    merged_df.to_pickle(output_file)
    print(f"Merged data saved to: {output_file}")

if __name__ == "__main__":
    merge_translated_parts(TRANSLATED_FOLDER, OUTPUT_FILE)
