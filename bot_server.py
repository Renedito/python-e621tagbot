from http.server import BaseHTTPRequestHandler, HTTPServer
from tags import tagsList
import random
import tweepy
import os

# load_dotenv("D:\Documents\Github\python-e621tagbot\API_keys.env")

client = tweepy.Client(
    consumer_key = os.environ.get("API_key"),
    consumer_secret = os.environ.get("API_key_secret"),
    bearer_token = os.environ.get("Bearer_token"),
    access_token = os.environ.get("Access_Token"),
    access_token_secret = os.environ.get("Access_Token_Secret")
)
print(client.consumer_key)
print(client.consumer_secret)
print(client.bearer_token)
print(client.access_token)
print(client.access_token_secret)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code (200 for success)
        self.send_response(200)

        # Set the response headers (e.g., content type)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Define the content of the response
        random_entry = random.choice(tagsList)
#       client.create_tweet(text = random_entry)
        self.wfile.write(random_entry.encode())

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()
    
if __name__ == "__main__":
    run_server()