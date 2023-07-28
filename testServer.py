import requests

def handle_get_request(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the response content to a local file
            print(response.text)
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace "http://localhost:8000/your_file.txt" with the actual URL of your file
    file_url = "http://localhost:8000/"

    handle_get_request(file_url)