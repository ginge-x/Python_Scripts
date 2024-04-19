import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(filename):
    with open(filename, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()  # Clean up newline or any extra spaces
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should change your password')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'finished!'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py passwords.txt")
        sys.exit(1)
    filename = sys.argv[1]
    sys.exit(main(filename))