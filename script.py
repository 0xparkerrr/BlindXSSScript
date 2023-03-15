import requests 

# predefine dictionary with arbitrary values
payload = {
	'fullname': 'script1',
	'username': 'script2',
	'password': 'password',
	'email': 'declined@declined.com',
	'imgurl': 'https%3A%2F%2Fnationaltoday.com%2Fwp-content%2Fuploads%2F2019%2F11%2Famerican-football-day.jpg'
} 

# opening a file in the directory to count how many payloads 
# to end loop(s)
num_of_lines = 0

with open('username.txt', 'r') as l:
	for line in l:
		num_of_lines += 1
		




def inject_payloads():
	soo = 0
	
	while soo < num_of_lines:
		# with loop to loop through all lines of the files
		with open('fullname.txt', 'r') as fname, open('username.txt', 'r') as uname, open('imgurl.txt', 'r') as imgurl:
			# appending payloads into a list using the zip() function
			for f, u, i in zip(fname, uname, imgurl):
				
				payload['fullname'] = f		# Replacing paramaters with the payload
				payload['username'] = u
				payload['imgurl'] = i
				r = requests.post('http://<URL HERE>/', params=payload)
				soo += 1
				if str(r) == "<Response [200]>":
					print('Payload successfully sent. Moving to next payload.')
					print('URL: {}\n'.format(r.url))
				else:
					print('error')



print('Detected {0} payloads . . . Starting POST requests.'.format(num_of_lines))	
inject_payloads()
	
	



	

