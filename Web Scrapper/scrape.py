# Program to scrape a website and extract a table from it.
# Once we get the table correct, save it in a CSV file.

import requests
from bs4 import BeautifulSoup
import pandas as pd


if __name__ == '__main__':
    url = "ENTER A URL HERE"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    table1 = soup.find('table', attrs={})  # Enter a table identifiable attribute here by inspecting the element like { 'class': 'test' }

    # Obtain every title of columns with tag <th>
    headers = []
    for i in table1.find_all('th'):
        title = i.text.strip()
        headers.append(title)

    # Create a dataframe
    mydata = pd.DataFrame(columns=headers)

    # Create a for loop to fill mydata
    for j in table1.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text.strip() for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row

    # Export to csv
    mydata.to_csv('data.csv', index=False)
