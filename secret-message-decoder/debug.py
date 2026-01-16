import requests
from bs4 import BeautifulSoup

def debug_parse(url):
    # Fetch the Google Doc
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table in the document
    table = soup.find('table')
    if not table:
        print("No table found!")
        return

    rows = table.find_all('tr')
    print(f"Total rows found: {len(rows)}")
    print("\n--- First 10 rows ---")

    for i, row in enumerate(rows[:10]):
        cells = row.find_all('td')
        print(f"Row {i}: {len(cells)} cells")
        for j, cell in enumerate(cells):
            text = cell.get_text().strip()
            print(f"  Cell {j}: '{text}' (repr: {repr(text)})")
        print()

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    debug_parse(url)
