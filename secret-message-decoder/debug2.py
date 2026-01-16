import requests
from bs4 import BeautifulSoup

def show_all_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # Skip header

    print("All coordinate data:")
    print("x, y, char")
    print("-" * 20)

    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:
            x = cells[0].get_text().strip()
            char = cells[1].get_text().strip()
            y = cells[2].get_text().strip()
            print(f"{x}, {y}, '{char}'")

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    show_all_data(url)
