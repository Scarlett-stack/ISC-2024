import requests

TARGET_URL = "http://localhost:8080"
WORDLIST_PATH = "wordlist.txt"


def fuzz_directories(target_url, wordlist_path):

    # TODO1 - open the wordlist file

    f = open(wordlist_path, 'r')
    directories = f.readlines()

    for dir_name in directories:

        # TODO2 - remove all whitelines and newlines from the directories
        dir = dir_name.strip()
        # TODO3 - build the url
        url = target_url + "/" + dir
        # TODO4 - send a GET request to the constructed URL
        rasp = requests.get(url)

        #print( rasp)
        if rasp.status_code == 200:
            print(f"Found valid path: {url} - Status: {rasp.status_code}")
        #else:
            #print(f"Path not found: {url} - Status: {rasp.status_code}")

        # TODO5 - verify if the directory exists or not by checking the
        #         response and print a meaningful message

       # pass


fuzz_directories(TARGET_URL, WORDLIST_PATH)
