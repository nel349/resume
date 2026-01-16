import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    # Fetch the Google Doc
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table in the document
    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # Skip header row

    # Parse the data
    characters = []
    max_x = 0
    max_y = 0

    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:
            x = int(cells[0].get_text().strip())
            char = cells[1].get_text().strip()
            y = int(cells[2].get_text().strip())

            characters.append((x, y, char))
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    # Create the grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place characters in the grid
    for x, y, char in characters:
        grid[y][x] = char

    # Print the grid (reverse order so y=0 is at bottom)
    for row in reversed(grid):
        print(''.join(row))

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
    decode_secret_message(url)
