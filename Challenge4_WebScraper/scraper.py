import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://example.com"

def scrape_website():
    response = requests.get(URL, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    data.append(["Example Data 1", "Example Data 2", "Example Data 3"])

    df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3"])
    df.to_csv('output/data.csv', index=False)

    print("Data saved to output/data.csv")

scrape_website()
