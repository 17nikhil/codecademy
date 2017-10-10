# Parsing XML
# XML (which stands for eXtensible Markup Language) is very similar to HTML—it uses tags between angle brackets. The difference is that XML allows you to use tags that you make up, rather than tags that the W3C decided on. For instance, you could create an API that returns information about a pet:
#
# <pet>
#   <name>Jeffrey</name>
#   <species>Giraffe</species>
# </pet>
# As long as you document the structure of your API's response, other people can use your API to get information about <pet>s.
#
# Instructions
# Check out the code in the editor. We've imported xml.dom.minidom from the xml module for parsing XML, and we're just using the open() method to read from pets.txt (under the "Files") tab. Reading from this file is just like reading XML sent by a server.
#
# Click Save & Submit Code to continue.
