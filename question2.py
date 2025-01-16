


import os
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

# URL of the CBN Circulars page
url = "https://www.cbn.gov.ng/Documents/circulars.html"

# Directory to save downloaded PDFs
download_dir = "cbn_pdfs"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Function to download a PDF and save it with a new name
def download_pdf(pdf_url, filename):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
        file_path = os.path.join(download_dir, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
        return file_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {pdf_url}: {e}")
        return None

# Function to extract circulars and save them to a JSON file
def extract_circulars_and_download_pdfs():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Checking if the page content is fetched successfully
    print("Page content fetched successfully.")
    soup = BeautifulSoup(response.text, "html.parser")

    # Finding all relevant circulars
    circulars = []
    for link in soup.find_all('a', href=True):
        pdf_url = link['href']
        if pdf_url.endswith('.pdf'):
            title = link.get_text(strip=True)
            pdf_url = urljoin(url, pdf_url)
            filename = title.replace(" ", "_") + ".pdf"
            saved_pdf_path = download_pdf(pdf_url, filename)
            if saved_pdf_path:
                circulars.append({
                    "title": title,
                    "pdf_link": pdf_url,
                    "saved_pdf_path": saved_pdf_path
                })

    with open('cbn_circular.json', 'w') as json_file:
        json.dump(circulars, json_file, indent=4)
    print(f"Extracted {len(circulars)} circulars and saved to cbn_circular.json")

extract_circulars_and_download_pdfs()



