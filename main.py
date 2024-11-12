import os
import random
import time
import requests

def multi_token_convo():
    # Logo
    logo = """
    \\
    ...
    """

    print(logo)

 # Facebook Graph API endpoint
thread_id = input("\033[1;32mEnter thread ID: ")
url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

# Token file paths
token_file_paths = input("\033[33mEnter token file paths (separated by comma): ").split(',')

# Message file path
message_file_path = input("\033[34mEnter message file path: ")

# Haters name
haters_name = input("\033[35mEnter haters name: ")

# Delay between messages
delay_between_messages = int(input("\033[36mEnter delay between messages: "))

# Read tokens from files
access_tokens = []
token_names = []
for token_file_path in token_file_paths:
    with open(token_file_path.strip(), "r") as token_file:
        for i, token in enumerate(token_file.readlines()):
            access_tokens.append(token.strip())
            token_names.append(f"Token {i+1}")

# Read messages from file
messages = []
with open(message_file_path, "r") as message_file:
    messages = message_file.readlines()

def get_account_name(token):
    try:
        response = requests.get(f'(link unavailable)')
        data = response.json()
        return data['name']
    except Exception as e:
        return "Unknown"

def send_message(token, message, thread_id, haters_name):
    try:
        message_url = f"{url}"
        message_params = {
            "access_token": token,
            "message": f"{haters_name} {message}"
        }
        message_response = requests.post(message_url, params=message_params)
        if message_response.status_code == 200:
            print(f"""
\033[34m
✪✭═══════•『 BL4CK M4FI4 0N FIR3』•═══════✭✪
""")
            account_name = get_account_name(token)
            print(f"\033[38;5;25m[+] AAPKA MESSAGE MAFIA KI TARAF SE SEND KIYA GYA HAI Thread ID: {thread_id} ✪✭════════✭✪ Token: {token_names[access_tokens.index(token)]} ✪✭════════✭✪  Account Name: {account_name} ✪✭════════✭✪  Haters Name: {haters_name} ✪✭════════✭✪  Message: {message}\033[0m")
        else:
            print(f"""
\033[31;5;196m
✪✭═══════•『 BL4CK M4FI4 0N FIR3』•═══════✭✪
""")
            print(f"\033[38;5;196mM3SS4G3 F9IL3D H0 GYA HAI Thread ID: {thread_id} ✪✭════════✭✪ Token: {token_names[access_tokens.index(token)]} ✪✭════════✭✪  Haters Name: {haters_name} ✪✭════════✭✪  Message: {message}\033[0m")
    except Exception as e:
        print(str(e))

def process_messages_thread():
    try:
        while True:
            random_token = random.choice(access_tokens)
            random_message = random.choice(messages).strip()
            send_message(random_token, random_message, thread_id, haters_name)
            time.sleep(delay_between_messages)
    except Exception as e:
        print(str(e))

process_messages_thread()

def single_convo_without_haters_name():
    # Facebook Graph API endpoint
thread_id = input("Enter thread ID: ")
url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

# Token file path
token_file_path = input("Enter token file path: ")

# Message file path
message_file_path = input("Enter message file path: ")

# Time value
time_value = int(input("Enter time value: "))

# Message count
message_count = int(input("Enter message count: "))

# Delay between messages
delay_between_messages = int(input("Enter delay between messages: "))

# Read tokens from file
access_tokens = []
with open(token_file_path, "r") as token_file:
    access_tokens = token_file.readlines()

# Read messages from file
messages = []
with open(message_file_path, "r") as message_file:
    messages = message_file.readlines()

def send_message(token, message, thread_id):
    try:
        message_url = f"{url}"
        message_params = {
            "access_token": token,
            "message": message
        }
        message_response = requests.post(message_url, params=message_params)
        if message_response.status_code == 200:
            print(f"Message sent: {message}")
        else:
            print(f"Failed to send message: {message}")
    except Exception as e:
        print(str(e))

def process_messages_thread():
    try:
        for i in range(message_count):
            random_token = random.choice(access_tokens).strip()
            random_message = random.choice(messages).strip()
            send_message(random_token, random_message, thread_id)
            time.sleep(delay_between_messages)
    except Exception as e:
        print(str(e))

process_messages_thread()

def main():
    os.system('clear')
    print("Select Option:")
    print("1. MULTI TOKEN CONVO")
    print("2. SINGLE CONVO WITHOUT HATERS NAME")
    option = input("Enter your choice (1/2): ")
    if option == "1":
        multi_token_convo()
    elif option == "2":
        single_convo_without_haters_name()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
