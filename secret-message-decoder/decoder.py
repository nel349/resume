import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')[1:]

    chars = []
    max_x, max_y = 0, 0

    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:
            x = int(cells[0].get_text().strip())
            c = cells[1].get_text().strip()
            y = int(cells[2].get_text().strip())
            chars.append((x, y, c))
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, c in chars:
        grid[y][x] = c

    for row in reversed(grid):
        print(''.join(row))

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
    decode_secret_message(url)
