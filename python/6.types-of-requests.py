# The Four Verbs
# The number of HTTP methods you'll use is quite small—there are just four HTTP "verbs" you'll need to know! They are:
#
# GET: retrieves information from the specified source.
# POST: sends new information to the specified source.
# PUT: updates existing information of the specified source.
# DELETE: removes existing information from the specified source.
# So when we sent our GET request to placekitten.com using urlopen(), we retrieved information. When you add to or update your blog, you're sending POST or PUT requests; when you delete a tweet, there goes a DELETE request.
#
# Instructions
# Another way to communicate through HTTP in Python is with the requests library (available here). On line 4, pass http://placekitten.com/ to the get() method of requests and assign the result to a variable named kittens. This is just like calling urllib2.urlopen(), but uses a different library.
#
# On line 6, we get the text out of the webpage using the text attribute of the new object named kittens, then we use subscripting to display just a portion of the text string.


import requests

# Make a GET request here and assign the result to kittens:
kittens = requests.get('http://placekitten.com/')

print kittens.text[559:1000]
