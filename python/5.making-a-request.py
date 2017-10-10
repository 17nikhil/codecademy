# Making a Request
# You saw a request in the first exercise. Now it's time for you to make your own! (Don't worry, we'll help.)
#
# On line 1, we've imported urlopen from the urllib2 module, which is the Python way of bringing in additional functionality we'll need to make our HTTP request. A module is just a collection of extra Python tools.
#
# On line 4, we'll use urlopen on placekitten.com in preparation for our GET request, which we make when we read from the site on line 5. (On line 6, we limit the response to specific character numbers to control the input we get back—this is what gives us our cat image.)
#
# We'll need your help to complete the request!
#
# Instructions
# On line 4, declare a variable, kittens, and set it equal to calling urlopen on http://placekitten.com. No need for the "www"!
#
# On line 8, print the body variable so we can see some of the data we got back.


from urllib2 import urlopen

# Open http://placekitten.com/ for reading on line 4!
kittens = urlopen('http://placekitten.com')
response = kittens.read()
body = response[559:1000]

# Add your 'print' statement here!
print body
