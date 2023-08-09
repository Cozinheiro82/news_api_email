import requests
from send_email import send_email

api_key = "6e8ba66f8f8249679aa2eade17e3cd6d"

url = ("https://newsapi.org/v2/everything?q=apple&from=2023-08-08&to=2023-08-08&sortBy="
       "popularity&apiKey=6e8ba66f8f8249679aa2eade17e3cd6d")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles an descriptions
body = ""
for article in content["articles"]:
       if article["title"] is not None:
              body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)