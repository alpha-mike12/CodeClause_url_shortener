import requests

# the URL you want to shorten
API_KEY = "a90dad7006624e50b97deb67a46c44e84d770"

# the URL you want to shorten
URL = input('Enter URL to shorten : ') 
name = input('Enter name in shortened url : ') # preferred name in the URL

API_REQ_URL = f"https://cutt.ly/api/api.php?key={API_KEY}&short={URL}&name={name}"

# make the API request
responseObj = requests.get(API_REQ_URL).json()["url"]
if responseObj["status"] == 7:
    shortened_url = responseObj["shortLink"]
    print("Shortened Link :", shortened_url)
else:
    print("Error in getting URL shortening")