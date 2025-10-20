# config/settings.py

import logging

# --- General Settings ---
INPUT_FILE_PATH = "emails_or_numbers.txt"
VALID_OUTPUT_FILE = "Valid.txt"
INVALID_OUTPUT_FILE = "Invalid.txt"
UNKNOWN_OUTPUT_FILE = "Unknown.txt" # For cases where a definitive valid/invalid cannot be determined

# --- Logging Settings ---
LOG_LEVEL = logging.INFO # INFO for standard operation, DEBUG for detailed request/response logs

# --- Proxy Settings (for `requests` proxy usage) ---
USE_PROXIES = False # Set to True if you want to use proxies with requests
PROXY_FILE_PATH = "config/proxies.txt"
PROXY_CHECK_TIMEOUT = 10
PROXY_CHECK_URL = "https://login.microsoftonline.com" # Example URL to check proxy connectivity

# --- Multiprocessing Settings ---
# Number of concurrent workers. Start with a low number and increase cautiously.
NUM_THREADS = 60 

# --- Number Generation Settings (if you want to generate numbers instead of using an input file) ---
GENERATE_NUMBERS = True
GENERATED_NUMBERS_FILE = "generated_numbers.txt"
PHONE_NUMBER_PREFIX = "207" # e.g., "234" for Nigeria
GENERATED_NUMBER_LENGTH = 10 # Total length of the generated number, e.g., 11 for 234xxxxxxxx
NUM_NUMBERS_TO_GENERATE = 1000000 # How many numbers to generate if GENERATE_NUMBERS is True

# --- CSRF Token Settings ---
CSRF_TOKEN_REFRESH_HOURS = 20