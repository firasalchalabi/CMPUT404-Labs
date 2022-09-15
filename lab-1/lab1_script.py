import requests

print(requests.__version__)

google_homepage = requests.get("http://www.google.com")
print(google_homepage.content)

print("=======================================================================")

python_script_file = requests.get("https://github.com/firasalchalabi/CMPUT404-Labs/blob/main/lab-1/lab1_script.py")
print(python_script_file.text)
