# BlindXSSScript
Originally made to enumerate a HackTheBox XSS exercise with a registration form, this Python script sends HTTP requests to a target host with a list of payloads. To see how it was made, check out my blogpost on it [here](https://0xparkerrr.github.io/2023/02/13/creating-a-blind-xss-script-htb).

![Script Gif](https://www.andrewpark.blog/_next/static/media/Animation.ed44d728.gif)

**NOTE: This is the second revision to the script. It has improved significantly but user experience is not all the way there yet.**
### Notable Changes:
- First iteration required a manual change of the text file that has the payloads ; Second iteration performs string formatting for the user given an input.
- The script collects ALL parameters, but not all parameters can take in blind XSS payloads ; Implemented a menu selection to pick out what parameters will take expected input (WIP)

## Usage
python3 script.py <url>

Follow the prompts (please see item 2 in Notable Changes)

## Loading the Script
If you've configured everything properly, set a netcat listener on 0.0.0.0 over port 80. You can also do the same with a PHP server.

Execute the script and if there is a vulnerable field, there will be a response on your web listener with the name of the vulnerable parameter.
