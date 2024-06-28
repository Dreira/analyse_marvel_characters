import requests
import hashlib
import time
import pandas as pd
import json
import logging

BASE_URL = 'https://gateway.marvel.com/v1/public'

def load_api_keys(filename='secret.json'):
    """
    Loads Marvel API keys (public and private) from a JSON file.

    Args:
        filename (str): Name of the JSON file containing API keys. Default is 'secret.json'.

    Returns:
        tuple: Tuple containing (PUBLIC_KEY, PRIVATE_KEY). Returns (None, None) if file or keys are not found.
    """
    public_key = None
    private_key = None

    try:
        with open(filename, 'r') as f:
            keys = json.load(f)
            public_key = keys.get('PUBLIC_KEY')
            private_key = keys.get('PRIVATE_KEY')
    except FileNotFoundError:
        logging.error(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from '{filename}'.")
    except KeyError as e:
        logging.error(f"Key '{str(e)}' not found in '{filename}'.")

    return public_key, private_key

def generate_hash(timestamp, private_key, public_key):
    """
    Generates MD5 hash required for Marvel API authentication.

    Args:
        timestamp (str): Current timestamp.
        private_key (str): Marvel API private key.
        public_key (str): Marvel API public key.

    Returns:
        str: MD5 hash string.
    """
    hash_input = timestamp + private_key + public_key
    return hashlib.md5(hash_input.encode()).hexdigest()

def fetch_characters(public_key, private_key, limit=100) -> pd.DataFrame:
    """
    Fetches a list of characters from the Marvel API with pagination.

    Args:
        public_key (str): Marvel API public key.
        private_key (str): Marvel API private key.
        limit (int, optional): Number of results to fetch per request (default is 100).

    Returns:
        pd.DataFrame: A DataFrame containing character data (name and comic count).
    """
    timestamp = str(int(time.time()))
    hash_value = generate_hash(timestamp, private_key, public_key)

    url = f'{BASE_URL}/characters'
    offset = 0
    characters = []

    try:
        while True:
            params = {
                'ts': timestamp,
                'apikey': public_key,
                'hash': hash_value,
                'limit': limit,
                'offset': offset
            }

            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()['data']['results']

            for character in data:
                character_name = character['name']
                comic_count = character['comics']['available']
                characters.append({'Character': character_name, 'Comic Count': comic_count})

            if len(data) < limit:
                break
            else:
                offset += limit

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching characters: {str(e)}")

    return pd.DataFrame(characters)