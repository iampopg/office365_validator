import requests
import threading
from colorama import init, Fore




init(autoreset=True)

red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
background = white + green


print()
print(yellow +  """Coded by Pop(G) - Black Coders Team
                  Contact: @iampopg
                  Telegram: https://t.me/iampopg
                """)

print()

# Define the URL for the API request
url = 'https://login.microsoftonline.com/common/GetCredentialType?mkt=en-US'

# Define the payload template (without the username)
payload_template = {
    "isOtherIdpSupported": True,
    "checkPhones": False,
    "isRemoteNGCSupported": True,
    "isCookieBannerShown": False,
    "isFidoSupported": True,
    "country": "NG",
    "forceotclogin": False,
    "isExternalFederationDisallowed": False,
    "isRemoteConnectSupported": False,
    "federationFlags": 0,
    "isSignup": False,
    "flowToken": "AQABAAEAAAAtyolDObpQQ5VtlI4uGjEPmVTvB5eZTaL_xvRdNX8zoF_M9oCPfpR1_3-Wz9ETrDbl5ca9Avq0LYJkoyoMgY5LIhrw_zFYKZPKDynsKoHPZfgeKmWiIAs1DXbLOrj1FwddvGzTm1ABWqIWhpNkryjIGv9-pljgbUnhPWj9pTn9ffvUpp8V2MtaAhrj46pyDne0WQmgpo5yxrOcie6NRDmX-vIRN1MIuXjLJ27VP51D0OM2hEp1OD47P6dtU6fk3-n2oCqUh1nP1tJCP1Pr47Uw2d3Hx3uCPYHHQJ8S3DkYwNqi4ieYGWQoRIaGrswGKuHiQRsyIuf8jtXEVXyOGqJhVIrV13orhsMe8QFdNAQE95yTcr7oSV6cXL7EWJdelszMsPUosCWSNdpwVI3lFGrKkYHetSaT2PrQem5AJIKBpKpvdLzk4q_P1P5_HA5hrOLCjH451cW4GJ2aVLL8wejgiEdppAzICHiHJOAthyGUP1R7w0z62wD6Ml9QOrRuqGS1KRxOCycJSUhLQcXDX5yIL1PCokaNJIAca5y1wkJb4zMbwhsGoVaUnWZK8XjTWYovsLqEn1dvUW_GrQxdQzwyIAA",
    "isAccessPassSupported": True,
}


headers = {
    "Host": "login.microsoftonline.com",
    # (other headers here)
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close"
}

# Function to make the API request and process the email
def process_email(email,valid_email):
    # Create a copy of the payload template
    payload = payload_template.copy()
    # Set the username in the payload
    payload["username"] = email

    # Make the API request
    response = requests.post(url, json=payload, headers=headers)

    # Check if the response status code is 200
    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()

        # Check if "IfExistsResult" is present in the response JSON
        if "IfExistsResult" in response_json:
            # Extract the value of "IfExistsResult"
            if_exists_result = response_json["IfExistsResult"]

            # Check the value of "IfExistsResult"
            if if_exists_result == 5:
                print(green + f"=>VALID {email}")
                # Save valid email to the 'validEmail.txt' file
                
                with open(valid_email, 'a') as valid_file:
                    valid_file.write(email + '\n')
            else:
                print(red + f"=>INVALID {email} ({if_exists_result})")
        else:
            print(red + f"INVALID INPUT {email}")
    else:
        print(f"API request failed for email {email} with status code:", response.status_code)

try:
    file_path = input(blue + "Enter the file path containing email addresses: ")
    valid_email = input("Name to save the valid email with: ")
    print()
    # Open the file for reading emails
    with open(file_path, 'r') as email_file:

        for line in email_file:
            email = line.strip()  

        
            thread = threading.Thread(target=process_email, args=(email,valid_email))
            thread.start()
except Exception as e:
    print(e)
        
    # print()
    # print(background + 'COMPLETED..')
    # print(yellow + "Valid email saved to validEmail.txt....")
