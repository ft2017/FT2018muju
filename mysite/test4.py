import urllib.request


req = urllib.request.Request('http://python.org/')  
response = urllib.request.urlopen(req)  
the_page = response.read() 
print(response) 
# if __name__ == "__main__":
# 	main()

# 	print("done")