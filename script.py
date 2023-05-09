import requests, os

token = os.getenv("GH_TOKEN")

def make_request(url):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(url, headers=headers)
    return response.json()

print(make_request("https://api.github.com/repos/raizen-analytics/new-fenix/commits"))