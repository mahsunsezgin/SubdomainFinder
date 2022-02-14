import requests

domain = input("Enter domain: ")

file = open('subdomains.txt')
content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
	url = "http://{}.{}".format(subdomain, domain)
	try:
		requests.get(url)
		print(url)
	except:
		pass


