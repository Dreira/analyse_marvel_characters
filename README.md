# Analyse Marvel Characters

This project fetches characters from the Marvel API and the number of comics they appear in. It uses Python to interact with the Marvel API and outputs the results.

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
git clone https://github.com/yourusername/marvel-api-characters.git
cd marvel-api-characters
``` 

### Step 2: Create a Virtual Environment

```bash 
git clone https://github.com/yourusername/marvel-api-characters.git
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
### Step 5: Obtain Marvel API Keys
1. Go to the Marvel Developer Portal.
2. Sign up or log in to your account.
3. Navigate to 'Get a key'.
4. Create a new application to obtain your Public Key and Private Key.

### Step 6: Configure Environment Variables
Create a .env file in the project directory and add your Marvel API keys:

PUBLIC_KEY=your_public_key
PRIVATE_KEY=your_private_key

### Step 7: Run the Script
```bash
python main.py
```








