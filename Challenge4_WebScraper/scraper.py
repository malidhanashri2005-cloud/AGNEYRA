import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

# Website URL
URL = "https://example.com"  # Tumhi je website scrape karaychi aahe, tya URL ne replace kara

# Function to scrape website
def scrape_website():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to retrieve data")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: extract table data
    data = []
    table = soup.find('table')  # Website madhe je table scrape karaycha aahe
    if table:
        for row in table.find_all('tr')[1:]:  # Skip header row
            cols = row.find_all('td')
            data.append([col.text.strip() for col in cols])
    
    # Save data to CSV
    df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3"])  # Update column names
    df.to_csv('output/data.csv', index=False)
    print("Data saved to output/data.csv")

# Schedule scraper
schedule.every().day.at("10:00").do(scrape_website)  # Run daily at 10 AM

print("Scraper started... Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)
