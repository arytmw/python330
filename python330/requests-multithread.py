import requests
from concurrent.futures import ThreadPoolExecutor

url = 'https://httpbin.org/uuid'

def fetch(session,url):
    with session.get(url) as response:
        print(response.json()['uuid'])


def main():
    with ThreadPoolExecutor(max_workers=40) as executor:
        with requests.Session() as session:
            executor.map(fetch,[session]*100,[url]*100)
            executor.shutdown(wait=True)

main()
