
# CBN Circulars Scraper

This Python script extracts circulars from the Central Bank of Nigeria (CBN) website and downloads the associated PDF files. It saves the circular data in a JSON file and downloads the PDFs to a local directory. The script uses **BeautifulSoup** to scrape the web page and **requests** to handle HTTP requests and download PDFs.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `json` library (built-in with Python)

### Install the Required Libraries

Before running the script, install the necessary libraries using the following command:

```bash
pip install requests beautifulsoup4
```

## Setup

1. **Directory Structure**: 
   - The script will create a directory named `cbn_pdfs` to store the downloaded PDFs.
   - The circular data (title, PDF link, and saved file path) will be saved in a JSON file named `cbn_circular.json`.

2. **Running the Script**: 
   - The script automatically fetches circular data from the CBN website and saves it locally. 
   - Ensure you have Python installed on your machine, then run the script.

## How It Works

1. **Extract Circular Data**: 
   - The script sends a `GET` request to the URL `https://www.cbn.gov.ng/Documents/circulars.html` and retrieves the HTML content.
   - It parses the page using **BeautifulSoup** to find all the links that contain PDF files.

2. **Download PDFs**:
   - The script checks if the links point to PDF files by checking if the `href` attribute ends with `.pdf`.
   - It constructs the full URL for the PDF (in case of relative links), downloads the file, and saves it with a sanitized filename (spaces are replaced with underscores).
   - The downloaded PDFs are saved in a directory named `cbn_pdfs`.

3. **Save Data in JSON**:
   - The script creates a JSON file (`cbn_circular.json`) containing the extracted circular data, including:
     - Circular title
     - PDF link
     - Path where the PDF was saved locally.

4. **Error Handling**:
   - If a PDF fails to download due to any network issues, the script will log an error but continue processing the rest of the links.

## Running the Script

1. Clone or download the repository, and ensure the script is in your working directory.
2. To run the script, simply use the following command:

   ```bash
   python cbn_circular_scraper.py
   ```

3. Once the script completes, it will generate two outputs:
   - A **`cbn_pdfs`** directory containing all downloaded PDFs.
   - A **`cbn_circular.json`** file containing the extracted circular data.

## Output

- **`cbn_pdfs/`**: A folder containing all downloaded PDFs.
- **`cbn_circular.json`**: A JSON file containing a list of circulars, with each item containing the following:
  - `title`: The title of the circular.
  - `pdf_link`: The URL to the PDF file on the CBN website.
  - `saved_pdf_path`: The local path where the PDF was saved.



## Notes

- **Sanitization of Filenames**: The script replaces spaces in the circular titles with underscores (`_`) to create valid filenames for the PDFs.
- **Error Handling**: The script uses `requests.exceptions.RequestException` to handle any errors that occur while fetching the webpage or downloading the PDFs.
- **PDF Download Folder**: The script creates a folder called `cbn_pdfs` where all the PDFs will be stored. Ensure you have write permissions in the current working directory.


### Summary

- The **README2.md** file provides instructions on setting up and running the Python script that scrapes CBN circulars from the web.
- It details the steps for installing dependencies, running the script, and understanding the output.
- It also explains how the script works, including how it downloads PDFs, processes circulars, and saves the data in a JSON file.