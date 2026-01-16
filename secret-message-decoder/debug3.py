import requests
from bs4 import BeautifulSoup

def check_document(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check how many tables
    tables = soup.find_all('table')
    print(f"Number of tables found: {len(tables)}")

    # Check for any text content
    print("\n--- Document text content (first 500 chars) ---")
    body = soup.find('body')
    if body:
        text = body.get_text()[:500]
        print(text)

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    check_document(url)
