import requests
import re
from colorama import init, Fore, Style

# Initialize colorama
init()

# Color definitions
RED = Fore.RED
CYAN = Fore.CYAN
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

# ASCII banner
LOGO = GREEN + """
██████╗░███████╗██████╗░  ░█████╗░██╗░░░░░██████╗░██╗░░██╗███████╗██╗░░██╗░█████╗░
██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗██║░██╔╝██╔════╝██║░░██║██╔══██╗
██████╦╝█████╗░░██████╔╝  ███████║██║░░░░░██████╦╝█████═╝░█████╗░░███████║███████║
██╔══██╗██╔══╝░░██╔═══╝░  ██╔══██║██║░░░░░██╔══██╗██╔═██╗░██╔══╝░░██╔══██║██╔══██║
██████╦╝███████╗██║░░░░░  ██║░░██║███████╗██████╦╝██║░╚██╗███████╗██║░░██║██║░░██║
╚═════╝░╚══════╝╚═╝░░░░░  ╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝

""" + RESET
LINE = YELLOW + "=" * 54 + RESET
TVERSION = CYAN + "\t\t   Version : 2.0.0 " + RESET
DTLS = YELLOW + "\t\t Created By: Redwiat (Modified for SMS)" + RESET
NOTE = CYAN + "Note: Uses BulkSMSBD API. Requires your own API key & sender ID." + RESET

# Print banner
print(LOGO)
print(DTLS)
print(TVERSION)
print(LINE)
print(NOTE)
print(LINE)
print()

# Validate Bangladesh phone number
def is_valid_bd_number(number):
    pattern = r"^(?:\+8801|01)[3-9]\d{8}$"
    return bool(re.match(pattern, number))

# Send SMS
def send_sms(number, message, api_key, sender_id):
    # Remove + if exists
    if number.startswith("+"):
        number = number.replace("+", "")
    url = f"https://bulksmsbd.net/api/smsapi?api_key={api_key}&type=text&number={number}&senderid={sender_id}&message={message}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{GREEN}✅ SMS Sent Successfully to {number}{RESET}")
        else:
            print(f"{RED}❌ Failed to send SMS (Status: {response.status_code}){RESET}")
    except Exception as e:
        print(f"{RED}❌ Error: {str(e)}{RESET}")

# Main function
def main():
    try:
        number = input(RED + "[➙] Enter Your Number (e.g., +8801XXXXXXXXX or 01XXXXXXXXX): " + RESET)
        if not is_valid_bd_number(number):
            print(RED + "Invalid Bangladesh phone number!" + RESET)
            return

        # Your BulkSMSBD API credentials
        api_key = input(CYAN + "[➙] Enter Your BulkSMSBD API Key: " + RESET)
        sender_id = input(CYAN + "[➙] Enter Your Sender ID: " + RESET)

        message = "জয় বাংলা, জয় বঙ্গবন্ধু"
        send_sms(number, message, api_key, sender_id)

    except KeyboardInterrupt:
        print(RED + "\nProcess interrupted by user." + RESET)
    except Exception as e:
        print(RED + f"An error occurred: {str(e)}" + RESET)

if __name__ == "__main__":
    main()