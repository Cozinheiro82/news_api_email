import requests

api_key = "6e8ba66f8f8249679aa2eade17e3cd6d"

url = ("https://newsapi.org/v2/everything?q=apple&from=2023-08-08&to=2023-08-08&sortBy="
       "popularity&apiKey=6e8ba66f8f8249679aa2eade17e3cd6d")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles an descriptions
for article in content["articles"]:
       print(article["title"])
       print(article["description"])
