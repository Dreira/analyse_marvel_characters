
import logging
import pandas as pd
from utils import load_api_keys, fetch_characters

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Load API keys from secret.json
    public_key, private_key = load_api_keys()

    if not public_key or not private_key:
        logging.error("Failed to load Marvel API keys from secret.json.")
        return

    # Fetch characters and their comic counts using loaded keys
    characters_df = fetch_characters(public_key, private_key)

    if not characters_df.empty:
        # Export to CSV
        characters_df.to_csv('marvel_characters.csv', index=False)
        logging.info('Data exported to marvel_characters.csv')
    else:
        logging.warning('No data fetched. CSV export skipped.')

if __name__ == '__main__':
    main()