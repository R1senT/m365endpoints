import requests

def fetch_urls(json_url, output_file):
    try:
        # Fetch the JSON data from the URL
        response = requests.get(json_url)
        response.raise_for_status()
        data = response.json()

        # Extract URLs from the JSON data
        urls = []
        for item in data:
            if 'urls' in item:
                urls.extend(item['urls'])

        # Write the URLs to a text file
        with open(output_file, 'w') as file:
            for url in urls:
                file.write(url + '\n')

        print(f"Successfully wrote {len(urls)} URLs to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    json_url = "https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7"
    output_file = "urls.txt"
    fetch_urls(json_url, output_file)