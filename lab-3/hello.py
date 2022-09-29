#!/usr/bin/env python3

mport os
import json
import templates

# Turn the environ object into a dictionary
env_variables = dict(os.environ)

#print("Content-Type: application/json", end="\r\n\r\n")
#print(json.dumps(env_variables))

print("Content-Type: text/html", end="\r\n\r\n")
#print(templates._wrapper(os.environ["HTTP_USER_AGENT"]))

print(templates.login_page())
