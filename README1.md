

# Google Gemini API Integration

This Python script interacts with the Google Gemini API to send a query and retrieve a response. The API key for authentication is securely stored in a `.env` file, and the script sends a query to the Gemini model and prints the answer.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library
- Acivate virtual environments for dependencies
- Install dependencies from requirements.txt (pip install -r requirements.txt)

### Install the Required Libraries

Before running the script, you need to install the required libraries. You can install them using pip:

```bash
pip install requests python-dotenv
```

## Setup

1. **API Key**: 
   - You need to have a valid Google Gemini API key. You can obtain one by following the instructions on the [Google Gemini API documentation](https://developers.google.com/generative-language).
   - Create a `.env` file in the same directory as the Python script and store the API key like this:

   **.env**:
   ```
   API_KEY=your-google-gemini-api-key
   ```

2. **Environment Variables**:
   - The script uses the `python-dotenv` library to load environment variables from the `.env` file. Ensure that your `.env` file contains the API key as shown above.

3. **Python Script**:
   - The script will load the API key, send a query to the Google Gemini API, and print the answer to the console.

## Running the Script

1. Clone or download the repository, and ensure the script is in the same directory as your `.env` file.
2. To run the script, simply use the following command:

   ```bash
   python gemini_query.py
   ```

   This will output the response from the Google Gemini API.

## How It Works

1. The script uses the **`requests`** library to send a `POST` request to the Google Gemini API endpoint with the query.
2. The API key is read from the `.env` file using the **`python-dotenv`** library, and it is passed as a query parameter.
3. The response from the API is parsed, and the text answer is printed.

## Example Output

When you run the script with the query `"Who is Donald Trump?"`, you might see an output similar to:

```
Answer from Gemini API: Donald Trump is an American politician, businessman, and television personality who served as the 45th president of the United States from 2017 to 2021. Before entering politics, he was a prominent figure in the real estate industry, developing and branding numerous skyscrapers, hotels, and golf courses. He also achieved significant media recognition through his appearances on television, notably as the host of *The Apprentice*...
```

## Error Handling

- If the API key is missing or invalid, the script will raise an error with the message: `"API key is missing. Please set it in the .env file."`.
- If there's an issue with the network or the API request fails, an appropriate error message will be displayed.




### Summary

- The `README1.md` file outlines how to set up and run the Python script, which interacts with the Google Gemini API.
- It describes how to install dependencies, set up the `.env` file with the API key, and run the script to query the API.
- It also includes error handling instructions and expected outputs.

