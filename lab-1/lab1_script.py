import requests

print(requests.__version__)

google_homepage = requests.get("http://www.google.com")
print(google_homepage.status_code)
