#The good news is that if you've gotten this far (that is, to the Codecademy website), you've met HTTP before! It's that little bit before the "www" in a website's address. Some browsers might hide it from you, but Codecademy's full address is:
#
#http://www.codecademy.com/
#The HTTP stands for HyperText Transfer Protocol. HyperText is text with links in it (like this!) and a transfer protocol is a fancy way of saying "rules for getting something from one place to another." In this case, the rules are for transferring web pages to your browser.


from urllib2 import Request, urlopen, URLError

request = Request('http://placekitten.com/')

try:
	response = urlopen(request)
	kittens = response.read()
	print kittens[559:1000]
except URLError, e:
    print 'No kittez. Got an error code:', e
