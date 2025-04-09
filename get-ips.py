import requests

def fetch_ips(json_ip, output_file):
    try:
        # Fetch the JSON data from the IPs
        response = requests.get(json_ip)
        response.raise_for_status()
        data = response.json()

        # Extract IPs from the JSON data
        ips = []
        for item in data:
            if 'ips' in item:
                ips.extend(item['ips'])

        # Write the IPs to a text file
        with open(output_file, 'w') as file:
            for ip in ips:
                file.write(ip + '\n')

        print(f"Successfully wrote {len(ips)} IPs to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    json_ip = "https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7"
    output_file = "ips.txt"
    fetch_ips(json_ip, output_file)