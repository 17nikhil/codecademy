# Anatomy of a Response
# The HTTP response structure mirrors that of the HTTP request. It contains:
#
# A response line (line 2), which includes the three-digit HTTP status code;
#
# A header line or lines (line 3), which include further information about the server and its response;
#
# The body (line 5 and line 6), which contains the text message of the response (for example, "404" would have "file not found" in its body).
#
# Check out the example response in the editor. See how its structure resembles the request layout?
#
# Instructions
# Header lines can contain lots of extra information. We've made a request to placekitten.com on line 10. On line 13, print the header information (which will display as a big, ugly dictionary) by calling print on the headers attribute of response.


################## Example response ##########################
# HTTP/1.1 200 OK
# Content-Type: text/xml; charset=UTF-8

# <?xml version="1.0" encoding="utf-8"?>
# <string xmlns="https://www.codecademy.com/">Accepted</string>
##############################################################

import requests
response = requests.get("http://placekitten.com/")

# print the header information from the response
print response.headers
