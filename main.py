import requests
from send_email import send_email

topic = "apple"

api_key = "6e8ba66f8f8249679aa2eade17e3cd6d"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2023-08-08&"
       "to=2023-08-08&"
       "sortBy=popularity&"
       "apiKey=6e8ba66f8f8249679aa2eade17e3cd6d&"
       "language=en")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles an descriptions
body = ""
for article in content["articles"][:20]:
       if article["title"] is not None:
              body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)