#!/usr/bin/env python3

# Most of the code was copied from Alex's login.py
# Link: https://github.com/aianta/cgi-lab/blob/master/login.py

import cgi
import os
from templates import login_page
from templates import secret_page
from secret import username, password

def parse_cookies(cookie_string):
    result = {}
    if cookie_string == "":
        return result
        
    cookies = cookie_string.split(";")
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]

    return result

cookies = parse_cookies(os.environ["HTTP_COOKIE"])

form = cgi.FieldStorage()

username_input = form.getfirst("username")
password_input = form.getfirst("password")

header = ""
header += "Content-Type: text/html\r\n"    # HTML is following

body = ""

if (username_input == username and password_input == password) or ('logged' in cookies and cookies['logged'] == "true"):
    body += secret_page(username, password)
    header += "Set-Cookie: logged=true; Max-Age=60\r\n"
    header += "Set-Cookie: cookie=nom\r\n"
    body += "<h1>A terrible secret</h1>"
else:
    body += login_page()

print(header)
print()
print(body)
