import requests

# Define the URL and the file path
url = "https://www.kaggle.com/api/v1/datasets/download/sid321axn/malicious-urls-dataset"
output_file = "/Phishing-detector/DataFiles/malicious-urls-dataset.zip"

# Send a GET request to the URL
response = requests.get(url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Write the file in chunks to handle large files
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"File downloaded successfully to {output_file}")
else:
    print(f"Failed to download the file. HTTP status code: {response.status_code}")
