# Analyse Marvel Characters

This project fetches characters from the Marvel API and the number of comics they appear in. 

## Prerequisites

- Python 3.x installed on your system
- Access to the Marvel API (requires an API key)

## Getting a Marvel API Key

1. Go to the [Marvel Developer Portal](https://developer.marvel.com/).
2. Sign up for an account or log in if you already have one.
3. Go to the 'Get a key' section.
4. Create a new application and note down your **Public Key** and **Private Key**.

## Project Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/analyse_marvel_characters.git
cd marvel-api-characters
``` 

### Step 2: Create a Virtual Environment
```bash 
python3 -m venv venv
```
### Step 3: Activate the Virtual Environment
- On Windows (Command Prompt):
``` bash
.\venv\Scripts\activate
```
 - On Windows (PowerShell):
``` bash 
.\venv\Scripts\Activate.ps1
```
 - On macOS/Linux (Bash/Zsh):

``` bash 
source venv/bin/activate
```
### Step 4: Install Dependencies
```bash 
pip install -r requirements.txt
```

### Step 7: Configure API key
Create a .json file in the project directory and add your Marvel API keys:

{PUBLIC_KEY=your_public_key
PRIVATE_KEY=your_private_key}

### Step 7: Run the Script
```bash
python main.py
```








