# An HTTP request is made up of three parts:
#
# The request line, which tells the server what kind of request is being sent (GET, POST, etc.) and what resource it's looking for;
# The header, which sends the server additional information (such as which client is making the request)
# The body, which can be empty (as in a GET request) or contain data (if you're POSTing or PUTing information, that information is contained here).
# Instructions
# Check out the text in the editor. This is what a simple request looks like! Note the POST information in the request line, the header information below it, and the data to be POSTed at the bottom.
#
# Click Save & Submit Code once you're all set; on the next page, you'll learn to make this request on your own.


############ Request line #############
# POST /learn-http HTTP/1.1

############## Header ################
# Host: www.codecademy.com
# Content-Type: text/html; charset=UTF-8

############### Body #################
# Name=Eric&Age=26
