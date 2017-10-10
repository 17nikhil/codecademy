#Did you see that? A few lines of Python pulled in some source code from the PlaceKitten website! (They're very good at cat pictures.)

#We can use HTTP to grab just about any web page on the Internet. But where do those web pages come from? They come from other computers on the Internet called servers.

#The Internet is full of clients (like you!) who ask for various resources (web pages, files, and so on), and servers, who store that information (or know where to get it). When you make an HTTP request, it zips through the Internet until it finds the server that knows how to fulfill that request. Then the server sends a response back to you!


							##########
							# Server #
							##########
					  #		##########     #
					#		##########	 	 #
				  #							   #
				#		 #		 #		 #	     #
		#######		    #		 #		  #		   #######
		#Client		   #		 #		   #	   #Client
		#######		  #			 #		    #	   #######
				   #######	  #######    #######
				   #Client	  #Client	 #Client
				   #######	  #######	 #######
				   #######	  #######	 #######
