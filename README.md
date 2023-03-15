# BlindXSSScript
Originally made to enumerate a HackTheBox XSS exercise with a registration form, this Python script sends HTTP requests to a target host with a list of payloads. To see how it was made, check out my blogpost on it [here](https://www.andrewpark.blog/blind-xss-htb).

![Script Gif](https://www.andrewpark.blog/_next/static/media/Animation.ed44d728.gif)

**NOTE: The code has not been polished. I made it up for the sole purpose of completing the exercise. You could say it's still in development.**

## Usage
The script requires two things: parameters and a target URL.

## Building The Payload
The repo has a payload_template.txt file. For every parameter that's on your target, copy the template and rename it a paramater. 

With a text editor, use the search and replace tool with the following keywords (angle brackets included):
- <URL_HERE> : Your server
- PARAM : include angle brackets. Not sure why markdown is not accepting it.

Do the same with all files, each having different parameters.

### Parameters
Inside the script you will need to configure the payload dictionary to match all the parameters that resides on the target.
<break>
```
payload = { # This is what my target had for parameters
	'fullname': 'script1',
	'username': 'script2',
	'password': 'password',
	'email': 'declined@declined.com',
	'imgurl': 'https%3A%2F%2Fnationaltoday.com%2Fwp-content%2Fuploads%2F2019%2F11%2Famerican-football-day.jpg'
}
```
Just below that dictionary is a with open() function. If you do not have a username parameter, change it accordingly.

In the main inject_payloads() function, you will want to adjust the code accordingly. 
```
with open('param1.txt', 'r') as fname, open('param2.txt', 'r') as uname, open('param3.txt', 'r') as imgurl:
			# appending payloads into a list using the zip() function
			for f, u, i in zip(fname, uname, imgurl):
				
				payload['fullname'] = f		# Replacing paramaters with the payload
				payload['username'] = u
				payload['imgurl'] = i
```
Replace the name of the text files to the name of the text files you have [made] in the same directory of the script. These are the files for the payloads for each parameter. Then change the attribute name. With that, you can adjust the for loop and build on top of it if you have more parameters to test.

### Target
```
r = requests.post('http://<URL HERE>/', params=payload)
```
Replace <URL HERE> with the target host's address.

## Loading the Script
If you've configured everything properly, set a netcat listener on 0.0.0.0 over port 80. You can also do the same with a PHP server.

Execute the script and if there is a vulnerable field, there will be a response on your web listener with the name of the vulnerable parameter.
