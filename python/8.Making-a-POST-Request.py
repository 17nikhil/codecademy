# Using the Requests library, you can make a POST request by using the requests.post() method. You aren't just GETting data with a POST - you can pass your own data into the request as well, like so:
#
# requests.post("http://placekitten.com/", data="myDataToPost")
# We're going to make the same request as the one shown on line 2 through line 5. Request header lines (line 3 and line 4) are usually created automatically, so we don't have to worry about them. The body of the request on line 5 is what we will need to add to our POST.
#
# Instructions
# We created the body of the request as a dictionary on line 9. Call requests.post() on the URL http://codecademy.com/learn-http/ and pass the argument data=body, as in the example above, to create the POST request; set this result equal to a new variable named response.


########## Example request #############
# POST /learn-http HTTP/1.1
# Host: www.codecademy.com
# Content-Type: text/html; charset=UTF-8
# Name=Eric&Age=26

import requests

body = {'Name': 'Eric', 'Age': '26'}

# Make the POST request here, passing body as the data:
response = requests.post('http://codecademy.com/learn-http/', data=body)
