# DZIEŃ 80

import hashlib
import base64
import os

FILE_NAME = "url_shortener.txt"

def save_to_file(short_url, original_url):
    with open(FILE_NAME, "a") as f:
        f.write(f"{short_url}{original_url}\n")

def load_urls():
    if not os.path.exists(FILE_NAME):
        return {}

    url_dict = {}
    with open(FILE_NAME, "r") as f:
        for line in f:
            short_url, original_url = line.strip().split()
            url_dict[short_url] = original_url

    return url_dict

def generate_short_url(original_url):
    hash_obj = hashlib.sha256(original_url.encode("utf-8"))
    hash_str = hash_obj.hexdigest()
    b64_encoded = base64.b64encode(hash_str.encode("utf-8"))[:6]
    short_url = b64_encoded.decode("utf-8").replace("/", "_").replace("+", "-")
    return short_url

def main():
    url_dict = load_urls()

    while True:
        user_input = input("Podaj adres URL lub skrócony adres URL (q aby zakończyć): ")

        if user_input == "q":
            break

        if user_input in url_dict:
            print(f"Oryginalny adres URL: {url_dict[user_input]}")
        else:
            short_url = generate_short_url(user_input)
            if short_url not in url_dict:
                save_to_file(short_url, user_input)
                url_dict[short_url] = user_input
                print(f"Skrócony adres URL: {short_url}")
            else:
                print("Skrót już istnieje. Spróbuj ponownie.")

if __name__ == "__main__":
    main()