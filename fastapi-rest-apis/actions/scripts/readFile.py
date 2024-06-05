import sys
import urllib.request
import json

def read_file_from_url(url):
    try:
        # Add a user-agent header to the request
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        # Open the URL and read the contents
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            return data
    except Exception as e:
        return e
    
def get_output(input_json):
    try:
        file_url = input_json["url"]
        file_contents = read_file_from_url(file_url)
        if file_contents:
            return (json.dumps({"output": {"type": "json", "content": {"text": file_contents}}}))
    except:
        return (json.dumps({"output": {"type": "error", "content": "Error reading file."}}))
